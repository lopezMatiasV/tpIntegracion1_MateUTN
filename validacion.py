num = input("Ingrese un número: ")
for i in range(len(num)):
    print(num[i])
    if num[i] == "1" or num[i] == "0":
        print("ok")
    else:
        print("Tu número no es un binario!!")