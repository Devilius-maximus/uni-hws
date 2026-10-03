class something:

    def __init__(self, Base, value):
        self._Base = Base
        self.__value= value #dota underscore ==> name mangeling , seda zadan ==> b._something__value 
        # 1 under score ==> nonpublic, b._base
        #a._base wrong, a.set_base (ye tabe joda bayad besazi)

    def set_base(self, base):
        a._Base = base 
        
        pass

    def show_base(self):
        print(f"baso: {self._base}")

    def show_value (self):
        print(f"value: {self._value}")



a = something('bin' , '0b10110101001')

b = something("hex" , "0x2aAF")





