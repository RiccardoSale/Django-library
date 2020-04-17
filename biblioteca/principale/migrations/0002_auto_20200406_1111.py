# Generated by Django 2.1.5 on 2020-04-06 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoreLibro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'AUTORI-LIBRI',
            },
        ),
        migrations.CreateModel(
            name='Autori',
            fields=[
                ('idAutore', models.AutoField(primary_key=True, serialize=False)),
                ('CognomeNome', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'AUTORI',
            },
        ),
        migrations.CreateModel(
            name='Collocazione',
            fields=[
                ('idCollocazione', models.AutoField(primary_key=True, serialize=False)),
                ('Collocazione', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'COLLOCAZIONI',
            },
        ),
        migrations.CreateModel(
            name='Dewey',
            fields=[
                ('codiceDewey', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('Dewey', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'CodiciDewey',
            },
        ),
        migrations.CreateModel(
            name='EDITORI',
            fields=[
                ('IdEditore', models.AutoField(primary_key=True, serialize=False)),
                ('editore', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'EDITORI',
            },
        ),
        migrations.CreateModel(
            name='LibriInDisuso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateTimeField()),
                ('Motivo', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name_plural': 'LIBRI In DISUSO',
            },
        ),
        migrations.CreateModel(
            name='Prestito',
            fields=[
                ('idPrestito', models.AutoField(primary_key=True, serialize=False)),
                ('dataPrelievo', models.DateTimeField(null=True)),
                ('dataRestituzione', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'PRESTITI',
            },
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('IdSede', models.AutoField(primary_key=True, serialize=False)),
                ('Sede', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'SEDI',
            },
        ),
        migrations.CreateModel(
            name='Stato',
            fields=[
                ('idStato', models.AutoField(primary_key=True, serialize=False)),
                ('Stato', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'STATI',
            },
        ),
        migrations.CreateModel(
            name='Utente',
            fields=[
                ('idUtente', models.AutoField(primary_key=True, serialize=False)),
                ('CognomeNome', models.CharField(max_length=255)),
                ('Classe', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'UTENTI',
            },
        ),
        migrations.AddField(
            model_name='libro',
            name='Luogopubblicazione',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libro',
            name='Dewey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principale.Dewey'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='InPrestito',
            field=models.BooleanField(choices=[(True, 'si'), (False, 'no')]),
        ),
        migrations.AddField(
            model_name='prestito',
            name='idlibro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principale.Libro'),
        ),
        migrations.AddField(
            model_name='prestito',
            name='idutente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principale.Utente'),
        ),
        migrations.AddField(
            model_name='libriindisuso',
            name='idLibro',
            field=models.ForeignKey(on_delete=True, to='principale.Libro'),
        ),
        migrations.AddField(
            model_name='autorelibro',
            name='Idlibro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principale.Libro'),
        ),
        migrations.AddField(
            model_name='autorelibro',
            name='idAutore',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principale.Autori'),
        ),
        migrations.AddField(
            model_name='libro',
            name='Autore',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='principale.Autori'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='Editore',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='principale.EDITORI'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='IdSede',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='principale.Sede'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='idCollocazione',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='principale.Collocazione'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libro',
            name='idStato',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='principale.Stato'),
            preserve_default=False,
        ),
    ]
