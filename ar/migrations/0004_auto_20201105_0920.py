# Generated by Django 3.0.5 on 2020-11-05 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ar', '0003_division_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.TextField()),
                ('stu_class', models.IntegerField()),
                ('stu_roll', models.IntegerField()),
                ('stu_dept', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='subjects',
            name='lec_no',
        ),
    ]
