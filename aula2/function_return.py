# void
def ola():
    print('Olá')

ola()

# funcao retorno
def soma(a, b):
    resultado = a + b
    return a + b

result = soma(5, 5)
print(result)

def mensagem(header, footer):
    header()
    print('Olá você esta no CodeShow ')
    footer()

def header():
    print('### início ###')

def footer():
    print('### fim ###')

mensagem(header= header, footer= footer)