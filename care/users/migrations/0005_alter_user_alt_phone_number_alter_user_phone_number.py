# Generated by Django 4.2.2 on 2023-06-26 12:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_district_id_alter_localbody_id_alter_skill_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="alt_phone_number",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=14,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^(?:(?:(?:\\+|0{0,2})91|0{0,2})(?:\\()?\\d{3}(?:\\))?[\\-]?\\d{3}[\\-]?\\d{4})$",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                max_length=14,
                validators=[
                    django.core.validators.RegexValidator(
                        code="invalid_mobile",
                        message="Please Enter 10/11 digit mobile number or landline as 0<std code><phone number>",
                        regex="^(?:(?:(?:\\+|0{0,2})91|0{0,2})(?:\\()?\\d{3}(?:\\))?[\\-]?\\d{3}[\\-]?\\d{4})$",
                    )
                ],
            ),
        ),
    ]