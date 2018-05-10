from .models import Chat, User, ChatMember
import time

def createChat(creator,chatType,chatName,users={}):
	currentTime = time.clock()
	try:
		newchat = Chat(chatType__name=chatType,name=chatName)
		newchat.save()
		chatmember.objects.add(ChatMember(user=creator,chat=newchat,isCreator=True))
		for user in users:
			ChatMember.objects(ChatMember(user=user,chat=newchat,isCreator=False))
	except error:
		print('error of creating chat')

