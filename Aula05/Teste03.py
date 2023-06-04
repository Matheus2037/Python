lista = []
rep = True
n = 5

while(rep == True):

    nr = int(input("Digite um número: "))
    lista.append(nr)
    if(len(lista) > n):
        stop = int(input("Deseja parar de adicionar? 1-Sim: "))
        if(stop == 1):
            rep = False
        else: 
            n += 5

lista.sort()    
print(lista)

lista.sort(reverse = True)
print(lista)   