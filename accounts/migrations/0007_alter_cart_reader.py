# Generated by Django 3.2.5 on 2022-06-12 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_staff_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='reader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.reader'),
        ),
    ]
