from socket import *
import json

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 7777))

with open('presence.json', 'r', encoding='utf-8') as message:
    message_content = message.read()
    msg = json.loads(message_content).get("action").encode('utf-8')
s.send(msg)

data = s.recv(500)
print('Сообщение от сервера: ', data.decode('utf-8'), ', длиной ', len(data), ' байт')
s.close()