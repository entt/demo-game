# Generated by Django 2.1.6 on 2019-02-13 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20190211_2320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('position_counter', models.IntegerField(default=6)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='color',
            field=models.CharField(default='#ffffff', max_length=25),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='player',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.Game'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('game', 'position')},
        ),
    ]
