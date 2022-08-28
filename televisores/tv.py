
class TV():
    _numTV=0
    def __init__( self,marca,estado):
        self._marca=marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None
        TV._numTV+=1

    #Setters
    def setMarca (self, marca):
        self.marca = marca

    def setControl (self, control):
        self.control = control

    def setPrecio (self, precio):
        self.precio = precio

    def setVolumen (self, volumen):
        if self._estado and volumen<=7 and volumen>=0:
            self.volumen = volumen


    def setCanal (self, canal):
        if self._estado and canal<=120 and canal>=1:
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

    def  get_Estado(self):
        return self._estado

    @classmethod
    def  getNumTV(cls):
        return cls._numTV


    #otros metodos
    def turnOn(self):
        self._estado =True
                               #una cosa rara para el "set_Estado"
    def turnOff(self):
        self._estado =False


    def canalUp(self):
        if self._estado and self._canal<120:
            self._canal+=1


    def canalDown(self):
        if self._estado and self._canal>1:
            self._canal-=1



    def volumenUp(self):
        if self._estado and self._volumen<7:
            self._volumen+=1


    def volumenDown(self):
        if self._estado and self._volumen>0:
            self._volumen-=1


