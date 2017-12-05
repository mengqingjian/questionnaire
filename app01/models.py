from django.db import models

# Create your models here.


class UserInfo(models.Model):
    """
    员工表
    """
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    def __str__(self):
        return self.username
class ClassRoom(models.Model):
    """
    班级表
    """
    title=models.CharField(verbose_name="班级名",max_length=32)
    def __str__(self):
        return self.title
class Student(models.Model):
    """
    学生表
    """
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    cls=models.ForeignKey(verbose_name="学生所在的班级",to="ClassRoom")
    def __str__(self):
        return self.username
class Questionnaire(models.Model):
    """
    问卷表
    """
    title=models.CharField(verbose_name="问卷名",max_length=32)
    cls=models.ForeignKey(verbose_name="班级中的所有问卷",to="ClassRoom")
    creator=models.ForeignKey(verbose_name="班级创建者",to="UserInfo")
    def __str__(self):
        return self.title
class Question(models.Model):
    """
    问题表
    """
    caption =models.CharField(max_length=32)
    question_type=(
        (1,"打分"),
        (2, "单选"),
        (3, "评价")
    )
    type=models.IntegerField(choices=question_type)
class Option(models.Model):
    """
    单选题的选项表
    """
    name=models.CharField(verbose_name="选项名称",max_length=32)
    score=models.IntegerField(verbose_name="选项对象的分值")
    question=models.ForeignKey(verbose_name="问题表中所有的单选",to="Question")

    def __str__(self):
        return self.name
class Answer(models.Model):
    """
    回答表
    """
    student=models.ForeignKey(verbose_name="所有学生回答的问题",to="Student")
    question=models.ForeignKey(verbose_name="所有回答的问题",to="Question")
    option = models.ForeignKey(to="Option",null=True,blank=True)
    val = models.IntegerField(null=True,blank=True)
    content = models.CharField(max_length=255,null=True,blank=True)





