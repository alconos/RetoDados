import random
import time

def mis_dados():
    
    n=random.randint(1, 6)
    m=random.randint(1, 6)
    resp=(input("Quieres tirar los dados (s/n) : "  ))
    time.sleep(2)
    suma=n+m
    
    if resp == "s":
    
        print(n, m,"= ", suma)
        break    
    else:
        print("Adios")
        quit()
    
    
    time.sleep(1) 
          
    if (suma == 7 or suma == 11):
        print("Todos ganan")
        mis_dados()
    elif (suma ==2 or suma == 6 or suma == 12):
        print("Jugador gana")
        mis_dados()      
    else:
        print("Siga probando")   
        mis_dados()
       

mis_dados()
