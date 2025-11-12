import unittest
from src.procesador import Analizador #estamos importando el analizador


class TestAnalizador(unittest.TestCase):#el parentesis es herencia, es una clase que tiene atributos y metodos

    @classmethod
    def setUpClass(cls): #cls es 
        cls.analizador = Analizador("datos/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        self.assertEqual(total_provincias, 25)

    def test_ventas_totales_mayores_5k(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        todas_mayores= True
        for valor in resumen.values():
            if float(valor) <= 5000:
                todas_mayores = False
                break
        self.assertTrue(todas_mayores)

    def ventas_por_provincia(self, provincia):
        provincia = provincia.strip().lower()
        ventas = self.ventas_totales_por_provincia()
        if provincia not in ventas:
            raise KeyError(f"Provincia '{provincia}' no encontrada")
        return ventas[provincia]


    def test_ventas_por_provincia_existente(self):
        resultado = self.analizador.ventas_por_provincia("pichincha")
        self.assertGreater(resultado, 0)