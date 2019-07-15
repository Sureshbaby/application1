# Generated by Django 2.2.3 on 2019-07-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('programs', models.CharField(max_length=50)),
                ('display_mode', models.CharField(max_length=50)),
                ('force_displaying', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('font_size', models.CharField(max_length=50)),
                ('layout', models.CharField(max_length=50)),
                ('background_width', models.CharField(max_length=50)),
                ('background_height', models.CharField(max_length=50)),
                ('x_pos', models.CharField(max_length=50)),
                ('y_pos', models.CharField(max_length=50)),
                ('background_transparent', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='King',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('display_mode', models.CharField(max_length=50)),
                ('flashing', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('repetition', models.CharField(max_length=50)),
                ('interval', models.CharField(max_length=50)),
                ('font_size', models.CharField(max_length=50)),
                ('layout', models.CharField(max_length=50)),
                ('background_width', models.CharField(max_length=50)),
                ('background_height', models.CharField(max_length=50)),
                ('x_pos', models.CharField(max_length=50)),
                ('y_pos', models.CharField(max_length=50)),
                ('font_color', models.CharField(max_length=50)),
                ('background_color', models.CharField(max_length=50)),
                ('background_transparent', models.CharField(max_length=50)),
                ('display_device_id', models.CharField(max_length=50)),
                ('display_stb_id', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=50)),
            ],
        ),
    ]