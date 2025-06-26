from django.db import models
from django.shortcuts import render,redirect
from django.utils.text import slugify

# Create your models here.


class Device(models.Model):
    device=models.CharField(max_length=100)
    def __str__(self):
        return self.device


class Gift_Name(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        context={}
        if self.slug == None:
            slug = slugify(self.name)
            has_slug = Gift_Name.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.name) + "-" + str(count)
                has_slug = Gift_Name.objects.filter(slug=slug).exists()

            self.slug = slug
            
        super().save(*args, **kwargs)
        