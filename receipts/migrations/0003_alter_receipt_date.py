# Generated by Django 4.1.1 on 2022-09-09 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receipts", "0002_alter_receipt_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]