# Generated by Django 3.2.9 on 2022-01-03 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0003_auto_20220103_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('1', 'LCD TV'), ('2', 'Computer'), ('3', 'Laptop'), ('4', 'Lamp'), ('5', 'Electric heater'), ('6', 'Air conditioner'), ('7', 'Mini-fridge'), ('8', 'Fan'), ('9', 'Extension cord'), ('10', 'Smartphone carger')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Appliances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appliance_name', models.CharField(max_length=20)),
                ('label_class', models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D'), ('5', 'E'), ('6', 'F'), ('7', 'G')], max_length=1)),
                ('energycomsuption', models.IntegerField()),
                ('room_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
                ('type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appliances.type')),
            ],
        ),
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appliances.type')),
            ],
        ),
    ]