from django.db.models.base import ModelBase
from django.db.models.signals import post_save
from django.dispatch import receiver


# from .models import Message, Chat


# @receiver(post_save, sender=Message)
# def create_new_message(sender: ModelBase, instance: Message, created: bool, **kwargs):
#
#     if created:
#         instance.chat.last_message = instance
#         instance.chat.save()
