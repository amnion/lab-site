# Generated by Django 2.1.4 on 2018-12-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woolleyMain', '0002_communitydescription_labmissiontext_labnewsitem_researchitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='weblink',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]