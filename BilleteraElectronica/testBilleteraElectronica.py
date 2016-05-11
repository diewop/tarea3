'''
Created on 10/05/2016

@author: PedrozaSalerno
'''
import unittest
from IN import INT_MAX


class Persona(unittest.TestCase):


    def testDatosValidos(self):
        X = Persona("Chu-li","Salerno","V-24900767",4679)
        self.assertEqual(X.nombre, "Chu-li", "Nombre aceptado")
        self.assertEqual(X.apellido, "Salerno", "Apellido aceptado")
        self.assertEqual(X.ci, "V-24900767", "Cedula aceptada")
        self.assertEqual(X.pin, 4679, "PIN aceptado")
    
    def testNombreNumero(self):
        with self.assertRaises(SystemExit):
            Persona(1232,"Salerno","V-24900767",4679)
            
    def testNombreStringConNumeros(self):
        with self.assertRaises(SystemExit):
            Persona("Maur1cio","Salerno","V-24900767",4679)
    
    def testNombreCaracteresInvalidos(self):
        with self.assertRaises(SystemExit):
            Persona("Ma/uri=ci*","Salerno","V-24900767",4679)
            
    def testNombreVacio(self):
        with self.assertRaises(SystemExit):
            Persona(None,"Salerno","V-24900767",4679)
    
    def testApellidoNumero(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio",1234,"V-24900767",4679)
            
    def testApellidoStringConNumeros(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Sal3rno","V-24900767",4679)
    
    def testApellidoCaracteresInvalidos(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Ma/uri=ci*","V-24900767",4679)
    
    def testApellidoVacio(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio",None,"V-24900767",4679)
            
    def testCedulaMalformada(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-249E077",4679)
    
    def testCedulaVacia(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno",None,4679) 
            
    def testPINEnteroMax(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",INT_MAX)
    
    def testPINEnteroNegativo(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",-4679)
            
    def testPINNoEsNumero(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077","4679")
    
    def testPINEsFlotante(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",46.21)
    
    def testPINVacio(self):
        with self.assertRaises(SystemExit):
            Persona("Mauricio","Salerno","V-2499077",None)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()