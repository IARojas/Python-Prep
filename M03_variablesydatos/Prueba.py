x=5
while True:
    x-=1
    print(x)
    if x==0:
        break
print("Fin del bucle")


cadena = 'Python'
for letra in cadena:
    if letra == 'P':
        continue
    print(letra)