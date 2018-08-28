# Generated by Django 2.1 on 2018-08-28 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_title', models.CharField(max_length=30)),
                ('category_description', models.CharField(max_length=1000)),
                ('date_modified', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipe_title', models.CharField(max_length=30)),
                ('recipe_description', models.CharField(max_length=1000)),
                ('date_modified', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Categories')),
            ],
        ),
    ]
