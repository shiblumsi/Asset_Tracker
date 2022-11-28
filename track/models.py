from django.db import models
import datetime
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from uuid import uuid4
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None, password2=None):
      
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
     
        user = self.create_user(
            email,
            password=password,
            name=name,
          
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    alias = models.UUIDField(default=uuid4, editable=False)
    email = models.EmailField(max_length=200,verbose_name='Email',unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
       
        return self.is_admin

    def has_module_perms(self, app_label):
    
        return True

    @property
    def is_staff(self):
       
        return self.is_admin






class Employee(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200, null=True,blank=True)
    email = models.CharField(max_length=200, blank=True,null=True)
    designation = models.CharField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.name


class Asset(models.Model):
    Devise = [
        ('PHONE','Phone'),
        ('TABLET','Tablet'),
        ('LAPTOP','Laptop')
    ]
    
    asset_type = models.CharField(max_length=200,choices=Devise)
    model_no = models.CharField(max_length=200)
    brand = models.CharField(max_length=200,null=True,blank=True)
    


    def __str__(self):
        return self.model_no



class DelegateTo(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='delegateto')
    assets = models.ManyToManyField(Asset,null=True,blank=True,related_name='asset')
    checked_out_at = models.DateTimeField(default=datetime.datetime.now)
    condition = models.CharField(max_length=200,null=True,blank=True)
    

    def __str__(self):
        return str(self.employee)



class GiveBack(models.Model):
    returned_condition = models.CharField(max_length=200)
    returned_date = models.DateTimeField(default=datetime.datetime.now)
    delegat = models.ForeignKey(DelegateTo,on_delete=models.CASCADE,related_name='employee_name')
    model = models.ForeignKey(Asset,on_delete=models.CASCADE,related_name='asset_model')

    @property
    def checked_out_time(self):
        return self.delegat.checked_out_at

    @property
    def asset_type(self):
        return self.model.asset_type

    @property
    def delegate_condition(self):
        return self.delegat.condition
    @property
    def employee_name(self):
        return self.delegat.employee.name
    
    @property
    def brand(self):
        return self.model.brand
