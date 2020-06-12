from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import VolunteerApplicationForm

from django.core.mail import send_mail

default_from_email = 'webmaster@bridge-hospice.com'
support_email = 'support@bridge-hospice.com'


def volunteer_form(request):
    if request.method == 'POST':
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            subject = 'Your volunteer form has been submitted for review'

            message = \
                f"Hello {form.cleaned_data['first_name']} {form.cleaned_data['last_name']},\n" \
                '\n' \
                'Your volunteer application has been submitted. Please allow 3-5 business days for our team to review your application.\n' \
                'After the review, a member of our team will contact you with additional information related to our volunteer program with the information you provided.\n\n' \
                'Thank you,\n' \
                'The Bridge Hospice Staff\n'
            send_mail(subject, message, default_from_email, [form.cleaned_data['email_address']])
            message2 = \
                "Hello Support Team,\n\n" \
                f"{form.cleaned_data['first_name']} {form.cleaned_data['last_name']} has completed a volunteer application.\n\n" \
                f"Their contact information is mobile: {form.cleaned_data['mobile_phone']} and email: {form.cleaned_data['email_address']}. "\
                f"They heard about us [{form.cleaned_data['source']}] and want to apply to work as a {form.cleaned_data['volunteer_type']}.\n\n" \
                f"Their reason for wanting to be involved is: [{form.cleaned_data['reason']}].\n\n" \
                f"Lastly, their relationship with significant loss is: [{form.cleaned_data['personal_loss']}]\n\n" \
                f"For additional information please visit the https://bridge-hospice.com/admin site and find volunteer applications.\n\n" \
                f"Thanks Support Team,\n -- Webmaster [Automated] --"

            send_mail(subject, message2, default_from_email, [support_email])
            return HttpResponseRedirect('/forms/volunteer/thanks/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'volunteer_form.html', context)

    form = VolunteerApplicationForm()
    context = {
        'form': form,
    }
    return render(request, 'volunteer_form.html', context)


def build_form_email(form):


    return message
