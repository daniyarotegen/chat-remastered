# Generated by Django 4.2.1 on 2023-05-22 07:22

import chatrooms.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatrooms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='chat_type',
            field=models.CharField(choices=[('PRIVATE', 'Private'), ('GROUP', 'Group')], default=chatrooms.models.ChatType['PRIVATE'], max_length=7),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='is_group',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ChatRoomMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('chat_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatrooms.chatroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]