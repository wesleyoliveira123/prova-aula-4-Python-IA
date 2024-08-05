def media(num1, num2, num3):
    soma = num1 + num2 + num3
    media_aritmetica = soma / 3
    return media_aritmetica

num1=float(input('digite o numero 1 :'))
num2=float(input('digite o numero 2 :'))
num3=float(input('digite o numero 3 :'))
resultado=media(num1, num2, num3)
print(f'a media deu: {resultado}')