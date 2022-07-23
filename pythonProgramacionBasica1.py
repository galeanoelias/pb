from array import array
import os
clear = lambda: os.system('cls')

"""
Ej 1)  Un programa que recibe el sexo de una persona como un char y retorne true si
el sexo de la persona es femenino (F) o  masculino (M) o false en cualquier otro caso.
"""

def Pantalla1():
    clear()
    active = False
    while not active:
        try:
            gender = input('Introduzca su genero/Enter your gender (F) o (M)\n')
            
            if gender == "F" or gender == "M":
                gender_sex =  True
            else:
                gender_sex = False
            print("Su genero seleccionado es/Your selected gender is", gender, "la respuesta es/the answer is: ", gender_sex)
            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor/Please enter a value F o M')

"""
Ej 2)  Un programa que recibe la edad de una persona y retorna True si es mayor de 18 años o false si es menor.
"""
        
def Pantalla2():
    clear()
    active = False
    while not active:
        try:
            age = int(input('Introduzca su edad/Enter your age: \n'))
            
            if age > 18:
                age_valid =  True
            else:
                age_valid = False
            print("Su edad es/your age is", age, "la respuesta es/the answer is: ", age_valid)
            opcion = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 3) Un programa que reciba una edad y retorne True si es menor a 10 o mayor a 60 en caso contrario retornara False.
"""
        
def Pantalla3():
    clear()
    active = False
    while not active:
        try:
            age = int(input('Introduzca su edad/Enter your age: \n'))
            
            if age < 10 or age > 60:
                age_valid =  True
            else:
                age_valid = False
            print("Su edad es/your age is", age, "la respuesta es/the answer is: ", age_valid)
            opcion = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 4) Un programa que reciba una temperatura en F° y la convierta a C°.
"""

def Pantalla4():
    clear()
    active = False
    while not active:
        try:
            degress = int(input('Introduzca su grados Fahrenheit/Enter your degrees Fahrenheit: \n'))
            
            celsius = (degress - 32)/1.8000
            print("Sus grados en Farenheit son/His degrees in Fahrenheit are: ", degress, "Sus grados en Celsius son/His degrees in Celsius are: ", celsius)
            opcion = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 5) Un programa que retorne true si la suma de los números en las posiciones “2” “3” y “4”
de un arreglo de enteros es par, de lo contrario retorna false.
"""

def Pantalla5():
    clear()
    active = False
    while not active:
        try:
            number_arrays = []
            while len(number_arrays) < 5:
                elem = int(input('Ingrese los numeros para rellenar el arreglo/Enter the numbers to fill the array: \n'))
                number_arrays.append(elem)       
                print(number_arrays)

            if number_arrays[2]%2 == 0 and number_arrays[3]%2 == 0 and number_arrays[4]%2 == 0:
                resolve_number =  True
            else:
                resolve_number = False
            print(resolve_number)
            opcion = input('Desea continuar/Do you wish to continue: Y/N\n')                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 6) Un programa que retorne true si un arreglo de enteros contiene al menos un número par,
de lo contrario retorna false.
"""

def Pantalla6():
    clear()
    active = False
    while not active:
        try:
            number_arrays = []
            while len(number_arrays) < 5:
                elem = int(input('Ingrese los numeros para rellenar el arreglo/Enter the numbers to fill the array: \n'))
                number_arrays.append(elem)       
                print(number_arrays)

            count = 0
            for number in number_arrays:
                if number%2 == 0:
                    count = count + 1
            
            if count >= 1:
                resolve_number =  True
            else:
                resolve_number = False     
            print(resolve_number)
            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 7) Un programa que retorne true si dos palabras son iguales entre sí, de lo contrario retorna false.
"""

def Pantalla7():
    clear()
    active = False
    while not active:
        try:
            def equal_word(word1, word2):
                if word1 == word2:
                    resolve_word =  True
                else:
                    resolve_word = False
                return resolve_word


            word_one = input('Introduzca una palabra/Enter a word: \n').lower()
            word_two = input('Introduzca una palabra/Enter a word: \n').lower()
            print(equal_word(word_one, word_two))
     
            option = input('¿Desea continuar?/Do you wish to continue?: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 8) Un programa donde el usuario  ingrese un día de la semana e imprimir un mensaje si es lunes,
otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo.
Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
"""

def Pantalla8():
    clear()
    active = False
    while not active:
        try:
            def equal_word(day_x):
                if day_x == "lunes":
                    print('Arriba que hay que arrancar la semana')
                elif day_x == "viernes":
                    print('Lo bueno dela semana es cuando va terminando')
                elif day_x == "sabado":
                    print('Arriba que se nos va el fnde y hay que disfrutarlo!!!')
                elif day_x == "domingo":
                    print('A juntar energia!! Mañana arrancamos la semana')
                elif day_x == "martes" or day_x == "miercoles" or day_x == "jueves":
                    print('Tenemos que seguír, estamos en plena semana')
                else:
                    print('Debes ingresar un dia de la semana, no otra cosa')
                return True

            day_week = input('Ingrese un dia de la semana: ').lower()
            print(equal_word(day_x = day_week))
             
            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 9) Un programa que retorne true si un entero es capicúa (ej: 12321), de lo contrario retorna false.
