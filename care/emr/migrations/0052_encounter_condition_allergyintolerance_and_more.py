# Generated by Django 5.1.3 on 2024-12-27 21:53

import django.contrib.postgres.fields
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emr', '0051_remove_condition_created_by_and_more'),
        ('facility', '0480_delete_patientorganizations'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('encounter_class', models.CharField(blank=True, max_length=100, null=True)),
                ('period', models.JSONField(default=dict)),
                ('hospitalization', models.JSONField(default=dict)),
                ('priority', models.CharField(blank=True, max_length=100, null=True)),
                ('external_identifier', models.CharField(blank=True, max_length=100, null=True)),
                ('facility_organization_cache', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('appointment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='emr.tokenbooking')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='facility.facility')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('clinical_status', models.CharField(blank=True, max_length=100, null=True)),
                ('verification_status', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('severity', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.JSONField(default=dict)),
                ('body_site', models.JSONField(default=dict)),
                ('onset', models.JSONField(default=dict)),
                ('recorded_date', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AllergyIntolerance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('clinical_status', models.CharField(blank=True, max_length=100, null=True)),
                ('verification_status', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('criticality', models.CharField(blank=True, max_length=100, null=True)),
                ('code', models.JSONField(default=dict)),
                ('onset', models.JSONField(default=dict)),
                ('recorded_date', models.DateTimeField(blank=True, null=True)),
                ('last_occurrence', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EncounterOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.facilityorganization')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('status_reason', models.CharField(blank=True, max_length=100, null=True)),
                ('status_changed', models.DateTimeField(blank=True, null=True)),
                ('intent', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('priority', models.CharField(blank=True, max_length=100, null=True)),
                ('do_not_perform', models.BooleanField()),
                ('method', models.JSONField(blank=True, default=dict, null=True)),
                ('authored_on', models.DateTimeField(blank=True, null=True)),
                ('dosage_instruction', models.JSONField(blank=True, default=list, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MedicationStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('status', models.CharField(max_length=100)),
                ('reason', models.CharField(blank=True, max_length=100, null=True)),
                ('medication', models.JSONField(default=dict)),
                ('effective_period', models.JSONField(default=dict)),
                ('information_source', models.CharField(max_length=100)),
                ('dosage_text', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoteThread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoteMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('message', models.TextField()),
                ('message_history', models.JSONField(default=dict)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.notethread')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionnaireResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('subject_id', models.UUIDField()),
                ('responses', models.JSONField(default=list)),
                ('structured_responses', models.JSONField(default=dict)),
                ('structured_response_type', models.CharField(blank=True, default=None, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('questionnaire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emr.questionnaire')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.UUIDField(db_index=True, default=uuid.uuid4, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, db_index=True, null=True)),
                ('deleted', models.BooleanField(db_index=True, default=False)),
                ('history', models.JSONField(default=dict)),
                ('meta', models.JSONField(default=dict)),
                ('status', models.CharField(max_length=255)),
                ('is_group', models.BooleanField(default=False)),
                ('category', models.JSONField(default=dict)),
                ('main_code', models.JSONField(default=dict)),
                ('alternate_coding', models.JSONField(default=list)),
                ('subject_type', models.CharField(max_length=255)),
                ('subject_id', models.UUIDField()),
                ('effective_datetime', models.DateTimeField()),
                ('performer', models.JSONField(default=dict)),
                ('value_type', models.CharField(max_length=255)),
                ('value', models.JSONField()),
                ('note', models.TextField()),
                ('body_site', models.JSONField(default=dict)),
                ('method', models.JSONField(default=dict)),
                ('reference_range', models.JSONField(default=list)),
                ('interpretation', models.CharField(max_length=255)),
                ('parent', models.UUIDField(null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', to=settings.AUTH_USER_MODEL)),
                ('data_entered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observations_entered', to=settings.AUTH_USER_MODEL)),
                ('encounter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.encounter')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emr.patient')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(app_label)s_%(class)s_updated_by', to=settings.AUTH_USER_MODEL)),
                ('questionnaire_response', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='emr.questionnaireresponse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
