from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, UserManager, AbstractUser


ADMIN = 1
MANAGER = 2
EMPLOYEE = 3


class MyUser(AbstractUser):
    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (MANAGER, 'manager'),
        (EMPLOYEE, 'employee')
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True)

    def __str__(self):
        return f'({self.id}) {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        ordering = ('user', )

    def __str__(self):
        return f'{self.user} - {self.department}'