# Generated by Django 3.1.3 on 2021-09-11 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210911_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accept', 'Accept'), ('Cancel', 'Cancel')], default='Pending', max_length=25),
        ),
    ]
