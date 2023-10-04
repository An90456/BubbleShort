
if __name__ == '__main__':
    lista=[8,0,-1,9,10,2,4]
    i = 0
    j = 0
    while i < len(lista):
        if j == len(lista)-1:
            j = 0
        if lista[j] > lista[j+1]:
            dato_post=lista[j+1]
            lista[j+1]=lista[j]
            lista[j]= dato_post
            j+=1
            i = 0

        else:
            i+=1
            j+=1
    print(lista)

