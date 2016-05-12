'''
Created on 10/05/2016

@author: PedrozaSalerno
'''
import unittest
import sys
from datetime import datetime

from BilleteraElectronica import *



class PruebaPersona(unittest.TestCase):

    #Caso interior
    def testDatosValidos(self):
        X = Persona("Chu-li-ñon","López", "V-24900767","4679")
        self.assertEqual(X.nombre, "Chu-li-ñon", "Nombre aceptado")
        self.assertEqual(X.apellido, "López", "Apellido aceptado")
        self.assertEqual(X.ci, "V-24900767", "Cedula aceptada")
        self.assertEqual(X.pin, "4679", "PIN aceptado")
    
    #Caso Inválidos
    def testNombreNumero(self):
        with self.assertRaises(SystemExit):
            Persona(1232,"Salerno","V-24900767","4679")
    
    #Caso Malicioso      
    def testNombreStringConNumeros(self):
        with self.assertRaises(SystemExit):
            Persona("Maur1cio","Salerno","V-24900767","4679")
    
    #Caso Malicioso
    def testNombreCaracteresInvalidos(self):
        with self.assertRaises(SystemExit):
            Persona("Ma/uri=ci*","Salerno","V-24900767","4679")
    
    #Caso Frontera      
    def testNombreVacio(self):
        with self.assertRaises(SystemExit):
            Persona(None,"Salerno","V-24900767","4679")
    
    #Caso Inválidos
    def testApellidoNumero(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio",1234,"V-24900767","4679")
    
    #Caso Malicioso        
    def testApellidoStringConNumeros(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Sal3rno","V-24900767","4679")
    
    #Caso Malicioso
    def testApellidoCaracteresInvalidos(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Ma/uri=ci*","V-24900767","4679")
    
    #Caso Frontera
    def testApellidoVacio(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio",None,"V-24900767","4679")
    
    #Caso Inválidos        
    def testCedulaMalformada(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-249E077","4679")
    
    #Caso Frontera
    def testCedulaVacia(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno",None,"4679") 
    
    #Casos Inválidos        
    def testPINEntero(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",155)
    
    #Casos Inválidos 
    def testPINConNumeroNegativo(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077","-4679")
    
    #Casos Inválidos         
    def testPINSonLetras(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077","AbCd")
    
    #Casos Inválidos 
    def testPINEsFlotante(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077","46.21")
    
    #Casos Frontera
    def testPINVacio(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",None)
    
    #Caso Interior
    def testPINEsCero(self):
        x=Persona("Mauricio","Salerno","V-2499077","0")
        self.assertEqual(x.pin, "0", "Pin Es cero")

    #Caso Interior/Malicia
    def testPINCerosALaIzquierda(self):
        x=Persona("Mauricio","Salerno","V-2499077","0001")
        self.assertNotEqual(x.pin, "1", "PIN: 0001 != 1")
        


class PruebaRegistro(unittest.TestCase):
    #Caso Interior
    def testRegistroValido(self):
        fecha = datetime(2012,6,30)
        x = Registro(200, fecha, 50)
        self.assertEqual(x.monto, 200, "Se guardó el monto")
        self.assertEqual(x.fecha, fecha, "Se guardó la fecha")
        self.assertEqual(x.identificador, 50, "Se guardó el id")

    #Caso Inválido
    def testMontoNoEsNumero(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro("No es numero", fecha, 50)

    #Caso Frontera
    def testMontoVacio(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro(None, fecha, 50)
    
    #Caso Inválido        
    def testFechaNoEsDateTime(self):
        with self.assertRaises(SystemExit):
            Registro(50.7, '2012-06-12', 23)

    #Caso Frontera
    def testFechaVacia(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro(512.2, None, 50)
    
    #Caso Frontera        
    def testMontoMaximoFloat(self):
        fecha = datetime(2012,6,30)
        x = Registro(sys.float_info.max, fecha, 60)
        self.assertEqual(x.monto, sys.float_info.max, "El monto es el maximo flotante")
    
    #Caso Malicia
    def testMontoNegativo(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro(-0.77, fecha, 757)

     #Caso Malicia
    def testMontoNegativoMuyPequenio(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro((0-sys.float_info.min), fecha, 757)

    
    #Caso Frontera        
    def testMontoEsCero(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro(0, fecha, 57)
    

   
    
class PruebaBilleteraElectronica(unittest.TestCase):
    
    #Caso Interior
    def testBilleteraValida(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        self.assertTrue((type(x) is  BilleteraElectronica), "Es una Billetera Electronica")
    
    #Caso Inválido
    def testNoEsPersona(self):
        p="Hola Mundo"
        with self.assertRaises(SystemExit):
            BilleteraElectronica(12,p)
    
    #Caso Frontera
    def testConsumoSinSaldo(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = Registro(128,fecha,789)
        self.assertEqual(x.consumir(r), "No tiene suficiente saldo", "Consumo sin saldo")
    
    #Caso Inválido
    def testConsumoConAlgoQueNoEsRegistro(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = "Registro(128,fech,789)"
        self.assertEqual(x.consumir(r), "No es un registro", "Consumo entrada invalida")
    
    #Caso Inválido
    def testRecargaConAlgoQueNoEsRegistro(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = "Registro(128,fech,789)"
        self.assertEqual(x.recargar(r), "No es un registro", "Registro entrada invalida")
    
    #Caso Interior
    def testRecargaValidaYConsumoValido(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = Registro(128,fecha,789)
        self.assertEqual(x.recargar(r), "Recarga realizada", "Recarga Valida")
        self.assertEqual(x.consumir(r), "Consumo realizado", "Consumo Valida")
     
    #Caso   Interior
    def testBalance(self):
        p = Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = Registro(128,fecha,789)
        x.recargar(r)
        self.assertEqual(x.saldo(), x.balance, "Saldo correcto")

    #Caso Esquina
    def testSaldoMaximoYRecargaMaxima(self):
        p = Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(5,p)
        fecha = datetime(2012,6,30)
        r = Registro(sys.float_info.max,fecha,789)
        x.recargar(r)
        mensaje = x.recargar(r)
        self.assertEqual(mensaje, "No se puede recargar. Billetera llena", "No se puede recargar. Billetera llena")

    #Caso Esquina
    def testSaldoMaximoYRecargaPequenia(self):
        p = Persona("Mauricio","Salero","V-2499077","1212")
        x = BilleteraElectronica(5,p)
        fecha = datetime(2012,6,30)
        r = Registro(sys.float_info.max,fecha,789)
        x.recargar(r)
        r = Registro(0.0001,fecha,789)
        mensaje = x.recargar(r)
        self.assertEqual(mensaje, "No se puede recargar. Billetera llena", "No se puede recargar. Billetera llena")

    #Caso Esquina
    #Saldo maximo y consumo cero no se realiza, porque no se puede
    #crear un registro con valor 0. Igual para todos los casos esquinas
    #en que haya un cero en regarga o consumo.

    #Caso Esquina
    #Sald
        
     #Caso Esquina
    def testSaldoMaximoYGastoPequenio(self):
        p = Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(5,p)
        fecha = datetime(2012,6,30)
        r = Registro(sys.float_info.max,fecha,789)
        x.recargar(r)
        r = Registro(0.000001, fecha, 789)
        mensaje = x.consumir(r)
        self.assertEqual(mensaje, "Consumo realizado", "Consumo realizado")   
 
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
