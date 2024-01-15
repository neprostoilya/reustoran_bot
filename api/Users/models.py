import jwt
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserProfileManager(BaseUserManager):
    """
    Defines user creation fields and manages to save user
    """

    def create_user(self, name, surname, phone, password=None):
        """
        Create User
        """
        if not phone:
            raise ValueError('The Phone number must be set')

        user = self.model(
            name=name,
            surname=surname,
            phone=phone,
        )
        user.save(using=self._db)
        return user


    def create_staffuser(self, name, surname, phone, password=None):
        """
        Create Staff User
        """
        user = self.create_user(
            name=name,
            surname=surname,
            phone=phone,
        )
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, surname, phone, password=None):
        """
        Create SUPER MAN User
        """
        user = self.create_user(
            name=name,
            surname=surname,
            phone=phone,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    Model UserProfile 
    """
    name = models.CharField(
        verbose_name='Имя',
    )
    surname = models.CharField(
        verbose_name='Фамилия'
    )
    phone = models.CharField(
        verbose_name='Номер',
        max_length=15,
        unique=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_admin = models.BooleanField(
        default=False
    )
    
    USERNAME_FIELD = 'phone'

    REQUIRED_FIELDS = ['surname', 'name']

    objects = UserProfileManager()

    def str(self):
        return f'{self.name} {self.surname}'
    
    def __repr__(self) -> str:
        return f'User: name={self.name}, surname={self.surname}, phone={self.phone}'

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
    @property
    def token(self):
        return self.generate_jwt_token()

    def generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=45)
        token = jwt.encode({
            'id': self.pk,
            'exp': dt.strftime('%S')
        },
            settings.SECRET_KEY, algorithm='HS256')
        return token