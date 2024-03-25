a = "Hola"
z = "Mundo"
b = False
c = 1.2
d = 10

def suma (n1,n2):
    n3 = n1+n2
    return n3

def resta (n1,n2):
    n3 = n1-n2
    return n3

def multiplicacion (n1,n2):
    n3 = n1*n2
    return n3

def division (n1,n2):
    n3 = n1/n2
    return n3
primer_num = int(input("Digite primer numero"))
segundo_num = int(input("Digite segundo numero"))
resultado = suma (primer_num,segundo_num)

print(resultado)



