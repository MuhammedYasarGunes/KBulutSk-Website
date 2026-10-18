from django.db import migrations


def kazanildi_degerini_duzelt(apps, schema_editor):
    """Bazı eski kayıtlarda durum 'kazanıldı' (ı ile) olarak duruyor.

    Modeldeki seçenek değeri 'kazanildi'. Panelden girilen kayıtlar zaten
    'kazanildi' olduğu için hepsini aynı değere getiriyoruz.
    """
    Mac = apps.get_model("website", "Mac")
    Mac.objects.filter(durum="kazanıldı").update(durum="kazanildi")


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_remove_galeriöğesi_turu_alter_galeriöğesi_başlık_and_more"),
    ]

    operations = [
        migrations.RunPython(kazanildi_degerini_duzelt, migrations.RunPython.noop),
    ]
