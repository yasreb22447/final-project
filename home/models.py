from django.db import models

class universities(models.Model):
  Field_of_study = models.CharField(max_length=255, null=True)
  location = models.CharField(max_length=255)
  university = models.CharField(max_length=255,)
  time = models.DateTimeField(null=True)
  Degree = models.CharField(max_length=225, null=True)
  funding_type = models.CharField(max_length=255, null=True)
  Eligible_Countreies = models.CharField(max_length=255, null=True)



class canada(models.Model):
  Field_of_study = models.CharField(max_length=225)
  location = models.CharField(max_length=255)
  university = models.CharField(max_length=255,)
  time = models.DateTimeField(null=True)
  Degree = models.CharField(max_length=225, null=True)
  funding_type = models.CharField(max_length=255, null=True)
  Eligible_Countreies = models.CharField(max_length=255, null=True)





class germany(models.Model):
  Field_of_study = models.CharField(max_length=225)
  location = models.CharField(max_length=255)
  university = models.CharField(max_length=255,)
  time = models.DateTimeField(null=True)
  Degree = models.CharField(max_length=225, null=True)
  funding_type = models.CharField(max_length=255, null=True)
  Eligible_Countreies = models.CharField(max_length=255, null=True)




class USA(models.Model):
  Field_of_study = models.CharField(max_length=225)
  location = models.CharField(max_length=255)
  university = models.CharField(max_length=255,)
  time = models.DateTimeField(null=True)
  Degree = models.CharField(max_length=225, null=True)
  funding_type = models.CharField(max_length=255, null=True)
  Eligible_Countreies = models.CharField(max_length=255, null=True)
  