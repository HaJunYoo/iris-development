# Generated by Django 4.0.4 on 2022-06-06 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_alter_predresults_ml_param'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresults',
            name='ml_param',
            field=models.CharField(default='default', max_length=30),
        ),
    ]
