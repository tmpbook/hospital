#coding=utf-8
from django.db import models
  
# Create your models here.
#创建医院表
class Hospital(models.Model):
    prope_Public ='public'
    prope_Private ='private'
    prope_choices = (
        (prope_Public,'公立医院'),
        (prope_Private,'私立医院'),             
    )
    hos_ID = models.CharField(max_length=20)  #医院ID
    hos_name = models.CharField(max_length=50)  #医院名称
    hos_palce = models.CharField(max_length=100)  #医院地址
    hos_profile = models.CharField(max_length=1000)  #医院简介
    hos_rating = models.CharField(max_length=20)  #医院等级
    hos_grade = models.CharField(max_length=20)  #医院评级星数
    type = models.CharField(max_length=20)  #医院类型标志(1表示医院，2表示体检中心)
    hos_prope =models.CharField(max_length=10,choices=prope_choices,default=prope_Public)  #医院性质
      
def hospital(self):
    return self.hos_name
  
  
#创建医生表
class Doctor(models.Model):
    doc_ID = models.CharField(max_length=20)  #医生ID
    hos_ID = models.CharField(max_length=20)  #医院ID
    doc_name = models.CharField(max_length=50)  #医生姓名
    doc_depart = models.CharField(max_length=100)  #医生所属科室
    doc_professional = models.CharField(max_length=100)  #职称
    doc_profile = models.CharField(max_length=500)  #医生简介
    doc_grade = models.CharField(max_length=20)  #医生评级星数
    doc_depart = models.CharField(max_length=20)  #医生所属科室
      
def doctor(self):
    return self.doc_name
  
  
#创建产品表
class Product(models.Model):
    pro_ID = models.CharField(max_length=20)  #产品ID
    doc_ID = models.CharField(max_length=20)  #医生ID
    hos_ID = models.CharField(max_length=20)  #医院ID
    pro_name  = models.CharField(max_length=50)  #产品名称
    pro_detail = models.CharField(max_length=500)  #产品说明
    pro_depart = models.CharField(max_length=200)  #产品所属科室
    pro_standard = models.CharField(max_length=500)  #规格
    pro_time = models.DateField()  #发布时间
    pro_user = models.CharField(max_length=50)  #发布人
      
def product(self):
    return self.pro_name
  
  
#创建订单表
class Order(models.Model):
    order_ID =models.CharField(max_length=20)  #订单ID
    user_ID = models.CharField(max_length=50)  #用户
    pro_ID = models.CharField(max_length=20)  #产品ID
    order_name = models.CharField(max_length=200)  #订单名称
    order_time = models.DateField()  #订单生成时间
    order_batch = models.IntegerField()  #订单批次
      
def order(self):
    return self.order_name
  
  
#创建支付表
class Payment(models.Model):
    order_ID =models.CharField(max_length=20)  #订单ID
    pay_ID  = models.CharField(max_length=20)  #支付ID
    pay_money = models.IntegerField() #支付金额
    pay_time = models.DateField()  #支付时间
    pay_mark = models.CharField(max_length=10)  #付费成败标志
      
def payment(self):
    return self.pay_title
  
  
  
#创建评价
class Comments(models.Model):
    com_ID = models.CharField(max_length=20)  #评论ID 
    user_ID = models.CharField(max_length=20)  #用户ID
    pro_ID = models.CharField(max_length=20)  #产品ID
    com_content  = models.IntegerField()  #评论内容
    com_time = models.DateField()  #评论时间
    com_status = models.DateField()  #审核状态
      
def comments(self):
    return self.com_content
  
  
  
#热点资讯表
class News(models.Model):
    news_ID = models.CharField(max_length=20)  #资讯ID
    user_ID =models.CharField(max_length=20)   #用户ID
    news_title  = models.IntegerField()  #资讯标题
    news_image = models.CharField(max_length=50)  #资讯图标路径
    news_time = models.DateField()   #发布时间
    news_name = models.DateField()  #发布人
      
def news(self):
    return self.news_title
  
  
     
# class Student(models.Model):
#     FRESHMAN = 'FR'
#     SOPHOMORE = 'SO'
#     JUNIOR = 'JR'
#     SENIOR = 'SR'
#     YEAR_IN_SCHOOL_CHOICES = (
#         (FRESHMAN, 'Freshman'),
#         (SOPHOMORE, 'Sophomore'),
#         (JUNIOR, 'Junior'),
#         (SENIOR, 'Senior'),
#     )
#     year_in_school = models.CharField(max_length=2,
#                                       choices=YEAR_IN_SCHOOL_CHOICES,
#                                       default=FRESHMAN)
#  
#     def is_upperclass(self):
#         return self.year_in_school in (self.JUNIOR, self.SENIOR)     