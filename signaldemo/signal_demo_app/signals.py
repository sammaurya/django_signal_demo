from django.db.models.signals import pre_save, post_save, pre_delete, post_delete,m2m_changed
from django.dispatch import receiver
from .models import UserProfile, Book

@receiver(pre_save, sender=UserProfile)
def pre_save_user_profile(sender, instance, **kwargs):
    instance.username = instance.username.strip().lower()
    instance.first_name = instance.first_name.strip().upper()
    instance.last_name = instance.last_name.strip().upper()
    print("Username: {}\nFirst Name: {}\nLast Name: {}".format(
        instance.username,
        instance.first_name,
        instance.last_name
    ))

@receiver(post_save, sender=UserProfile)
def post_save_user_profile(sender, instance, created, **kwargs):
    print("User Profile is created, an email verification link is send to "+instance.email)

@receiver(pre_delete, sender=UserProfile)
def pre_delete_user_profile(sender, instance, using, **kwargs):
    print("A confirmation link is send to {} to delete the user profile {}".format(
        instance.email,
        instance.username
        ))

@receiver(post_delete, sender=UserProfile)
def post_delete_user_profile(sender, instance, using, **kwargs):
    print("User {} is deleted permanently".format(instance.username))

@receiver(m2m_changed, sender=Book.author.through)
def m2m_changed_user_profile(sender, instance, action, **kwargs):
    user_profile_model = kwargs['model']
    pk_set = kwargs['pk_set']
    if action == 'pre_add':
        for pk in pk_set:
            print("Adding {} as author for the book {}".format(
                user_profile_model.objects.get(username=pk).full_name(),
                instance.title
            ))
    elif action == 'post_add':
        for pk in pk_set:
            print("Added {} as author for the book {}".format(
                user_profile_model.objects.get(username=pk).full_name(),
                instance.title
            ))
    elif action == 'pre_remove':
        for pk in pk_set:
            print("Removing {} as author for the book {}".format(
                user_profile_model.objects.get(username=pk).full_name(),
                instance.title
            ))
    elif action == 'post_remove':
        for pk in pk_set:
            print("Removed {} as author for the book {}".format(
                user_profile_model.objects.get(username=pk).full_name(),
                instance.title
            ))
    elif action == 'pre_clear':
        print("Pre Clear")
        
    elif action == 'post_clear':
        print("Post Clear")


