# Generated by Django 3.2.15 on 2024-01-31 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_facebook', models.CharField(max_length=255)),
                ('href_value', models.CharField(max_length=255)),
                ('ptit', models.CharField(max_length=255)),
                ('birth_of_date', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('orientation', models.CharField(max_length=255)),
                ('main_programming_language', models.CharField(max_length=255)),
                ('priority', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('other_note', models.CharField(max_length=255)),
            ],
        ),
    ]