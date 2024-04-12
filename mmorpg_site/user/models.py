from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    """Нужен при определении базовой модели пользователя"""
    def create_user(self, username, email, password=None, **kwargs):
        """Создание базового пользователя (без прав)"""

        if not username:
            raise ValueError('Profile needed username')

        if not email:
            raise ValueError('Profile needed email')

        email = self.normalize_email(email).lower()

        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """Создание не базового пользователя (с правами)"""

        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Переопределение базовой модели пользователя.
    Так как форум является игровым, пользовательское имя и почта - уникальные поля.
    Дата создания поста - нужна для возможного функционала по типу годовщин и тому подобное
    Дата времени изменения пароля для внутреннего логирования и безопасности
    Картинка - у каждого пользователя может быть игровая картинка
    STAFF и SUPERUSER - нужны для администрирования системы (выдачи ограничений)"""
    username = models.CharField(unique=True, max_length=255, verbose_name='Nickname')
    email = models.EmailField(unique=True, max_length=255, verbose_name='Email')
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name='Time create')
    date_password_change = models.DateTimeField(null=True, blank=True, verbose_name='Time password change')
    image = models.ImageField(null=True, blank=True, verbose_name='Image')

    is_staff = models.BooleanField(default=False, verbose_name='Staff')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    """Подписка пользователей на еженедельную рассылку"""
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class EmailAccept(models.Model):
    """Прием токенов, игрового имени, почты и пароля, для регистрации и аутентификации"""
    token = models.CharField(max_length=255)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
