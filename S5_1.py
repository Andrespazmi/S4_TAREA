class operaciones: 
    def __init__(self,num1,num2):
        self.numero1=num1
        self.numero2=num2
    
    def suma (self):
        suma=self.numero1 + self.numero2
        return suma

    def  resta (self):
        return self.numero1 - self.numero2
        


    def multiplicacion (self):
        return self.numero1 * self.numero2
        

    def divicion (self):
        if self.numero2 !=0: return self.numero1 / self.numero2
        return 0

    def divicionEntera (self):
        if self.numero2 !=0: return self.numero1 // self.numero2
        return 0

    def residuo (self):
        print (self.numero1 % self.numero2)
    
    def exponente (self):
        print (self.numero1 ** self.numero2)

    def mostrar (self):
        print("operando1={},operando2={}".fortmat(self.numero1,self.numero2))
        
print("Menu Operaciones Matematicas")
print ("1) Suma\n2) Resta\n3) Multiplicacion\n4) Divicion\n5) Divicion Entera\n6) Reciduo\n7) Exponente\n8) SALIR")
opc='0'
while opc !='8':
    opc= input("Elija opcion[1....8]")
    num1= int(input("ingrese numero1: "))
    num2= int(input("ingrese numero2: "))
    ope = operaciones(num1,num2)
    if opc =='1':
        print("{}+{}={}".format(ope.numero1,ope.numero2,ope.suma()))
    elif opc == '2':  
        print("{}-{}={}".format(ope.numero1,ope.numero2,ope.resta()))  
    elif opc == '3':
        print("{}*{}={}".format(ope.numero1,ope.numero2,ope.multiplicacion()))
    elif opc == '4':
        print("{}/{}={}".format(ope.numero1,ope.numero2,ope.divicion()))
        print(ope.divicion)
    elif opc == '5':
        print("{}//{}={}".format(ope.numero1,ope.numero2,ope.divicionEntera()))
    elif opc == '6':
        print("{}%{}={}".format(ope.numero1,ope.numero2,ope.reciduo()))
        print(ope.reciduo)
    elif opc == '7':
        print("{}**{}={}".format(ope.numero1,ope.numero2,ope.exponente()))
      
print ("Usted salio del programa muchas gracias")
