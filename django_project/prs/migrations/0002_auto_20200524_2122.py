# Generated by Django 3.0.6 on 2020-05-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pr',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('pending', 'Pending'), ('approval', 'Approval'), ('on hold', 'On Hold'), ('closed', 'Closed')], default='Open', max_length=10),
        ),
        migrations.AlterField(
            model_name='pr',
            name='pr_number',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
