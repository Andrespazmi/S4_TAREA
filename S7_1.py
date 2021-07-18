class ordenar:
    def __init__(self,lista):
        self.lista=lista
    def borbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i] > self.lista[j]:
                    aux = self.lista[i]
                    self.lista[i]=self.lista[j]
                    self.lista[j]=aux
    def insertar(self,valor):
        self.borbuja()
        auxlista=[]
        for pos,ele in enumerate(self.lista):
            if valor>ele:
                auxlista.append(valor)
                break
        auxlista = self.lista [0:pos]  + auxlista + self.pos
        return auxlista     
ord1 = ordenar([10,15,20,70,80])
#               0 1 2 3 4
print(ord1.insertar(50))
#ord1.borbuja
#print(ord1.lista)

