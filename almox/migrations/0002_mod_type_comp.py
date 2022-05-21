# Generated by Django 4.0.4 on 2022-05-19 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mod_brand', models.CharField(max_length=120)),
                ('mod_model', models.CharField(max_length=120)),
                ('mod_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_desc', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=255)),
                ('comp_ean', models.CharField(max_length=60)),
                ('comp_nserial', models.CharField(max_length=60)),
                ('comp_addobs', models.TextField()),
                ('comp_status', models.CharField(choices=[('O', 'operante'), ('I', 'inoperante')], max_length=15)),
                ('comp_estado', models.CharField(choices=[('DC', 'disponivel/com caixa'), ('DS', 'disponivel/sem caixa'), ('IND', 'indisponivel'), ('C', 'cedido')], max_length=30)),
                ('comp_loc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almox.loc')),
                ('comp_mod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almox.mod')),
            ],
        ),
    ]