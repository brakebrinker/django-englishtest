# Generated by Django 3.1.4 on 2020-12-04 22:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_questiontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('scores', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('duration_minutes', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questiontype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]