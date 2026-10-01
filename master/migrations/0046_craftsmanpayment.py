from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0045_backfill_sold_jewelry'),
    ]

    operations = [
        migrations.CreateModel(
            name='CraftsmanPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('craftsman_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField(blank=True, default='')),
                ('work_issue', models.TextField()),
                ('amount_given', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='craftsman_payments', to='master.ordermanagement')),
            ],
        ),
        migrations.CreateModel(
            name='CraftsmanPaymentAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='craftsman_payment_attachments/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='master.craftsmanpayment')),
            ],
        ),
    ]