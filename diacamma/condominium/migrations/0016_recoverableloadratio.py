# Generated by Django 2.1.7 on 2019-03-05 10:38

import django.core.validators
from django.utils import translation
from django.conf import settings
from django.db import migrations, models
from lucterios.CORE.models import PrintModel


def printer_model(*_args):
    translation.activate(settings.LANGUAGE_CODE)
    PrintModel().load_model("diacamma.condominium", "Owner_0003", is_default=False)


class Migration(migrations.Migration):

    dependencies = [
        ('payoff', '0007_bankaccount'),
        ('condominium', '0015_calldetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoverableLoadRatio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, verbose_name='account')),
                ('ratio', models.DecimalField(decimal_places=0, default=100, max_digits=4, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='ratio')),
            ],
            options={
                'verbose_name': 'recoverable load ratio',
                'verbose_name_plural': 'recoverable load ratios',
                'ordering': ['code'],
                'default_permissions': [],
            },
        ),
        migrations.RunPython(printer_model),
    ]
