from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, default='0')
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

    def register(self):
        self.save()

    def isExist(self):
        if User.objects.filter(email = self.email):
            return True
        else:
            return False

    @staticmethod
    def loginCustomer(email):
        try:
            return User.objects.get(email = email)
        except:
            return False