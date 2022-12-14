# Generated by Django 3.1 on 2022-12-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bacent', '0002_toppost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('tanlov', models.CharField(max_length=20)),
                ('malumot', models.DateTimeField(auto_now_add=True)),
                ('rasm', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='ism',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='malumot',
        ),
        migrations.RenameField(
            model_name='toppost',
            old_name='name',
            new_name='ism',
        ),
        migrations.RenameField(
            model_name='toppost',
            old_name='date',
            new_name='malumot',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
