from django.db import models

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)
    address=models.CharField(max_length=70,null=True)
    photo=models.ImageField('Your Image in jpg/png Format',upload_to=' ')
    birthcertif=models.ImageField('Your Image in jpg/png Format',upload_to=' ')
    adaar=models.ImageField('Your Image in jpg/png Format',upload_to=' ')
    sslc=models.ImageField('Your Image in jpg/png Format',upload_to=' ')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.amount}"
