from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ApplicationInquiry

def admission_info(request):
    return render(request, 'admissions/info.html')

def application_inquiry(request):
    if request.method == 'POST':
        ApplicationInquiry.objects.create(
            parent_name=request.POST.get('parent_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            child_name=request.POST.get('child_name'),
            child_dob=request.POST.get('child_dob'),
            program_interest=request.POST.get('program_interest'),
            message=request.POST.get('message', ''),
        )
        messages.success(request, 'Your inquiry has been submitted. The admissions office will contact you.')
        return redirect('admissions:info')
    return render(request, 'admissions/inquiry_form.html')