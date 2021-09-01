from django.db import models
import uuid

# Create your models here.

# definition de notre classe User
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __int__(self):
        return self.id

# definition de la classe Role
class Role(models.Model):
    id =  models.UUIDField(primary_key= True, default=uuid.uuid4, editable=False)
    label = models.CharField(max_length= 250)
    role_id =  models.UUIDField(primary_key= False, default=uuid.uuid4, editable=False)
    role_id_ssd =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, verbose_name='role_id_ssd')
    role_id_dsd =  models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False, verbose_name='role_id_dsd')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.label 
              
# definition de la classe User_role
class User_role(models.Model):
    user_id = models.ForeignKey(Role, on_delete = models.CASCADE)
    role_id = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.user_id


#definition de la table Object
class Object(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    label = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.label

# definition de la table Operation
class Operation(models.Model):
    CREATE = 'CREATE'
    READ = 'READ'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    VISIBLE = 'VISIBLE'
    PRINT = 'PRINT'
    STATUS_CHOICES = [
        (CREATE, 'Create'),
        (READ, 'Read'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
        (VISIBLE, 'Visible'),
        (PRINT, 'Print'),
    ]
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length= 120, null=True)
    type = models.CharField(max_length= 10, choices= STATUS_CHOICES, default= READ,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description

# definition dela table Permission
class Permission(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    object_id = models.ForeignKey(Object, on_delete = models.CASCADE)
    operation_id = models.ForeignKey(Operation, on_delete = models.CASCADE)
    label = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.label

# definition de la classe Permission_role
class Permission_role(models.Model):
    permission_id = models.ForeignKey(Permission, on_delete = models.CASCADE)
    role_id =  models.ForeignKey(Role, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.permission_id



