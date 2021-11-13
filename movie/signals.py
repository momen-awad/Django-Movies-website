from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movie
from django.core.mail import send_mail


#@receiver(post_save, sender=Movie)
#def new_movie_mail(sender, instance, created, *args, **kwargs):
#    send_mail(
#        subject = 'New movie created',
#        message = 'dear user a new movie {} is created '.format(instance.name),
#        from_email = 'awadmomen@gmail.com',
#        recipient_list = ['awadmomen@gmail.com'],
#        fail_silently = False
#    )
