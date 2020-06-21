from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(5)
while True:
    client, addr = s.accept()
    data = client.recv(500)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    if data.decode('utf-8') == 'presence':
        msg = 'Вы онлайн'
        client.send(msg.encode('utf-8'))
        client.close()
