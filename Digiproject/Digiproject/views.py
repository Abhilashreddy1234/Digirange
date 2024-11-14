from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.encoding import smart_str  # Import smart_str for encoding

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        email_subject = f"New Contact Form Submission: {subject}"

        # Render the email content using a template
        email_message = render_to_string('contact_email.txt', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        })

        # Ensure proper encoding of the email message
        email_message = smart_str(email_message)

        # Send the email to the admin
        send_mail(
            email_subject,
            email_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        # Show success message and redirect
        messages.success(request, "Your message has been sent successfully.")
        return redirect('contact-us')

    return render(request, 'contact-us.html')
