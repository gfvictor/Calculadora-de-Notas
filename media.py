calcular = True


def nota():
    ava = []
    prova = []
    x = 0
    while True:
        ava = input("---\nQual foi a nota no AVA?\n")
        try:
            float(ava)
            break
        except ValueError:
            print("---\nO valor deve ser um numero inteiro ou real!\n")
    while True:
        prova = input("---\nQual foi a nota da prova?\n")
        try:
            float(prova)
            break
        except ValueError:
            print("---\nO valor deve ser um numero inteiro ou real!\n")
    media = (9 * float(prova) + 1 * float(ava)) / 10
    if media >= 7:
        print(f"---\nSua média é ( {media} )! Aprovado!")
    else:
        while (media + x) / 2 < 5:
            x += 1
        print(f"---\nAinda precisa tirar ( {x} ) no Exame...")


def calc():
    while calcular == True:
        nota()
        while input("---\nDeseja continuar?\n")[0].lower() == "s":
            nota()
        break


calc()
