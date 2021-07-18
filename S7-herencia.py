class persona:
    _siguente = 0
    def __init__(self,nombre="invitado",activo=True):
        self.__codigo = self.siguiente()
        self.__nombre = self.nombreMayuscula(nombre)
        self.activo = activo
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
        self.__nombre - nom
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,cod):
        self.__codigo - cod
        
    def siguiente(self):
        persona._siguiente - persona._siguiente+1
        return persona._siguente
    
    def __nombreMayuscula(self,nomb):
        return nomb.upper()
    
    def mostrar datos(self):
        return "codigo: {} - nombre: {} - activo:  {}",format (Self)

class empleado(persona):
    
    def __init__(self,nom='invitado',act=True,sueldo=400):
        persona.__init__(self,nom,act)
        self.sueldo=sueldo
        
    def mostrar datos(self):
        return Persona.mostrar datos(self)+" - Sueldo: "+str()    