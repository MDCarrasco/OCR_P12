from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, PermissionsMixin
from datetime import datetime
from django.utils import timezone


class UserManager(BaseUserManager):
    """Define a model manager for User model without username field."""

    use_in_migrations = True

    def _create_user(self, email, group, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, group=group, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, group, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, group, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        group = Group.objects.get(name="superuser")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, group, password, **extra_fields)


class User(AbstractBaseUser):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='%(class)s_group')
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    username = None
    first_name = models.CharField('first name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    is_superuser = models.BooleanField(
        'superuser status',
        default=False,
        help_text=(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff


class Client(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='sales_contact')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def update_date(self):
        self.date_updated = datetime.now()

    def save(self, *args, **kwargs):
        self.update_date()
        return super(Client, self).save()


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    status = models.BooleanField(default=True)
    payment_amount = models.FloatField(default=0.0)
    payment_due = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f'{Client.objects.get(id=self.client.id)} {self.date_created}'

    def update_date(self):
        self.date_updated = datetime.now()

    def save(self, *args, **kwargs):
        self.update_date()
        return super(Contract, self).save()


class Event(models.Model):
    CREATED = 'created'
    INPROGRESS = 'in_progress'
    FINISHED = 'finished'
    EVENT_STATUS = (
        (CREATED, 'created'),
        (INPROGRESS, 'in_progress'),
        (FINISHED, 'finished')
    )

    name = models.CharField(max_length=30, unique=True)
    support_contact = models.ForeignKey(to=User, on_delete=models.CASCADE)
    client = models.ForeignKey(to=Client, on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    event_status = models.CharField(max_length=20, choices=EVENT_STATUS)

    attendees = models.IntegerField(default=0)
    event_date = models.DateTimeField(auto_now_add=False)

    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def update_date(self):
        self.date_updated = datetime.now()

    def save(self, *args, **kwargs):
        self.update_date()
        return super(Event, self).save()

