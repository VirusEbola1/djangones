# Generated by Django 4.2.7 on 2024-03-20 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_game_embed_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('platform', models.CharField(max_length=50)),
                ('release_date', models.DateField()),
                ('rom_file', models.FileField(upload_to='sega/')),
            ],
        ),
    ]
