from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser




class heroe(models.Model):
    name = models.CharField(max_length = 100)
    biography = models.TextField()
    rewards = models.TextField()
    lived = models.CharField(max_length = 100)
    army = models.ForeignKey('army', on_delete=models.CASCADE, null=True)
    took_part = models.ForeignKey('event', on_delete=models.CASCADE, null=True)

    def _str_(self):
        return self.name

class event(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    result = models.TextField()
    participants = models.ManyToManyField(heroe)
#    date = models.DateField()
#    heroes = models.CharField(max_length = 200)

    def _str_(self):
        return self.title

class army(models.Model):
    name = models.CharField(max_length = 100)
    took_part_events = models.ManyToManyField(event)
#    heroes = models.ForeignKey(heroe, on_delete=models.CASCADE, null=True)
    comander = models.CharField(max_length = 100)

    def _str_(self):
        return self.name


class date(models.Model):
    date = models.DateField()
    date_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

class place(models.Model):
    place = models.CharField(max_length = 200)
    place_id = models.ForeignKey(event, on_delete=models.CASCADE, null=True)

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not username:
            raise ValueError('Users must have a name')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, default="")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
