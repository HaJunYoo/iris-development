# Generated by Django 4.0.3 on 2022-05-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predresults',
            name='ml_algorithm',
            field=models.CharField(default='KNeighborsClassifier(n_neighbors=1)', max_length=30),
        ),
    ]
