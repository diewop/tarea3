'''
Created on 10/05/2016

@author: PedrozaSalerno
'''
from datetime import datetime

class Persona():
    
    def __init__(self, nombre, apellido, ci, pin):
        if(type(nombre) is not str):
            exit("El nombre debe ser un string")
        elif(any(not(x.isalpha()) and x!="-" and  not(x.isspace()) for x in nombre)):
            exit("Caracteres invalidos en el nombre.")
        elif(type(apellido) is not str):
            exit("El apellido debe ser un string")
        elif(any(not(x.isalpha()) and x!="-" and  not(x.isspace()) for x in apellido)):
            exit("Caracteres invalidos en el apellido.")
        elif(type(ci) is not str):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguida de numeros")
        elif(len(ci)<3):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguido de numeros")
        elif(ci[:2] not in ["V-","E-"]):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguido de numeros")
        elif(any(not x.isdigit() for x in ci[2:])):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguido de numeros")
        elif(type(pin) is not str):
            exit("El pin debe ser un numero entero mayor o igual que cero")
        elif(any(not x.isdigit() for x in pin)):
            exit("El pin debe ser un numero entero mayor o igual que cero")
        
        
            
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.pin = pin
        

class Registro():
    
    def __init__(self,monto,fecha,identificador):
        try:
            self.monto = float(monto)
            assert(self.monto>0)
        except:
            exit("El monto no es válidentificadoro, debe ser un número mayor que cero")
    
        if(type(fecha) is not datetime):
            exit("La fecha debe ser del tipo datetime")
        
        self.fecha=fecha
        self.identificador=identificador


class BilleteraElectronica():
    def __init__(self,identificador,dueño):
        if(type(dueño) is not Persona):
            exit("El dueño no es del tipo Persona")
            
        self.dueño=dueño
        self.recargas=[]
        self.consumos=[]
        self.balance=0
        self.identificador=identificador
    
    def saldo(self):
        return self.balance
    
    def consumir(self,registro):
        if(type(registro) is not Registro):
            print("No es un registro")
            return "No es un registro"
        else:
            if(self.saldo()>=registro.monto):
                self.consumos.append(registro)
                self.balance -= registro.monto
                print("Consumo realizado")
                return "Consumo realizado"
            else:
                print("No tiene suficiente saldo")
                return "No tiene suficiente saldo"
    
    def recargar(self,registro):
        if(type(registro) is not Registro):
            print("No es un registro")
            return "No es un registro"
        else:
            self.recargas.append(registro)
            self.balance += registro.monto
            print("Recarga realizada")
            return "Recarga realizada"
            

