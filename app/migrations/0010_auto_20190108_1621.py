# Generated by Django 2.1.5 on 2019-01-08 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190107_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='childRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Launch_Time', models.DateTimeField(auto_now_add=True)),
                ('Edit_Time', models.DateTimeField(auto_now=True)),
                ('Content', models.CharField(max_length=256)),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childRemark', to='app.Article')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myReply', to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='parentRemark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Launch_Time', models.DateTimeField(auto_now_add=True)),
                ('Edit_Time', models.DateTimeField(auto_now=True)),
                ('Content', models.CharField(max_length=256)),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parentRemark', to='app.Article')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myRemark', to='app.User')),
            ],
        ),
        migrations.RemoveField(
            model_name='remark',
            name='Article',
        ),
        migrations.RemoveField(
            model_name='remark',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='remark',
            name='ParentRemark',
        ),
        migrations.DeleteModel(
            name='remark',
        ),
        migrations.AddField(
            model_name='childremark',
            name='ParentRemark',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childRemark', to='app.parentRemark'),
        ),
    ]
