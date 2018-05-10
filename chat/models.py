from django.db import models
from django import forms
from django.core.files.storage import FileSystemStorage


class Role(models.Model):
    name = models.CharField(max_length=30)

class File(models.Model):
	path = models.CharField(max_length=100)
	fileType = models.CharField(max_length=10)

class User(models.Model):
	login = models.CharField(primary_key=True,max_length=20)
	role = models.ForeignKey(Role,on_delete=models.PROTECT)
	password = models.CharField(max_length=20)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	email = models.EmailField(null=False)
	photo = models.ImageField(upload_to="photos")
	regDate = models.DateTimeField(auto_now_add=True)

class ChatType(models.Model):
    name = models.CharField(max_length=20,primary_key=True)

class Chat(models.Model):
	name = models.CharField(max_length=25)
	type = models.ForeignKey(ChatType,on_delete=models.PROTECT)
	createTime = models.DateTimeField(auto_now_add=True)

class ChatMember(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
	chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
	isCreator = models.BooleanField(default=False)

class Task(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=2048)
	allocTime = models.DateTimeField(auto_now_add=True)
	duration = models.DurationField()
	executors = models.ManyToManyField(User)

class File(models.Model):
	name = models.CharField(max_length=50)
	file = models.FileField(upload_to="embeddings")

class Message(models.Model):
    text = models.CharField(max_length=2048)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    createTime = models.DateTimeField(auto_now_add=True)
    embeddings = models.ManyToManyField(File)
