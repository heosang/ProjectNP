# Generated by Django 3.1 on 2020-09-03 13:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200903_2214'),
        ('myside', '0002_auto_20200903_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='브랜드명')),
                ('img_url', models.URLField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '댓글', 'verbose_name_plural': '댓글'},
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.TextField(default=0, verbose_name='내용'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='등록날짜'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='img_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myside.product', verbose_name='제품명'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='사용자'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like_product',
            name='bad',
            field=models.IntegerField(default=0, verbose_name='싫어요'),
        ),
        migrations.AddField(
            model_name='like_product',
            name='good',
            field=models.IntegerField(default=0, verbose_name='좋아요'),
        ),
        migrations.AddField(
            model_name='like_product',
            name='product_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myside.product', verbose_name='제품명'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='img_url',
            field=models.URLField(blank=True, verbose_name='이미지주소'),
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comment',
        ),
        migrations.CreateModel(
            name='Recomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='대댓글내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myside.comment', verbose_name='댓글')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='사용자')),
            ],
            options={
                'verbose_name': '대댓글',
                'verbose_name_plural': '대댓글',
                'db_table': 'recomment',
            },
        ),
        migrations.CreateModel(
            name='Product_has_brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myside.brand', verbose_name='브랜드명')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myside.product', verbose_name='제품명')),
            ],
        ),
        migrations.CreateModel(
            name='Like_recomment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.IntegerField(default=0, verbose_name='좋아요')),
                ('bad', models.IntegerField(default=0, verbose_name='싫어요')),
                ('recomment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myside.recomment')),
            ],
        ),
        migrations.CreateModel(
            name='Like_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good', models.IntegerField(default=0, verbose_name='좋아요')),
                ('bad', models.IntegerField(default=0, verbose_name='싫어요')),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myside.comment')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brands',
            field=models.ManyToManyField(through='myside.Product_has_brand', to='myside.Brand'),
        ),
    ]
