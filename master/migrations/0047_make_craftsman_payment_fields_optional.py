from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0046_craftsmanpayment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='craftsmanpayment',
            name='order',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='craftsman_payments',
                to='master.ordermanagement',
            ),
        ),
        migrations.AlterField(
            model_name='craftsmanpayment',
            name='work_issue',
            field=models.TextField(blank=True, default=''),
        ),
    ]