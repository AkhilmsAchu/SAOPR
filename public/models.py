from django.db import models

# Create your models here.

class Products(models.Model):
	name = models.CharField(max_length=200)
	url = models.CharField(max_length=200)

class StopWords(models.Model):
	name = models.CharField(max_length=200)

class TrainingData(models.Model):
	name = models.CharField(max_length=200)
	label = models.CharField(max_length=200)

class Category(models.Model):
	name = models.CharField(max_length=200)