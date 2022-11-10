
#Objeto
class Fraction():
    #Atributos
    numerator = 0
    denominator = 1 
    #Métodos
    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def imprimir(self): #Para imprimir una clase fraccion
        print(self.numerator,"/",self.denominator)
    
    def multiply(self,b): #Para multiplicar fracciones
        result_numerator = self.numerator *b.numerator
        result_denominator = self.denominator *b.denominator
        r = Fraction(result_numerator,result_denominator)
        r.imprimir()
        
    def sum(self,b): #Para sumar fracciones
        result_numerator = (self.numerator*b.numerator)+(b.numerator*self.denominator)
        result_denominator = (self.denominator *b.denominator)
        r = Fraction(result_numerator,result_denominator)
        r.imprimir()
        
    def minus(self,b): #Para restar fracciones
        result_numerator = (self.numerator *b.numerator)-(b.numerator*self.denominator)
        result_denominator = (self.denominator *b.denominator)
        r = Fraction(result_numerator,result_denominator)
        r.imprimir()
    def divide(self,b): #Para dividir fracciones
        result_numerator = (self.numerator *b.denominator)
        result_denominator = (self.denominator *b.numerator)
        r = Fraction(result_numerator,result_denominator)
        r.imprimir()
        
a=Fraction (int(input("Ingrese numerador de a: ")),int(input("Ingrese denominador de a: ")))
a.imprimir()
b=Fraction (int(input("Ingrese numerador de b: ")),int(input("Ingrese denominador de b: ")))
b.imprimir()
choice = int(input("Ingrese la operación a realizar (1 para multiplicar, 2 para sumar, 3 para restar y 4 para dividir): "))

if choice == 1:
  a.multiply(b)
elif choice == 2:
  a.sum(b)
elif choice == 3:
  a.minus(b)
else:
  a.divide(b)
