# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class GollaPicture(models.Model):
    id = models.BigAutoField(primary_key=True)
    img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'golla_picture'


class Goods(models.Model):
    goods_code = models.AutoField(db_column='Goods_Code', primary_key=True)  # Field name made lowercase.
    godds_name = models.CharField(db_column='Godds_Name', max_length=50)  # Field name made lowercase.
    goods_price = models.IntegerField(db_column='Goods_Price', blank=True, null=True)  # Field name made lowercase.
    goods_description = models.CharField(db_column='Goods_Description', max_length=255)  # Field name made lowercase.
    goods_category = models.IntegerField(db_column='Goods_Category')  # Field name made lowercase.
    goods_img_path = models.CharField(db_column='Goods_Img_Path', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goods'


class Goodsdetail(models.Model):
    detail_code = models.AutoField(db_column='Detail_Code', primary_key=True)  # Field name made lowercase.
    goods_code = models.ForeignKey(Goods, models.DO_NOTHING, db_column='Goods_Code')  # Field name made lowercase.
    volume = models.IntegerField()
    calories = models.IntegerField(db_column='Calories')  # Field name made lowercase.
    fat = models.IntegerField(db_column='Fat')  # Field name made lowercase.
    carbohydrates = models.IntegerField(db_column='Carbohydrates')  # Field name made lowercase.
    protein = models.IntegerField(db_column='Protein')  # Field name made lowercase.
    sugar = models.IntegerField(db_column='Sugar')  # Field name made lowercase.
    fiber = models.IntegerField(db_column='Fiber')  # Field name made lowercase.
    allergies = models.CharField(db_column='Allergies', max_length=19)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodsDetail'


class Grade(models.Model):
    grade_code = models.AutoField(db_column='Grade_Code', primary_key=True)  # Field name made lowercase.
    grade_name = models.CharField(db_column='Grade_Name', max_length=20)  # Field name made lowercase.
    point_rate = models.IntegerField(db_column='point_Rate')  # Field name made lowercase.
    base_amount = models.IntegerField(db_column='Base_Amount')  # Field name made lowercase.
    grade_img_path = models.CharField(db_column='Grade_Img_Path', max_length=1000)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'grade'


class Member(models.Model):
    member_code = models.AutoField(db_column='member_Code', primary_key=True)  # Field name made lowercase.
    member_name = models.CharField(db_column='member_Name', max_length=20)  # Field name made lowercase.
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    grade = models.IntegerField()
    member_point = models.IntegerField()
    joindate = models.DateTimeField(db_column='joinDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class Payment(models.Model):
    paymentcode = models.AutoField(db_column='paymentCode', primary_key=True)  # Field name made lowercase.
    membercode = models.ForeignKey(Member, models.DO_NOTHING, db_column='memberCode')  # Field name made lowercase.
    storecode = models.IntegerField(db_column='storeCode')  # Field name made lowercase.
    paymentprice = models.IntegerField(db_column='paymentPrice')  # Field name made lowercase.
    paymentdate = models.DateTimeField(db_column='paymentDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Store(models.Model):
    storecode = models.AutoField(db_column='storeCode', primary_key=True)  # Field name made lowercase.
    storename = models.CharField(db_column='storeName', max_length=20)  # Field name made lowercase.
    store_address = models.CharField(db_column='Store_Address', max_length=255)  # Field name made lowercase.
    stroe_phone = models.CharField(db_column='Stroe_Phone', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'
