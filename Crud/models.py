from django.db import models


class King(models.Model):
    name = models.CharField(max_length=50)
    display_mode = models.CharField(max_length=50)
    flashing = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    repetition = models.CharField(max_length=50)
    interval = models.CharField(max_length=50)
    font_size = models.CharField(max_length=50)
    layout = models.CharField(max_length=50)
    background_width = models.CharField(max_length=50)
    background_height = models.CharField(max_length=50)
    x_pos = models.CharField(max_length=50)



class Dummy(models.Model):
    name = models.CharField(max_length=50)
    programs = models.CharField(max_length=50)
    display_mode = models.CharField(max_length=50)
    force_displaying = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    font_size = models.CharField(max_length=50)
    layout = models.CharField(max_length=50)
