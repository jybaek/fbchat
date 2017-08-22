# encoding=utf-8

from fbchat import Client
from fbchat.models import *

client = Client('id', 'password') # XXX.

""" self message
client.sendMessage('hi me!', thread_id=client.uid)
exit(255)
"""

friends = client.searchForUsers('friend_name')[0] # XXX.

msg = 'jobs message' # XXX.

client.sendMessage(msg, thread_id=friends.uid, thread_type=ThreadType.USER)
client.logout()
