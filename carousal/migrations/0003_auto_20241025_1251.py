# Generated by Django 3.1.14 on 2024-10-25 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('carousal', '0002_auto_20241025_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='carousal_carousel', serialize=False, to='cms.cmsplugin')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel_images/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('carousel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='carousal.carousel')),
            ],
        ),
        migrations.DeleteModel(
            name='TextCardPluginModel',
        ),
    ]
