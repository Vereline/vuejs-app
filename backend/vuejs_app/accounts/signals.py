import logging

from django.conf import settings
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


logger = logging.getLogger(__name__)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender:
    :param reset_password_token:
    :param args:
    :param kwargs:
    :return:
    """
    # TODO: replace this thing to settings
    frontend_url = 'localhost:3000'
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'admin_email': settings.EMAIL_HOST_USER,
        'logo_image_url': '/static/images/favicon.ico',
        'reset_password_url': "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key),
        'reset_password_url_full': "{}/{}?token={}".format(frontend_url,
                                                           reverse('password_reset:reset-password-request'),
                                                           reset_password_token.key),
    }

    # render email text
    email_html_message = render_to_string(settings.STATICFILES_DIRS[0] + '/templates/user_reset_password.html', context)
    email_plaintext_message = render_to_string(settings.STATICFILES_DIRS[0] + '/templates/user_reset_password.txt',
                                               context)

    # https://docs.djangoproject.com/en/2.1/topics/email/

    logger.info("Send restore password message")

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for {title}".format(title="Vuejs_app"),
        # message:
        email_plaintext_message,
        # from:
        # "noreply@somehost.local",
        settings.EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
