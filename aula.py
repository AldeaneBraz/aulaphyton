def boasVindas(nome, atividade):
    print("Olá{}, você gosta de {} estudar".format(nome,atividade))


if __name__ == "__main__":
    nome = input("Qual o seu nome?:")
    atividade = input("você gosta de estudar?:")
    boasVindas(nome, atividade)
