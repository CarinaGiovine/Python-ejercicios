
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 17:03:15 2020

@author´s: Octavio Gomez, Carina Giovine y Eduardo Herrero Rivero
"""

# Funcionalidad:
# Al ingresar el promedio facturado mensual el sistema informa que categoria 
#de monotributo me corresponde y cuanto debo abonar por mes.
#además se agrego color a las salidas por consola utilizando código ANSI

# Crear un array de Categorias (A B C D E F G H I J K ), este array debe
# contener otro array con los datos de la categoria 
# LETRA, 
# BRUTO_FACTURADO_ANUAL, 
# CUOTA_MENSUAL

 
import numpy as np

#declaro array bidimencional
categorias = np.array([["A",273453,2562],["B",410180,2864 ],["C",546907,3275],
              ["D",820361,3862],["E",1093014,5072],["F",1367268,6072],
              ["G",1640722,7082],["H",2278780,12383],["I",2677577,114852],
              ["J",3076353,17058],["K",3418170,19280]])

#print(categorias)

print("""\033[;36m

                        (0 0) 
                ---oOO-- (_) ----oOO---    
+---------------------------------------------------+ 
¦En base a su  Facturacion Bruta Anual se calcula la¦
¦  categoria de Monotributo y el monto de la cuota  ¦ 
¦ mensual que podra abonar hasta el 20 de cada mes: ¦
+---------------------------------------------------+ 
                -----------------------
                      |__|__| 
                       || || 
                      ooO Ooo 
""")
            
facturacion_media = float(input("  Ingrese su Facturacion Bruta Mensual: $"))


def buscarCategoria (categorias,facturacion_media):
    #indicador = 0;
    #recorro por fila el array
    for row in categorias:
        
        for cat in row :
          
            tope_mensual = float(row[1]) / 12
            if(tope_mensual >= facturacion_media):
                return "Categoria: " + row[0] + "\n" + "Limite de Facturacion Mensual: $" + str(round(tope_mensual,2)) + "\n" + "Debera pagar por mes: $" + str(row[2])
            
cat_resultante = buscarCategoria (categorias,facturacion_media) 

print("\033[46m" +
"""


▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
""")

print("\033[0m" + "\033[36m" + """
  A partir del 1° de Enero de 2021 Ud. queda asi:
""")
   
 
print(cat_resultante)  
         
         
print("\033[0m" + "\033[46m" +
"""
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
""")
