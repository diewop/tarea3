'''
Created on 10/05/2016

@author: PedrozaSalerno
'''
import unittest
from IN import INT_MAX
import sys
from datetime import datetime

from BilleteraElectronica import *



class PruebaPersona(unittest.TestCase):


    def testDatosValidos(self):
        X = Persona("Chu-li-ñon","López", "V-24900767","4679")
        self.assertEqual(X.nombre, "Chu-li-ñon", "Nombre aceptado")
        self.assertEqual(X.apellido, "López", "Apellido aceptado")
        self.assertEqual(X.ci, "V-24900767", "Cedula aceptada")
        self.assertEqual(X.pin, "4679", "PIN aceptado")
    
    def testNombreNumero(self):
        with self.assertRaises(SystemExit):
            Persona(1232,"Salerno","V-24900767","4679")
            
    def testNombreStringConNumeros(self):
        with self.assertRaises(SystemExit):
            Persona("Maur1cio","Salerno","V-24900767","4679")
    
    def testNombreCaracteresInvalidos(self):
        with self.assertRaises(SystemExit):
            Persona("Ma/uri=ci*","Salerno","V-24900767","4679")
            
    def testNombreVacio(self):
        with self.assertRaises(SystemExit):
            Persona(None,"Salerno","V-24900767","4679")
    
    def testApellidoNumero(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio",1234,"V-24900767","4679")
            
    def testApellidoStringConNumeros(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Sal3rno","V-24900767","4679")
    
    def testApellidoCaracteresInvalidos(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Ma/uri=ci*","V-24900767","4679")
    
    def testApellidoVacio(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio",None,"V-24900767","4679")
            
    def testCedulaMalformada(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-249E077","4679")
    
    def testCedulaVacia(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno",None,"4679") 
            
    def testPINEntero(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",INT_MAX)
    
    def testPINConNumeroNegativo(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077","-4679")
            
    def testPINSonLetras(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077","AbCd")
    
    def testPINEsFlotante(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077","46.21")
    
    def testPINVacio(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",None)
    
    def testPINEsCero(self):
        x=Persona("Mauricio","Salerno","V-2499077","0")
        self.assertEqual(x.pin, "0", "Pin Es cero")

    def testPINCerosALaIzquierda(self):
        x=Persona("Mauricio","Salerno","V-2499077","0001")
        self.assertNotEqual(x.pin, "1", "PIN: 0001 != 1")
        


class PruebaRegistro(unittest.TestCase):
    def testMontoNoEsNumero(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro("No es numero", fecha, 50)
            
    def testFechaNoEsDateTime(self):
        with self.assertRaises(SystemExit):
            Registro(50.7, '2012-06-12', 23)
            
    def testMontoMaximoFloat(self):
        fecha = datetime(2012,6,30)
        x = Registro(sys.float_info.max, fecha, 60)
        self.assertEqual(x.monto, sys.float_info.max, "El monto es el maximo flotante")
    
    def testMontoNegativo(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro(-0.77, fecha, 757)
            
    def testMontoEsCero(self):
        fecha = datetime(2012,6,30)
        with self.assertRaises(SystemExit):
            Registro(0, fecha, 57)
    
   
    
class PruebaBilleteraElectronica(unittest.TestCase):
    
    
    def testBilleteraValida(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        self.assertTrue((type(x) is  BilleteraElectronica), "Es una Billetera Electronica")
    
    def testNoEsPersona(self):
        p="Hola Mundo"
        with self.assertRaises(SystemExit):
            BilleteraElectronica(12,p)
    
    def testConsumoSinSaldo(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = Registro(128,fecha,789)
        self.assertEqual(x.consumir(r), "No tiene suficiente saldo", "Consumo sin saldo")
    
    
    def testConsumoConAlgoQueNoEsRegistro(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = "Registro(128,fech,789)"
        self.assertEqual(x.consumir(r), "No es un registro", "Consumo entrada invalida")
    
    def testRecargaConAlgoQueNoEsRegistro(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = "Registro(128,fech,789)"
        self.assertEqual(x.recargar(r), "No es un registro", "Registro entrada invalida")
    
    def testRecargaValidaYConsumoValido(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = Registro(128,fecha,789)
        self.assertEqual(x.recargar(r), "Recarga realizada", "Recarga Valida")
        self.assertEqual(x.consumir(r), "Consumo realizado", "Consumo Valida")
        
    def testBalance(self):
        p=Persona("Mauricio","Salerno","V-2499077","1212")
        x = BilleteraElectronica(12,p)
        fecha = datetime(2012,6,30)
        r = Registro(128,fecha,789)
        x.recargar(r)
        self.assertEqual(x.saldo(), x.balance, "Saldo correcto")
        
        
 
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()