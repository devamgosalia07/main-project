# Generated by Django 4.1.7 on 2024-03-22 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentprofile', '0004_remove_useranswer_user_useranswer_student_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]