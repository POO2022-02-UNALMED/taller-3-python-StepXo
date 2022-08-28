
class Control():
    def __init__(self):
        self.tv = None

    def enlazar(self,tv):
        self.tv = tv               #attributo -tv- apuntar a objeto -tv-
        self.tv.setControl(self)   #el atributo -tv.control- apunte a -este.control-
    

    def getTv(self):
        return self.tv
    
    def setTv(self, tv):
        self.tv = tv
    

    def turnOn(self):
        self.tv.turnOn(self)
    
    def turnOff(self):
        self.tv.turnOff(self)
    

    def canalUp(self):
        self.tv.canalUp(self)
    
    def canalDown(self):
        self.tv.canalDown(self)
    

    def volumenUp(self):
        self.tv.volumenUp(self)
    
    def volumenDown(self):
        self.tv.volumenDown(self)
    
    
    def setCanal(self, canal):
        if (self.tv.getEstado(self) and canal<=120 and canal>=1):
            self.tv.setCanal(canal)