"""

def Pantalla9():
    clear()
    active = False
    while not active:
        try:
            def capicua_number(number_a):
                if number_a == number_a[::-1]:
                    resolve_number=  True
                else:
                    resolve_number = False
                return resolve_number

            number_capicua = input('Ingrese un numero/Enter a number: \n')    
            print(capicua_number(number_capicua))

            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 10) Un programa que retorne true si el número a es menor que b, de lo contrario retorna false.
"""

def Pantalla10():
    clear()
    active = False
    while not active:
        try:
            def minor_number(number_a, number_b):
                if number_a < number_b:
                    resolve_number=  True
                else:
                    resolve_number = False
                return resolve_number

            number1 = int(input('Ingrese un numero/Enter a number: \n'))
            number2 = int(input('Ingrese un numero/Enter a number: \n'))
            print(minor_number(number1, number2))

            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 11) Un programa que retorne true si la multiplicación del número a con el número b es igual a la división del número a con el número b.
"""

def Pantalla11():
    clear()
    active = False
    while not active:
        try:
            def math_number(number_a, number_b):
                if number_a * number_b == number_a / number_b:
                    resolve_number=  True
                else:
                    resolve_number = False
                return resolve_number
            
            number1 = int(input('Ingrese un numero/Enter a number: \n'))
            number2 = int(input('Ingrese un numero/Enter a number: \n'))
            print(math_number(number1, number2))
        
            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 12) Un programa que retorne true si un arreglo de enteros A contiene al menos dos números que también contenga el arreglo de enteros B.
"""

def Pantalla12():
    clear()
    active = False
    while not active:
        try:
            def array_comparison(array1, array2):
                count = 0
                for i in array1:
                    if i in array2:
                        count += 1
                if count >= 1:
                    equal_array =  True
                else:
                    equal_array = False 
                return equal_array
            
            array_number1 = []
            array_number2 = []
            while len(array_number1) < 5:
                numb = int(input('Ingrese los numeros para rellenar el arreglo/Enter the numbers to fill the array: \n'))
                array_number1.append(numb)       
                print(array_number1)
            
            while len(array_number2) < 5:
                numb2 = int(input('Ingrese los numeros para rellenar el segundo arreglo/Enter the numbers to fill the second array: \n'))
                array_number2.append(numb2)
                print(array_number2)
            
            print(array_comparison(array_number1, array_number2))
            
            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 13) Un programa que retorne la palabra que recibe pero al revés. (ej: hola, retorno = aloh).
