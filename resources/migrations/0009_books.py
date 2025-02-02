# Generated by Django 5.0.2 on 2024-02-17 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_notes_thumbnail_qpaper_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('book_link', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thumbnails/')),
                ('standard', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resources.standard')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.subject')),
            ],
        ),
    ]
