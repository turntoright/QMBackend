# Generated by Django 3.2 on 2021-04-30 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20210429_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoteitem',
            name='quote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='quotes.quote'),
        ),
    ]
