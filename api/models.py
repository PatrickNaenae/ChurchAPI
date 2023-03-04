from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Member(models.Model):
    # Membership status
    MINISTER = 'MR'
    WORKER = 'WR'
    MEMBER = 'MB'
    FIRST_TIMER = 'FR'
    MEMBERSHIP_STATUS = [
        (MINISTER, 'Minister'),
        (WORKER, 'Worker'),
        (MEMBER, 'Member'),
        (FIRST_TIMER, 'First timer'),
    ]

    # Occupation
    STUDENT = 'ST'
    BUSINESS = 'BS'
    CORPORATE = 'CE'
    UNEMPLOYED = 'UD'
    OTHERS = 'OS'
    OCCUPATION = [
        (STUDENT, 'Student'),
        (BUSINESS, 'Business'),
        (CORPORATE, 'Corporate'),
        (UNEMPLOYED, 'Unemployed'),
        (OTHERS, 'Others'),
    ]

    # gender
    MALE = 'ME'
    FEMALE = 'FE'
    GENDER_CHOICES =( 
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    first_name = models.CharField(max_length=200, default=None)
    last_name = models.CharField(max_length=200, default=None)
    email = models.CharField(max_length=200, blank=True, null=True, default=None)
    dob = models.CharField(max_length=200, blank=False, null=False, default=None)
    phone = PhoneNumberField(null=False, default=None)
    occupation = models.CharField(max_length=200, choices=OCCUPATION, default=STUDENT)
    membership = models.CharField(max_length=200, choices=MEMBERSHIP_STATUS, default=MINISTER)
    address = models.CharField(max_length=200, blank=True, null=True )
    department = models.CharField(max_length=200, blank=True, null=True )
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES, default=MALE)
    profile_img = models.FileField(upload_to='images', unique=True, default=None, blank=True, null=True)


    def __str__(self):
        return self.first_name + " " + self.last_name

