
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
        self._tv.turnOn()
    
    def turnOff(self):
        self._tv.turnOff()
    

    def canalUp(self):
        self._tv.canalUp()
    
    def canalDown(self):
        self._tv.canalDown()
    

    def volumenUp(self):
        self._tv.volumenUp()
    
    def volumenDown(self):
        self._tv.volumenDown()
    
    
    def setCanal(self, canal):
        if self._tv.getEstado() and canal<=120 and canal>=1:
            self._tv.setCanal(canal)