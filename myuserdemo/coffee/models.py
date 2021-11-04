from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.db.models.signals import post_delete, post_save


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save()
        return user


class Account(AbstractBaseUser):
    objects = UserManager()
    email = models.EmailField(unique=True, db_index=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)

    is_active = models.BooleanField('active', default=True)
    is_admin = models.BooleanField('admin', default=False)


    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email


# class Profile(models.Model):
#     GENDER = (
#         ('M', 'Homme'),
#         ('F', 'Femme'),
#     )
#
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     first_name = models.CharField(max_length=120, blank=False)
#     last_name = models.CharField(max_length=120, blank=False)
#     gender = models.CharField(max_length=1, choices=GENDER)
#     zip_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)], blank=False)
#
#     def __unicode__(self):
#         return u'Profile of user: {0}'.format(self.user.email)
#
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# post_save.connect(create_profile, sender=User)

#
# def delete_user(sender, instance=None, **kwargs):
#     try:
#         instance.user
#     except User.DoesNotExist:
#         pass
#     else:
#         instance.user.delete()
#
#
# post_delete.connect(delete_user, sender=Profile)
