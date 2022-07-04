#Getting user input python
your_name = input("Enter your name: ")
print(f"Hello {your_name}. I am Gerardo.")

#Cuidado, input te devuelve un string
age = input("How old are you? ")
duplicado = age*12
print(duplicado)

#Como debería ser
age = int(input("How old are you? "))
print(f"You have lived {age*12} months")

#Las cosas dentro del paréntesis siempre se ejecutan primero

#BOOLEANS and COMPARISONS in python
truthy = True
falsy = False

age = 20 
is_over = age >= 18
is_twenty = age == 20       #Doble = es para comparación

#Example 
my_number = 5
user_number = int(input("Dame un número"))
matches = my_number == user_number
print(f"lo atinaste: {matches}.")

#And, Or

age = int(input("Dime tu edad"))
puede_aprender =  0 < age and age < 150

# AND te da el primer valor si es Falso. De otra forma te da el segundo
# OR te da el primer valor si es verdadero, de lo contrario te da el segundo

#Example

name = input("Dime tu nombre ")
surname = input("Dime tu apellido ")

greeting = name or surname
print(f"Hola {greeting}.")