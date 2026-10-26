

sair = ""

while sair != "exit":

    numero1 = float(input("digite um numero: "))
    numero2 = float(input("digite outro numero: "))

    print("ESCOLHA A FORMULA DA SOMA")
    print("1 = mais")
    print("2 = menos")
    print("3 = vezes")
    print("4 = dividido")
    print("5 = resto da divizao")

    opçao = [ 1 , 2 , 3 , 4 , 5 , ]

    soma = int((input("digite o numero da opçao: ")))

    if soma not in opçao:
        print("SO ESCOLHA UM NUMERO DA SOMA")

    elif soma in opçao and soma == 1:
        valor = numero1 + numero2
        print(f" o numero {numero1} + o nuemro {numero2} e igual a {valor}")

    elif soma in opçao and soma == 2:
        valor = numero1 - numero2
        print(f" o numero {numero1} - o nuemro {numero2} e igual a {valor}")

    elif soma in opçao and soma == 3:
        valor = numero1 * numero2
        print(f" o numero {numero1} x o nuemro {numero2} e igual a {valor}")

    elif soma in opçao and soma == 4:
        valor = numero1 / numero2
        print(f" o numero {numero1} // o nuemro {numero2} e igual a {valor}")

    elif soma in opçao and soma == 5:
        valor = numero1 % numero2
        print(f" o numero {numero1} % o nuemro {numero2} e igual a {valor}")

    sair = input("digite (exit) para sair ou (aperte (enter) para continuar:  )")
