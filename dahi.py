def es_primo():
     num=int(input(" Ingrese un número entero por favor:"))

     if num <= 3:
          print (" El número es primo")
     elif num > 3 and num % 2 == 0:
          return False
     else:
          for i in range (3, num ):
               if num % i== 0 :
                    return False 
               

   
es_primo()

