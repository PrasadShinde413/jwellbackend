from django.db import migrations


def backfill_sold_jewelry(apps, schema_editor):
    Jewelry = apps.get_model('master', 'Jewelry')
    SaleItem = apps.get_model('master', 'SaleItem')
    SoldJewelry = apps.get_model('master', 'SoldJewelry')

    for sale_item in SaleItem.objects.filter(jewelry__isnull=True).exclude(
        qr_barcode_id__isnull=True
    ).exclude(qr_barcode_id=''):
        try:
            jewelry_id = int(sale_item.qr_barcode_id)
        except (TypeError, ValueError):
            continue

        jewelry = Jewelry.objects.filter(pk=jewelry_id).first()
        if not jewelry:
            continue

        sale_item.jewelry_id = jewelry.id
        sale_item.save(update_fields=['jewelry'])
        SoldJewelry.objects.get_or_create(
            jewelry_id=jewelry.id,
            defaults={
                'sale_item_id': sale_item.id,
                'customer_id': sale_item.customer_id,
            },
        )


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0044_soldjewelry_saleitem_jewelry'),
    ]

    operations = [
        migrations.RunPython(backfill_sold_jewelry, migrations.RunPython.noop),
    ]