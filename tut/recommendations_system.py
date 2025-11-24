from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from adminsetup.models import Job
from accounts.models import CustomUserProfile



def job_skills_text(job):
    return " ".join([skill.name.lower() for skill in job.skills.all()])

def user_skills_text(user_profile):
    return " ".join([skill.name.lower() for skill in user_profile.skills.all()])

def experience_similarity(user_exp, job_exp):
    max_exp = max(user_exp, job_exp, 1)
    diff = abs(user_exp - job_exp)
    sim = 1 - (diff / max_exp)
    return max(sim, 0)

def recommend_jobs(user_profile, send_email=False):
    user_text = user_skills_text(user_profile).strip()
    jobs = Job.objects.filter(is_active=True)

    # --- Skill scores ---
    if user_text:
        job_texts = [job_skills_text(job) for job in jobs]
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([user_text] + job_texts)
        user_vec = tfidf_matrix[0]
        job_vecs = tfidf_matrix[1:]
        skill_scores = cosine_similarity(user_vec, job_vecs).flatten()
    else:
        skill_scores = [0] * len(jobs)

    # --- Experience scores ---
    if user_profile.total_years_of_experience > 0:
        exp_scores = [
            experience_similarity(user_profile.total_years_of_experience, job.total_years_of_experience_required)
            for job in jobs
        ]
    else:
        exp_scores = [0] * len(jobs)

    # --- Determine weights ---
    has_skills = bool(user_text)
    has_exp = user_profile.total_years_of_experience > 0

    if has_skills and has_exp:
        skill_weight, exp_weight = 0.7, 0.3
        reason_type = "Both skills and experience"
    elif has_skills:
        skill_weight, exp_weight = 1.0, 0.0
        reason_type = "Skills match"
    elif has_exp:
        skill_weight, exp_weight = 0.0, 1.0
        reason_type = "Experience match"
    else:
        skill_weight, exp_weight = 0.5, 0.5
        reason_type = "No skills or experience"

    # --- Combine scores ---
    results = []
    for i, job in enumerate(jobs):
        final_score = (skill_weight * skill_scores[i]) + (exp_weight * exp_scores[i])
        results.append({
            "job": job,
            "final_score": final_score,
            "skill_score": skill_scores[i],
            "experience_score": exp_scores[i],
            "reason": reason_type
        })

    # --- Find highest score ---
    if not results:
        return []

    max_score = max(results, key=lambda x: x["final_score"])["final_score"]
    top_jobs = [r for r in results if r["final_score"] == max_score]

  

    return top_jobs

