


    
    #Sabendo que a area de um triangulo é igual a 
   # base * altura /2
    #crie uma função para que receba a base e a altura
    #e retorne a area

def calcula_Area(base,altura):
    return altura/2*2
    
if __name__=="__main__":
    base= int(input("Digite sua base"))
    altura= int(input("Digite sua altura"))
    area=calcula_Area(base,altura)
    print("A area do triangulo é {area:.2f}")