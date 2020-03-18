from django.contrib import admin
from .models import Products,StopWords,TrainingData,Category
# Register your models here.
admin.site.register(Products)
admin.site.register(StopWords)
admin.site.register(TrainingData)
admin.site.register(Category)

