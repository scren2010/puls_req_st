# Generated by Django 3.2.7 on 2021-09-16 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_link', models.URLField(unique=True, verbose_name='Ссылка на публичный репозиторий')),
            ],
        ),
        migrations.CreateModel(
            name='UserRequestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pull_request', models.CharField(max_length=255)),
                ('pull_request_link', models.URLField()),
                ('pull_request_reviewers', models.CharField(blank=True, max_length=100, verbose_name='Reviewers (usernames)')),
                ('pull_request_assignees', models.CharField(blank=True, max_length=100, verbose_name='Assignees (usernames)')),
                ('user_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pull_req_app.userrequest')),
            ],
        ),
    ]
