from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Email content
        email_subject = f"New Contact Form Submission: {subject}"
        email_message = render_to_string('contact_email.txt', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })

        # Send email to admin
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        
        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact')
    
    return render(request, 'contact.html')


def members(request):
    template = get_template('caurosal_plugin.html')
    return HttpResponse(template.render())
