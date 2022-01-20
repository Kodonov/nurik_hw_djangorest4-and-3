# Generated by Django 4.0 on 2021-12-21 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tag_review_product_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descption', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main.movie')),
            ],
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Cinema',
        ),
        migrations.RenameModel(
            old_name='Tag',
            new_name='Genres',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.AddField(
            model_name='movie',
            name='cinema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cinema'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='main.Genres'),
        ),
    ]