""""
articulo
cliente
venta
ventadet
"""
class Articulo:
    def __init__(self,cod,des,pre,stoc):
        self.codigo=cod
        self.descripcion = des
        self.precio=pre
        self.stock=stoc





class ventaDetalle:
    def __init__(self,pro,pre,cant):
        self.producto=pro
        self.precio=pre
        self.cantidad=cant
