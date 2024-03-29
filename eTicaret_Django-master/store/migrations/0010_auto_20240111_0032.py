# Generated by Django 3.2.23 on 2024-01-10 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='white', max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='description...', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.category'),
        ),
    ]
