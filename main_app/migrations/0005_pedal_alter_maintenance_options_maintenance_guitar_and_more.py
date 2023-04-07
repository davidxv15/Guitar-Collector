# Generated by Django 4.1.7 on 2023-04-06 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_maintenance_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='maintenance',
            name='guitar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.guitar'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='date',
            field=models.DateField(verbose_name='Maintenance Date'),
        ),
        migrations.AddField(
            model_name='guitar',
            name='pedals',
            field=models.ManyToManyField(to='main_app.pedal'),
        ),
    ]