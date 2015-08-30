from __future__ import absolute_import
from celery import shared_task
from django.core.mail import EmailMultiAlternatives


# conf email
subject = 'nuevo compromiso registrado...'

@shared_task
def email_commitments(fm_em, to_em, nb_wl, ds_wl):
    msg = EmailMultiAlternatives(
        subject=subject,
        from_email=fm_em,
        to=to_em,
    )
    msg.global_merge_vars = {
        'nb_wl': nb_wl,
        'ds_wl': ds_wl,
    }
    msg.template_name = "simple_notifications"
    msg.send()

    response_f = {}
    response_m = msg.mandrill_response[0]
    response_f = response_m
    if response_f['status'] == 'sent':
        print 'mensaje enviado con exito'
    else:
        print 'error enviando el mensaje'
