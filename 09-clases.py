class OperasBas:
    #declaracion de propiedades
    #public 
    num1 = 0
    #private
    num2 = 0
    #protect
    res = 0
    
    #declaracion de constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    #declaracion de metodos de clase
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))
        
    def resta(self):
         self.res=self.num1-self.num2
         print("La resta es: {}".format(self.res))
         
def main():
    obj=OperasBas(3,4)
    obj.suma()
    
if __name__ == "__main__":
    main()