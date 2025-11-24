from django.shortcuts import render , redirect , get_object_or_404
from accounts.models import CustomUserProfile , CustomUser
from jobseeker.forms import JobSeekerCustomUserForm , JobSeekerProfileForm
from django.contrib.auth.decorators import login_required , user_passes_test
from accounts.views import check_jobseeker_perms
from jobseeker.models import Experience , Education
from jobseeker.forms import ExperienceForm , EducationForm
from skill.forms import SkillForm
from skill.models import Skill


# Create your views here.

@login_required
@user_passes_test(check_jobseeker_perms)
def profile(request):

    profile = get_object_or_404(CustomUserProfile, customuser=request.user)
    experiences = Experience.objects.filter(profile=profile)
    educations = Education.objects.filter(profile=profile)
    skills = profile.skills.all()

    context = {
        'profile': profile,
        "experiences":experiences,
        'educations':educations,
        'skills':skills,
    }

    return render(request , 'jobseeker/profile.html', context)



@login_required
@user_passes_test(check_jobseeker_perms)
def edit_jobseekerprofile(request):


    profile_instance = request.user.customuserprofile

    if request.method == 'POST':

        c_form = JobSeekerCustomUserForm(request.POST, instance=request.user)
        p_form = JobSeekerProfileForm(request.POST, request.FILES, instance=profile_instance)

        if c_form.is_valid() and p_form.is_valid():
            c_form.save()
            p_form.save()

            return redirect('profile')


    else:
        c_form = JobSeekerCustomUserForm(instance=request.user)
        p_form = JobSeekerProfileForm(instance=profile_instance)

    context = {
        'c_form': c_form,
        'p_form': p_form,
    }

    return render(request , 'jobseeker/edit_jobseekerprofile.html' , context)





@login_required
@user_passes_test(check_jobseeker_perms)
def add_experience(request):

    if request.method == 'POST':
        form = ExperienceForm(request.POST)

        if form.is_valid():
            exp = form.save(commit=False)
            profile = get_object_or_404(CustomUserProfile, customuser=request.user)
            exp.profile = profile
            exp.save()
            return redirect('profile')
    
    else:
        form = ExperienceForm()

    context = {
        'form': form
    }
    return render(request , 'jobseeker/add_experience.html', context)


@login_required
@user_passes_test(check_jobseeker_perms)
def edit_experience(request , pk):
    exp = get_object_or_404(Experience , pk=pk)

    if request.method == 'POST':

        form = ExperienceForm(request.POST , instance=exp)

        if form.is_valid():
            exps = form.save(commit=False)
            profile = get_object_or_404(CustomUserProfile, customuser=request.user)
            exps.profile = profile
            exps.save()
            return redirect('profile')
            
    else:

        form = ExperienceForm(instance=exp)

    context = {
        'form': form,
        'exp':exp,
    }
    return render(request , 'jobseeker/edit_experience.html', context)


@login_required
@user_passes_test(check_jobseeker_perms)
def delete_experience(request , pk):

    exp = get_object_or_404(Experience , pk=pk)
    exp.delete()

    return redirect('profile')


@login_required
@user_passes_test(check_jobseeker_perms)
def add_education(request):

    if request.method == 'POST':
        form = EducationForm(request.POST)

        if form.is_valid():
            edu = form.save(commit=False)
            profile = get_object_or_404(CustomUserProfile, customuser=request.user)
            edu.profile = profile
            edu.save()
            return redirect('profile')
    
    else:
        form = EducationForm()

    context = {
        'form': form
    }
    return render(request , 'jobseeker/add_education.html', context)


@login_required
@user_passes_test(check_jobseeker_perms)
def edit_education(request , pk):
    edu = get_object_or_404(Education , pk=pk)

    if request.method == 'POST':

        print(EducationForm)

        form = EducationForm(request.POST , instance=edu)


        if form.is_valid():
            edus = form.save(commit=False)
            profile = get_object_or_404(CustomUserProfile, customuser=request.user)
            edus.profile = profile
            edus.save()
            return redirect('profile')
            
    else:

        form = EducationForm(instance=edu)

    context = {
        'form': form,
        'edu':edu,
    }
    return render(request , 'jobseeker/edit_education.html', context)



@login_required
@user_passes_test(check_jobseeker_perms)
def delete_education(request , pk):

    exp = get_object_or_404(Education , pk=pk)
    exp.delete()

    return redirect('profile')


@login_required
@user_passes_test(check_jobseeker_perms)
def add_skill(request):

    profile = CustomUserProfile.objects.get(customuser=request.user)


    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill_name = form.cleaned_data['name']
            skill, created = Skill.objects.get_or_create(name=skill_name)
            profile.skills.add(skill)
            profile.save()
            return redirect('profile') 

    else:

        form = SkillForm()

    context = {
        'form': form,
    }
    return render(request , 'jobseeker/add_skill.html', context)


@login_required
@user_passes_test(check_jobseeker_perms)
def delete_skill(request , pk):

    exp = get_object_or_404(Skill , pk=pk)
    exp.delete()

    return redirect('profile')




