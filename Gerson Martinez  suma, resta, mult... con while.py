number_1=float(input("Ingrese el valor del primer numero: "))
number_2=float(input("Ingrese el valor del segundo numero: "))
option=""
addition=0
rest=0
multiplication=0
division=0



while not(option in ["a","b","c","d"]):
    option=input("Ingrese la letra indicada para cada operacion suma->a,resta->b,multiplicacion->c,division->d:")
    
if option=="a":
    addition=number_1+number_2
    print("La suma es:",addition,)
if option=="b":
    rest=number_1-number_2
    print("La resta es:",rest,)
if option=="c":
    multiplication=number_1*number_2
    print("La multiplication:",multiplication,)
if option=="d":
    if number_2==0:
        while  number_2==0:
            number_2=float(input("La division entre sero no esta permitida.Ingrese otro valor para el segundo numero:"))
    if number_2!=0:
        division=number_1/number_2
        print("La division es: ",division,)
        
        
        
        
        
        
        
    