def funcion_sin_parametros():
    print("Holamundo, esto es una funcion sin parametros");
#entre las parentesis se pone el parametro o variable que se ocupara dentro de la funcion, como a continuacion
def funcion_con_parametros(palabra):
    #imprimira un texto pero ademas imprimira la palabra que se le de en el parametro
    print("Holamundo, esta es una funcion con parametros el cual imprime una palabra que se le de: ", palabra);

#aqui simplemente se "llama" a la funcion
funcion_sin_parametros();
#aqui se "llama" a la funcion pero se le de un texto como parametro
funcion_con_parametros("aqui le estoy dando el parametro")

def estano():
    print ("Esta es sin parametro")

def estasi(frase):
    print ("esta es con parametro", frase)
    
estano();
estasi("lo vees");

def sumar (num1,num2):
    print (num1+num2)
    
sumar (1,2);

def saludar(nombre):
    print ("¡Hola, " + nombre + "!")
nombre = input()
saludar (nombre);