"""

def Pantalla13():
    clear()
    active = False
    while not active:
        try:
            def upside_down(x):
                if x:
                    return "".join(reversed(x))
                else:
                    return print('Ingresa una palabra por favor!/ Enter a word please!')
            
            word1 = input('Ingrese una palabra/Enter a word: \n').capitalize()
            print(upside_down(x = word1))

            option = input('Desea continuar/Do you wish to continue: Y/N\n')
            if(option == 'N' or option == 'n'):
                active = True
        except:
            print('Por favor introduzca un dato valido/Please enter a valid data')

"""
Ej 14) Un programa que retorne la palabra que recibe cambiando todas sus vocales por x. (Ej: azul, retorno: xzxl).
"""

def Pantalla14():
    clear()
    active = False
    while not active:
        try:
            def word_change(words):
                vowel = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
                # return words for words in words  if c in vowel
                # for letter in words:
                #     if letter in vowel:
                #         print(letter)
                #     print(words.replace(letter, 'x'))


            word_of_change = input('Ingrese la palabra a inpeccionar/Enter the word to inspect: ').lower()
            print(word_change(word_of_change))
            
            # palabra = input('Ingrese una palabra\n')
            # vocales = ["a", "e", "i", "o", "u"]

            # for letra in palabra:
            #     if letra in vocales:
            #         palabra = palabra.replace(letra, "x")
                    
            # print(palabra)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

"""
Ej 15) Un programa que busque un string en una oracion y lo cambie por otra palabra.
"""

def Pantalla15():
    clear()
    active = False
    while not active:
        try:
            oracion = str(input('Ingrese una oración: '))
            palabra = str(input('Ingrse la palabra a cambiar: '))
            palabra2 = str(input('Ingrese la palabra a colocar: '))

            if palabra in oracion:
                oracion = oracion.replace(palabra, palabra2)
            else:
                print('La palabra no se encuentra en la oracion')

            print(oracion)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

"""
Ej 16) Un programa que reverse una lista
"""

def Pantalla16():
    clear()
    active = False
    while not active:
        try:
            lista_vacia = []
            elem = input('Ingrese los elementos de la lista: ')
            elem_split = elem.split()
            lista_vacia.append(elem_split)
            for elementos in lista_vacia:
               print(elementos)
            print(elementos[::-1])
            
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

"""
Ej 17) Un programa que busque elementos en una lista,
el elemento a buscar debe ser pasado como parametro en una
funcion.
"""

def Pantalla17():
    clear()
    active = False
    while not active:
        try:
            lista_vacia = []
            elem = input('Ingrese los elementos de la lista: ')
            elem_split = elem.split()
            lista_vacia.append(elem_split)
            for elementos in lista_vacia:
               print(elementos)

            search_value = input('Ingrese el elemento a buscar: ').lower()

            for search_value in lista_vacia:
                if search_value in lista_vacia:
                    print('Se encontro el elemento: ', search_value)
                else:
                    print('No se encontro el elmento buscado')

            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

"""
Ej 18) Crea un array o arreglo unidimensional donde le indiques
el tamaño por teclado y crear una función que rellene el array o
arreglo con los múltiplos de un número pedido por teclado.
Por ejemplo, si defino un array de tamaño 5 y elijo un 3 en la
función, el array contendrá 3, 6, 9, 12, 15.
Muestralos por pantalla usando otra función distinta.
"""

def Pantalla18():
    clear()
    active = False
    while not active:
        try:
            amount = int(input('Ingrese el tamaño que desea para su arreglo/Enter the size you want for your array: '))
            multiple = int(input('Ingrese el numero de multiplos/Enter the number of multiples: '))
            array_one_dimensional = []
            for i in range(0, amount):
                array_one_dimensional.append(i * multiple)
                print(array_one_dimensional)
        
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

"""
Ej 19) Dado el siguiente arreglo de números:
[1, 2 , 5, 8, 3, 30, 9, 13]
Imprimir en pantalla programáticamente los números impares
mayores a 7.
"""

def Pantalla19():
    clear()
    active = False
    while not active:
        try:
            arrays_numbers = [1, 2 , 5, 8, 3, 30, 9, 13]
            older_than_seven = []
            for i in arrays_numbers:
                if i > 7 and i % 2 != 0:
                    older_than_seven.append(i)
                    print('Estos son los numeros impares mayores a 7/These are the odd numbers greater than seven: ', older_than_seven)
                else:
                    continue

            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

"""
Ej 20) Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la función
(min) y escriba en pantalla. Luego programáticamente calcule el
promedio de notas descontando la nota eliminada.
"""

def Pantalla20():
    clear()
    active = False
    while not active:
        try:
            def number_min(numbers):
                min_n = numbers[0]

                for i in numbers:
                    if i < min_n:
                        min_n = i
                
                return min_n

            array_of_notes = [20, 15, 12, 11, 8, 4, 1]
            min_value = number_min(array_of_notes)
            print('este es el valor minimo del arreglo/This is the minimum value of array: ', min_value)

            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

active = False
while not active:
    clear()
    print('Un clasico:')
    print('1 - Elige tu sexo')
    print('2 - Mayor de edad')
    print('3 - Edad < 10 o >60')
    print('4 - Conversor de grados')
    print('5 - posiciones pares en un array')
    print('6 - Mas de un par en un array')
    print('7 - Palabras iguales')
    print('8 - Días de la semana')
    print('9 - Es capicua?')
    print('10 - < o >')
    print('11 - a*b = a/b')
    print('12 - A en B')
    print('13 - Al reves')
    print('14 - Vocales a x')
    print('15 - Cambiar palabras en oraciones')
    print('16 - Reverse en una lista')
    print('17 - Search elements in list')
    print('18 - Array one-dimensional')
    print('19 - Number grater than seven')
    print('20 - Value minimum')
    print('21 - Exit')
    opcion = input('Introduce un numero:')
    try:
        if int(opcion) == 1:
            Pantalla1()
        elif int(opcion) == 2:
            Pantalla2()
        elif int(opcion) == 3:
            Pantalla3()
        elif int(opcion) == 4:
            Pantalla4()
        elif int(opcion) == 5:
            Pantalla5()
        elif int(opcion) == 6:
            Pantalla6()
        elif int(opcion) == 7:
            Pantalla7()
        elif int(opcion) == 8:
            Pantalla8()
        elif int(opcion) == 9:
            Pantalla9()
        elif int(opcion) == 10:
            Pantalla10()
        elif int(opcion) == 11:
            Pantalla11()
        elif int(opcion) == 12:
            Pantalla12()
        elif int(opcion) == 13:
            Pantalla13()
        elif int(opcion) == 14:
            Pantalla14()
        elif int(opcion) == 15:
            Pantalla15()
        elif int(opcion) == 16:
            Pantalla16()
        elif int(opcion) == 17:
            Pantalla17()
        elif int(opcion) == 18:
            Pantalla18()
        elif int(opcion) == 19:
            Pantalla19()
        elif int(opcion) == 20:
            Pantalla20()
        elif int(opcion) == 21:
            print('Saliendo')
            active = True   
    except:
        print("Por favor introduzca una opcion valida")