# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score_one', models.IntegerField()),
                ('score_two', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='game',
            name='player_one',
            field=models.ForeignKey(related_name=b'games_as_p1', to='pingpong.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='player_two',
            field=models.ForeignKey(related_name=b'games_as_p2', to='pingpong.Player'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(related_name=b'games_as_winner', to='pingpong.Player'),
            preserve_default=True,
        ),
    ]
