# Generated by Django 2.1.5 on 2019-01-07 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181222_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Depth', models.SmallIntegerField()),
                ('Launch_Time', models.DateTimeField(auto_now_add=True)),
                ('Edit_Time', models.DateTimeField(auto_now=True)),
                ('Content', models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='app.User'),
        ),
        migrations.AddField(
            model_name='remark',
            name='Article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remark', to='app.Article'),
        ),
        migrations.AddField(
            model_name='remark',
            name='Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myRemark', to='app.User'),
        ),
        migrations.AddField(
            model_name='remark',
            name='ParentRemark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childRemark', to='app.remark'),
        ),
    ]