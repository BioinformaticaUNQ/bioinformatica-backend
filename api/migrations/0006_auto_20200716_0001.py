# Generated by Django 3.0.7 on 2020-07-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_fastaentry_alignament_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='fastaentry',
            name='newick_tree',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='fastaentry',
            name='alignament_file',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
