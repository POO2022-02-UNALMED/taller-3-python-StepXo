
class TV():
    numTV=0
    def __init__( self,marca,estado):
        self.marca=marca
        self.canal=1
        self.precio=500
        self.estado=estado
        self.volumen=1
        self.control=None

    #Setters
    def setMarca (self, marca):
        self.marca = marca

    def setControl (self, control):
        self.control = control

    def setPrecio (self, precio):
        self.precio = precio

    def setVolumen (self, volumen):
        if self.estado and volumen<=7 and volumen>=0:
            self.volumen = volumen


    def setCanal (self, canal):
        if self.estado and canal<=120 and canal>=1:
            self.canal = canal

    @classmethod
    def setNumTV (cls,numTV):
        cls._numTV = numTV


    #Getters
    def  getMarca(self):
        return self._marca

    def  getControl(self):
        return self._control

    def  getPrecio(self):
        return self._precio

    def  getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal

    def  getEstado(self):
        return self._estado

    @classmethod
    def  getNumTV(cls):
        return cls._numTV


    #otros metodos
    def turnOn(self):
        self.estado =True
                               #una cosa rara para el "setEstado"
    def turnOff(self):
        self.estado =False


    def canalUp(self):
        if self.estado and self.canal<120:
            self.canal+=1


    def canalDown(self):
        if self.estado and self.canal>1:
            self.canal-=1



    def volumenUp(self):
        if self.estado and self.volumen<7:
            self.volumen+=1


    def volumenDown(self):
        if self.estado and self.volumen>0:
            self.volumen-=1


