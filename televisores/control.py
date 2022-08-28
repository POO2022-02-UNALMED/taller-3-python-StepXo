
class Control():
    def __init__(self):
        self._tv = None

    def enlazar(self,_tv):
        self._tv = _tv               #attributo -tv- apuntar a objeto -tv-
        self._tv.setControl(self)   #el atributo -tv.control- apunte a -este.control-
    

    def getTv(self):
        return self._tv
    
    def setTv(self, tv):
        self._tv = tv
    

    def turnOn(self):
        self._tv.turnOn(self)
    
    def turnOff(self):
        self._tv.turnOff(self)
    

    def canalUp(self):
        self._tv.canalUp(self)
    
    def canalDown(self):
        self._tv.canalDown(self)
    

    def volumenUp(self):
        self._tv.volumenUp(self)
    
    def volumenDown(self):
        self._tv.volumenDown(self)
    
    
    def setCanal(self, canal):
        if self._tv.getEstado(self) and canal<=120 and canal>=1:
            self._tv.setCanal(self, canal)