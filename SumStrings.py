x = input()
listax = x.split()
quantidade_a_removerX=len(listax)
y = input()
listay = y.split()
quantidade_a_removerY=len(listay)

sequencias = ['11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '36', '37', '38', '39', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '52', '53', '54', '55', '56', '57', '58', '59', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '72', '73', '74', '75', '76', '77', '78', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']

for elemento in listax:
    if elemento in sequencias:
        print('Erro em uma ou mais sequência de entrada de dados')
        exit()

for elementoy in listay:
    if elementoy in sequencias:
        print('Erro em uma ou mais sequência de entrada de dados')
        exit()


resto = 0
soma = []

firstsequence = list(map(int, x.split()))
secondsequence = list(map(int, y.split()))

sapo = firstsequence[::-1]
sapinho = secondsequence[::-1]


for i, j in zip(sapo, sapinho):

    zapzap = i + j + resto

    if zapzap > 9:
        zapzap = zapzap - 10
        resto = 1
    else:
        resto = 0

    soma.append(zapzap)

if resto == 1:
    soma.append(1)

soma = soma[::-1]

sapao = ' '.join(map(str, soma))

if len(x) < len(y):

    for w in range(quantidade_a_removerX):
        listay.pop()
    listay_inteiros = [int(o) for o in listay]
    listay_com_espacos = ' '.join(map(str, listay_inteiros))
    print(f'{listay_com_espacos} {sapao}')

elif len(y) < len(x):

    for z in range(quantidade_a_removerY):
        listax.pop()
    listax_inteiros = [int(o) for o in listax]
    listax_com_espacos = ' '.join(map(str, listax_inteiros))
    print(f'{listax_com_espacos} {sapao}')
else:
    print(sapao)