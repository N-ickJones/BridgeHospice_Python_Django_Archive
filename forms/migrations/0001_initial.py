# Generated by Django 2.2 on 2020-06-02 00:00

from django.db import migrations, models
import localflavor.us.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=64)),
                ('last_name', models.CharField(default='', max_length=64)),
                ('address', models.CharField(default='', max_length=128)),
                ('city', models.CharField(default='', max_length=64)),
                ('state', localflavor.us.models.USStateField(default='TX', max_length=2)),
                ('zip_code', localflavor.us.models.USZipCodeField(default='', max_length=10)),
                ('home_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+1', max_length=128, null=True, region=None)),
                ('work_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+1', max_length=128, null=True, region=None)),
                ('mobile_phone', phonenumber_field.modelfields.PhoneNumberField(default='+1', max_length=128, region=None)),
                ('emergency_contact', phonenumber_field.modelfields.PhoneNumberField(default='+1', max_length=128, region=None)),
                ('email_address', models.EmailField(default='', max_length=128)),
                ('marital_status', models.CharField(choices=[('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widowed')], default=None, max_length=1, null=True)),
                ('source', models.CharField(default='', max_length=128, verbose_name='How did you learn of Bridge Hospice?')),
                ('volunteer_agency_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Agency 1')),
                ('volunteer_city_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('volunteer_state_1', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('volunteer_duties_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Duties')),
                ('volunteer_supervisor_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Supervisor')),
                ('volunteer_start_date_1', models.DateField(blank=True, default=None, null=True, verbose_name='Start Date')),
                ('volunteer_end_date_1', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
                ('volunteer_agency_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Agency 2')),
                ('volunteer_city_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('volunteer_state_2', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('volunteer_duties_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Duties')),
                ('volunteer_supervisor_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Supervisor')),
                ('volunteer_start_date_2', models.DateField(blank=True, default=None, null=True, verbose_name='Start Date')),
                ('volunteer_end_date_2', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
                ('volunteer_agency_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Agency 3')),
                ('volunteer_city_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('volunteer_state_3', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('volunteer_duties_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Duties')),
                ('volunteer_supervisor_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Supervisor')),
                ('volunteer_start_date_3', models.DateField(blank=True, default=None, null=True, verbose_name='Start Date')),
                ('volunteer_end_date_3', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
                ('employment_employer_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Employer 1')),
                ('employment_city_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('employment_state_1', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('employment_title_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Title')),
                ('employment_start_date_1', models.DateField(blank=True, default=None, null=True, verbose_name='Start Date')),
                ('employment_end_date_1', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
                ('employment_employer_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Employer 2')),
                ('employment_city_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('employment_state_2', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('employment_title_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Title')),
                ('employment_start_date_2', models.DateField(blank=True, default=None, null=True, verbose_name='Start Date')),
                ('employment_end_date_2', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
                ('employment_employer_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Employer 3')),
                ('employment_city_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('employment_state_3', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('employment_title_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Title')),
                ('employment_start_date_3', models.DateField(blank=True, default=None, null=True, verbose_name='Start Date')),
                ('employment_end_date_3', models.DateField(blank=True, default=None, null=True, verbose_name='End Date')),
                ('education_school_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Education 1')),
                ('education_city_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('education_state_1', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('education_years_studied_1', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Years Studied')),
                ('education_degree_1', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Degree/Diploma')),
                ('education_date_completed_1', models.DateField(blank=True, default=None, null=True, verbose_name='Date Completed')),
                ('education_school_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Education 2')),
                ('education_city_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('education_state_2', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('education_years_studied_2', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Years Studied')),
                ('education_degree_2', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Degree/Diploma')),
                ('education_date_completed_2', models.DateField(blank=True, default=None, null=True, verbose_name='Date Completed')),
                ('education_school_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Education 3')),
                ('education_city_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='City')),
                ('education_state_3', localflavor.us.models.USStateField(blank=True, default=None, max_length=2, null=True, verbose_name='State')),
                ('education_years_studied_3', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='Years Studied')),
                ('education_degree_3', models.CharField(blank=True, default=None, max_length=64, null=True, verbose_name='Degree/Diploma')),
                ('education_date_completed_3', models.DateField(blank=True, default=None, null=True, verbose_name='Date Completed')),
                ('licenses', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='List any professional licenses (include type and license #).')),
                ('training', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='Describe any special training, apprenticeship, skills (such as languages spoken other than English), or other activities that you feel may be helpful as a volunteer.')),
                ('volunteer_type', models.CharField(choices=[('D', 'Direct Patient Care Activities – working directly with the patients and their families (may include patient visitation, caregiver respite, telephone contacts, errands, etc.)'), ('I', 'Indirect Patient Activities - not working directly with the patients (may include yard work, pet care, light construction, sewing, baking, treats/gifts, projects, etc.)'), ('A', 'Administrative Activities (may include typing, mailings, filing, phone support, copying, faxing, special projects, etc.)')], default=None, max_length=1, null=True)),
                ('sunday_availability', models.CharField(choices=[('am', 'Morning'), ('pm', 'Afternoon'), ('both', 'Full-Day'), ('none', 'Not Available')], default=None, max_length=4, null=True)),
                ('monday_availability', models.CharField(choices=[('am', 'Morning'), ('pm', 'Afternoon'), ('both', 'Full-Day'), ('none', 'Not Available')], default=None, max_length=4, null=True)),
                ('tuesday_availability', models.CharField(choices=[('am', 'Morning'), ('pm', 'Afternoon'), ('both', 'Full-Day'), ('none', 'Not Available')], default=None, max_length=4, null=True)),
                ('wednesday_availability', models.CharField(choices=[('am', 'Morning'), ('pm', 'Afternoon'), ('both', 'Full-Day'), ('none', 'Not Available')], default=None, max_length=4, null=True)),
                ('thursday_availability', models.CharField(choices=[('am', 'Morning'), ('pm', 'Afternoon'), ('both', 'Full-Day'), ('none', 'Not Available')], default=None, max_length=4, null=True)),
                ('friday_availability', models.CharField(choices=[('am', 'Morning'), ('pm', 'Afternoon'), ('both', 'Full-Day'), ('none', 'Not Available')], default=None, max_length=4, null=True)),
                ('saturday_availability', models.CharField(choices=[('am', 'Morning'), ('pm', 'Afternoon'), ('both', 'Full-Day'), ('none', 'Not Available')], default=None, max_length=4, null=True)),
                ('reason', models.TextField(default='', max_length=255, verbose_name='Please state briefly your reasons for wanting to be involved with hospice.')),
                ('personal_loss', models.TextField(default='', max_length=255, verbose_name='Please write briefly about your personal experience with significant loses (deaths, divorce, etc.). For deaths, please indicate the relationship, dates and state your level of involvement.')),
                ('felony', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1, verbose_name='Have you ever been convicted of a felony? (Disclosure of this information will not necessarily preclude you from becoming a volunteer with our organization.)')),
                ('conviction', models.TextField(blank=True, default=None, max_length=255, null=True, verbose_name='If so, please provide information regarding type and date of which the felony occurred.')),
            ],
        ),
    ]
