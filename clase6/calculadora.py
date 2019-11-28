class Operation():
    def __init__(self,_parameters=[]):
        self.params=_parameters

    def execute(self):
        print("Hola, prueba calculadora")

class Suma(Operation):
    def execute(self):
        return self.params[0]+self.params[1]

class Resta(Operation):
    def execute(self):
        return self.params[0]-self.params[1]

class Multiplicacion(Operation):
    def execute(self):
        return self.params[0]*self.params[1]

class Division(Operation):
    def execute(self):
        if self.params[1]==0:
            print("---valor no válido---")
        else:
            return self.params[0]/self.params[1]


class Fibonacci(Operation):
    def __init__(self,_parameters=[]):
        super().__init__(_parameters=_parameters)
    
    def execute(self):
        n=self.params[0]
        if n<0:
            print("invalido")
        elif n==0:
            return 0
        elif n==1:
            return 1
        else:
            fn_1=Fibonacci([n-1])
            fn_2=Fibonacci([n-2])
            result=fn_1.execute()+fn_2.execute()
            return result


class Menu:
    def desplegar_menu(self):
        print("Introduzca la opcion deseada: ")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Fibonacci")
        print("6) Salir")

    def pedir_opcion(self):
        opcion_seleccionada=int(input())
        
    def validar_opcion(self,_opcion):    
        if _opcion<=0:
            self.pedir_opcion()
        elif _opcion<=4:
            p1=int(input())
            p2=int(input())
        elif _opcion==5:
            p1=int(input())
        elif _opcion==6:
            return None
        else:
            print("Opcion no valida")
            self.pedir_opcion()
    
    def executar_operation(self):
        pass

m1=Menu()
m1.desplegar_menu()
opcion=m1.pedir_opcion
m1.validar_opcion(opcion)
mi.pedir_parametros()
m1.ejecutar_operacion()
