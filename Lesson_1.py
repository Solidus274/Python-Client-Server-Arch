import subprocess

print('Задание 1.')

alpha = 'разработка'
beta = 'сокет'
gamma = 'декоратор'

print(type(alpha))
print(type(beta))
print(type(gamma))

alpha = '\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
beta = '\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
gamma = '\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'

print(type(alpha))
print(type(beta))
print(type(gamma))

print('Задание 2.')

delta = b'class'
epsilon = b'function'
zeta = b'method'

print(type(delta))
print(len(delta))
print(delta)
print(type(epsilon))
print(len(epsilon))
print(epsilon)
print(type(zeta))
print(len(zeta))
print(zeta)

print('Задание 3.')

theta = b'attribute'
# iota = b'класс'
# В строке iota есть символ, не относящийся к ASCII
# kappa = b'функция'
# В строке kappa есть символ, не относящийся к ASCII
lambda_ = b'type'

print(theta)
print(lambda_)

print('Задание 4.')

mu = 'разработка'
nu = 'администрирование'
xi = 'protocol'
omicron = 'standard'

mu_enc = str.encode(mu, encoding='utf-8')
nu_enc = str.encode(nu, encoding='utf-8')
xi_enc = str.encode(xi, encoding='utf-8')
omicron_enc = str.encode(omicron, encoding='utf-8')

print(mu_enc)
print(nu_enc)
print(xi_enc)
print(omicron_enc)

mu_enc = bytes.decode(mu_enc, encoding='utf-8')
nu_enc = bytes.decode(nu_enc, encoding='utf-8')
xi_enc = bytes.decode(xi_enc, encoding='utf-8')
omicron_enc = bytes.decode(omicron_enc, encoding='utf-8')

print(mu_enc)
print(nu_enc)
print(xi_enc)
print(omicron_enc)

print('Задание 5.')

arg_1 = ['ping', 'yandex.ru']
arg_2 = ['ping', 'youtube.com']

subproc_ping_1 = subprocess.Popen(arg_1, stdout=subprocess.PIPE)
subproc_ping_2 = subprocess.Popen(arg_2, stdout=subprocess.PIPE)

for line_1 in subproc_ping_1.stdout:
    print(line_1.decode('cp866'))

for line_2 in subproc_ping_2.stdout:
    print(line_2.decode('cp866'))

print('Задание 6.')

f_n = open("test_file.txt", "w")

f_n.write("сетевое программирование \n")

f_n.write("сокет \n")

f_n.write("декоратор \n")

print('\n')
print(f_n)

f_n.close()

with open('test_file.txt') as f_n:
    print('\n')
    for el_str in f_n:
        print(el_str)


