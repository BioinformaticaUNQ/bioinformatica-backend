# Generated by Django 3.0.7 on 2020-07-02 11:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200622_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fastaentry',
            name='detalles',
        ),
        migrations.AddField(
            model_name='fastaentry',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fastaentry',
            name='nombre',
            field=models.CharField(max_length=60, unique=True),
        ),
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gb_id', models.CharField(max_length=60)),
                ('sequence', models.TextField()),
                ('latitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=7, max_digits=11, null=True)),
                ('fasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sequences', to='api.FastaEntry')),
            ],
        ),
    ]
