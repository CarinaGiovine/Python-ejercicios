# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:22:23 2021

@author: CarinaGiovine
"""

import numpy as np

class Categoria_Monotributo:
    
    def __init__(self, facturacion_media):
        self.categorias = np.array([["A",273453,2562],["B",410180,2864 ],["C",546907,3275],
              ["D",820361,3862],["E",1093014,5072],["F",1367268,6072],
              ["G",1640722,7082],["H",2278780,12383],["I",2677577,114852],
              ["J",3076353,17058],["K",3418170,19280]])   #se declara un array bidimensional con las catgorias de AFIP
        
        
        self.facturacion_m=facturacion_media
       


    def buscarCategoria (self):
   
        for row in self.categorias:    #recorro por fila el array
        
          for cat in row :
          
            tope_mensual = float(row[1]) / 12
            if(tope_mensual >= self.facturacion_m):
                return print("Categoria: " + row[0] + "\n" + "Limite de Facturacion Mensual: $" + str(round(tope_mensual,2)) + "\n" + "Debera pagar por mes: $" + str(row[2]))
            

c=Categoria_Monotributo(56000) 
c.buscarCategoria()


   
 
        