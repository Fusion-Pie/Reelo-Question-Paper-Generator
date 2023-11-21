# Generated by Django 4.2.7 on 2023-11-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsDB',
            fields=[
                ('questionId', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
                ('correctAns', models.CharField(max_length=100)),
                ('incorrectAns', models.CharField(max_length=500)),
                ('difficulty', models.CharField(choices=[('NA', 'None'), ('E', 'easy'), ('M', 'medium'), ('H', 'hard')], default='NA', max_length=2)),
                ('type', models.CharField(choices=[('None', 'None'), ('Mult', 'multiple'), ('Bool', 'boolean')], default='None', max_length=4)),
            ],
        ),
    ]