#Créer une fonction prenant 4 paramètres et les retournant en ordre croissant en utilisant que des conditions(en n’utilisant pas de loops).

def ordre_croissant(num1,num2,num3,num4):
    return num1, num2, num3, num4
 
num1 = int(input("Entrez le premier nombre: ")) 
num2 = int(input("Entrez le deuxieme nombre: "))
num3 = int(input("Entrez le troisieme nombre: ")) 
num4 = int(input("Entrez le quatrieme nombre: "))
 #num1 = 1
 #num2 = 2
 #num3 = 3
 #num4 = 4

#if(num1<=num2<=num3<=num4):
ordre_croissant(num1,num2,num3,num4)
if(num1<=num2<=num3<=num4):
    print("num1,num2,num3,num4")
else:
    print("Il n'y a pas de l'ordre croissant")
    
