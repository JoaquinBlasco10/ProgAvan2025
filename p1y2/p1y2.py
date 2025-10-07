#JOAQUÍN BLASCO HÍPOLA


# Ejercicio 1===================================================================================

def process_text(text="This is a default text with Python and amazing words.",
                 words_to_replace=["Python", "amazing"]):
    """
    Procesa un texto: lo convierte a minúsculas, elimina espacios
    y reemplaza las palabras dadas por asteriscos.
    """
    text = text.lower().strip()
    replaced = 0
    for word in words_to_replace:
        if word.lower() in text:
            text = text.replace(word.lower(), "*" * len(word))
            replaced += 1
    return text, replaced


def main():
    processed, count = process_text()
    print("Processed text:", processed)
    print("Palabras reemplazadas:", count)


if __name__ == "__main__":
    main()


# Ejercicio 2==============================================================================================

def is_prime(n):
    """Comprueba si un número es primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_list(limit):
    """Devuelve una lista de números primos hasta el límite."""
    return [n for n in range(2, limit + 1) if is_prime(n)]


def check_palindrome(primes):
    """Devuelve los primos que son palíndromos."""
    return [p for p in primes if str(p) == str(p)[::-1]]


def categorize_prime(prime):
    """Clasifica un número primo."""
    if prime < 10:
        return "pequeño"
    elif prime < 100:
        return "mediano"
    else:
        return "grande"


def main():
    limit = int(input("Introduce un límite: "))
    primes = prime_list(limit)
    print("Lista de primos:", primes)
    print("Palíndromos:", check_palindrome(primes))
    print("Clasificación:")
    for p in primes:
        print(f"{p}: {categorize_prime(p)}")


if __name__ == "__main__":
    main()




# Ejercicio 3===============================================================================================

def suma_total(nums):
    return sum(nums)

def suma_pos_neg(nums):
    pos = sum(n for n in nums if n > 0)
    neg = sum(n for n in nums if n < 0)
    return pos, neg

def max_min(nums):
    return max(nums), min(nums)

def numeros_unicos(nums):
    return len(nums) == len(set(nums))

def comparar_pos_neg(nums):
    pos = sum(1 for n in nums if n > 0)
    neg = sum(1 for n in nums if n < 0)
    if pos > neg:
        return "Más positivos"
    elif neg > pos:
        return "Más negativos"
    else:
        return "Iguales"


def main():
    numeros = [int(x) for x in input("Introduce números separados por espacios: ").split()]
    while True:
        print("\n1. Suma total")
        print("2. Suma positivos y negativos")
        print("3. Máximo y mínimo")
        print("4. Números únicos")
        print("5. Más positivos o negativos")
        print("6. Salir")
        op = input("Opción: ")

        if op == "1":
            print("Suma total:", suma_total(numeros))
        elif op == "2":
            pos, neg = suma_pos_neg(numeros)
            print("Positivos:", pos, "Negativos:", neg)
        elif op == "3":
            mx, mn = max_min(numeros)
            print("Máximo:", mx, "Mínimo:", mn)
        elif op == "4":
            print("¿Todos únicos?:", numeros_unicos(numeros))
        elif op == "5":
            print(comparar_pos_neg(numeros))
        elif op == "6":
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()




# Ejercicio 4=========================================================================

tareas = []  # variable global

def add_task(task):
    tareas.append(task)
    print(f"Tarea '{task}' agregada.")

def remove_task(task):
    if task in tareas:
        tareas.remove(task)
        print(f"Tarea '{task}' eliminada.")
    else:
        print("No existe esa tarea.")

def list_tasks():
    print("\nLista de tareas:")
    for i, t in enumerate(tareas, 1):
        print(f"{i}. {t}")

def task_manager():
    def modify_task():
        if tareas:
            tareas[0] = tareas[0] + " (modificada)"
            print(f"Tarea modificada: {tareas[0]}")
        else:
            print("No hay tareas para modificar.")
    modify_task()

def main():
    add_task("Comprar leche")
    add_task("Llamar al doctor")
    add_task("Hacer ejercicio")
    list_tasks()
    task_manager()
    list_tasks()
    remove_task("Hacer ejercicio")
    list_tasks()


if __name__ == "__main__":
    main()





# Ejercicio 5==============================================================================================

def imprimir_por_letra(cadenas, letra):
    for c in cadenas:
        if c.startswith(letra):
            print(c)

def contar_subcadena(cadenas, sub):
    return sum(sub in c for c in cadenas)

def cadena_larga_corta(cadenas):
    return max(cadenas, key=len), min(cadenas, key=len)

def comparar_objetos(cadenas, i1, i2):
    return cadenas[i1] is cadenas[i2]

def verificar_longitud(cadenas):
    for c in cadenas:
        if len(c) > 10:
            print(f"'{c}' tiene más de 10 caracteres.")
            break
    else:
        print("Ninguna cadena tiene más de 10 caracteres.")

def main():
    cadenas = input("Introduce cadenas separadas por comas: ").split(",")
    while True:
        print("\n1. Imprimir por letra")
        print("2. Contar subcadena")
        print("3. Cadena más larga y más corta")
        print("4. Comparar si dos son el mismo objeto")
        print("5. Verificar longitudes")
        print("6. Salir")
        op = input("Opción: ")

        if op == "1":
            letra = input("Letra: ")
            imprimir_por_letra(cadenas, letra)
        elif op == "2":
            sub = input("Subcadena: ")
            print("Cantidad:", contar_subcadena(cadenas, sub))
        elif op == "3":
            larga, corta = cadena_larga_corta(cadenas)
            print("Más larga:", larga, "Más corta:", corta)
        elif op == "4":
            i1 = int(input("Índice 1: "))
            i2 = int(input("Índice 2: "))
            print("¿Mismo objeto?:", comparar_objetos(cadenas, i1, i2))
        elif op == "5":
            verificar_longitud(cadenas)
        elif op == "6":
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()



# Ejercicio 6=====================================================================================

import re
from datetime import datetime

def procesar_informe(informe):
    """Elimina datos personales del informe médico."""
    informe = re.sub(r"\b\d{1,2}/\d{1,2}/\d{4}\b", "FECHA", informe)
    informe = re.sub(r"Nombre:.*", "Nombre: PACIENTE", informe)
    informe = re.sub(r"Dr\.|Dra\.", "MEDICO", informe)

    nacimiento = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})", informe)
    if nacimiento:
        dia, mes, año = map(int, nacimiento.groups())
        edad = datetime.now().year - año
        informe = re.sub(r"Fecha de nacimiento:.*", f"Edad: {edad}", informe)
    return informe


def main():
    informe = """Informe clínico de Urgencias

Nombre: Juan Pérez López
Género: Hombre
Fecha de nacimiento: 12/05/1980
Motivo de consulta: dolor abdominal
12/05/2023 Dr. Ramírez
Tratamiento: reposo y analgésicos"""

    print(procesar_informe(informe))


if __name__ == "__main__":
    main()
