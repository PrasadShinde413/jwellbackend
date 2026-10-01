from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0047_make_craftsman_payment_fields_optional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftsmanpayment',
            name='craftsman_name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='craftsmanpayment',
            name='phone_number',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]