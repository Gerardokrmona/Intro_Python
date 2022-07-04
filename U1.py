from bdb import GENERATOR_AND_COROUTINE_FLAGS
x = 30
print(x)

x = 25
print(x)

#Snake_case consiste en nombrar las variables usando _ 
# en los lugares donde es necesario un espacio

#Two types of numbers 
age = 35            #INTEGER
PI = 3.1416         #FLOAT

maths_oper = 1 + 3 * 4 / 2 - 2
print(maths_oper)

#Division gives a float, if you want a integer you use //

integer_div = 5 // 2   #remove everything after the dot
print(integer_div)

integer_division = 13 // 5
print(integer_div)

remainder = 13 % 5
print(remainder)

# Así podemos saber si un número es par o impar

x = 37
remainder = x % 2
print(remainder)        # output 1 means a odd number

#Strings are used to use text/caracters

my_string = "Hello, World"
print(my_string)
print("Hello, it's me")
print('she said: "you are amazing" yesterday')
print("she said: \"you are amazing\" yesterday")  #Escaping

#multiline string
multiline = """
Hello, we are learning
how to use
python
"""
print(multiline)

"""
Es común usar estas 3 comillas para hacer un comentario grande
así no hay necesidad de poner # en cada renglón
"""

name = "jose"
greeting = "Hello, " + name     #Concatenamos los string
print(greeting)

#La función str() convierte a string su argumento

#String formatting

#example 1
age = 30
age_string = str(age)
print("I am " + age_string)

#example 2
print(f"I am {age}") #No hace falta convertir ni concatenar 

#example 3
name = "Gerardo"
print(f"Hello, my name is {name}")

#example 4
final_greeting = "how are you, {}?"
gera_greeting = final_greeting.format(name)
print(gera_greeting)