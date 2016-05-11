'''
Created on 10/05/2016

@author: PedrozaSalerno
'''

class Persona():
    
    def __init__(self, nombre, apellido, ci, pin):
        if(type(nombre) is not type("safsdf")):
            exit("El nombre debe ser un string")
        elif(any(not(x.isalpha()) and x!="-" and  not(x.isspace()) for x in nombre)):
            exit("Caracteres invalidos en el nombre.")
        elif(type(apellido) is not type("safsdf")):
            exit("El apellido debe ser un string")
        elif(any(not(x.isalpha()) and x!="-" and  not(x.isspace()) for x in apellido)):
            exit("Caracteres invalidos en el apellido.")
        elif(type(ci) is not type("asd")):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguida de numeros")
        elif(len(ci)<3):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguido de numeros")
        elif(ci[:2] not in ["V-","E-"]):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguido de numeros")
        elif(any(not x.isdigit() for x in ci[2:])):
            exit("La cedula de identidad debe ser un string de la forma V-|E- seguido de numeros")
        elif(type(pin) is not int):
            exit("El pin debe ser un numero entero mayor o igual que cero")
        elif(pin<0):
            exit("El pin debe ser un numero entereo mayor o igual que cero")
            
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
        self.pin = pin