from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Pizza(models.Model):
  id = models.AutoField(primary_key=True)
  size = models.ForeignKey('Size', on_delete=models.CASCADE, default=1)
  crust = models.ForeignKey('Crust', on_delete=models.CASCADE, default=2)
  sauce = models.ForeignKey('Sauce', on_delete=models.CASCADE, default=1)
  cheese = models.ForeignKey('Cheese', on_delete=models.CASCADE, default=1)
  toppings = models.ManyToManyField('Toppings')

class Size(models.Model):
  id = models.AutoField(primary_key=True)
  size = models.CharField(max_length=30)
  def __str__(self):
    return self.size

class Crust(models.Model):
  id = models.AutoField(primary_key=True)
  crust = models.CharField(max_length=30)
  def __str__(self):
    return self.crust

class Sauce(models.Model):
  id = models.AutoField(primary_key=True)
  sauce = models.CharField(max_length=30)
  def __str__(self):
    return self.sauce

class Cheese(models.Model):
  id = models.AutoField(primary_key=True)
  cheese = models.CharField(max_length=30)
  def __str__(self):
    return self.cheese

class Toppings(models.Model):
  topping = models.CharField(max_length=30, editable=True)
  def __str__(self):
    return self.topping

class PaymentInfo(models.Model):
  id = models.AutoField(primary_key=True)
  name_on_card = models.CharField(max_length=100)
  card_number = models.IntegerField(validators=[MaxValueValidator(9999999999999999)])
  expiration_month = models.IntegerField(validators=[MaxValueValidator(12), MinValueValidator(1)])
  expiration_year = models.IntegerField(validators=[MaxValueValidator(9999), MinValueValidator(2024)])
  cvv = models.IntegerField()
  address_line_1 = models.CharField(max_length=100)
  address_line_2 = models.CharField(max_length=100, blank=True)
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  zip_code = models.CharField(max_length=10)
  

class PizzaOrder(models.Model):
  id = models.AutoField(primary_key=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
  payment = models.ForeignKey(PaymentInfo, on_delete=models.CASCADE, null=True)
  date_ordered = models.DateTimeField(auto_now_add=True)