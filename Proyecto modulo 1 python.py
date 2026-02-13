# Calculadora de Índice de Masa Corporal (IMC) - Anghelo Carrillo

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Este campo no puede quedar vacío.")
        else:
            return valor

def pedir_numero(mensaje, tipo=float, minimo=None):
    """Pide un número con validación de tipo y mínimo."""
    while True:
        valor = input(mensaje).strip()
        if valor == "":
            print("Este campo no puede quedar vacío.")
            continue
        try:
            valor = tipo(valor)
            if minimo is not None and valor <= minimo:
                print(f"El valor debe ser mayor que {minimo}.")
                continue
            return valor
        except ValueError:
            print("Por favor, introduce un número válido.")

# Número de personas
personas = pedir_numero("¿Cuántas personas quieres registrar?: ", int, 0)

# Lista para guardar registros
registros = []

while personas > 0:
    nombre = pedir_texto("¿Cuál es tu nombre?: ")
    edad = pedir_numero("¿Cuál es tu edad?: ", int, 0)
    altura = pedir_numero("¿Cuál es tu altura en metros?: ", float, 0)
    peso = pedir_numero("¿Cuánto pesas en kilogramos?: ", float, 0)

    imc = peso / altura**2

    # Guardar registro
    registros.append({
        "nombre": nombre,
        "edad": edad,
        "altura": altura,
        "peso": peso,
        "imc": imc
    })

    # Resultados individuales
    print(f"\n{nombre}, tu IMC es {imc:.2f}")
    print("Eres menor de edad" if edad <= 17 else "Eres mayor de edad")

    if imc <= 15.99:
        print("Te hace falta comer más, te puede llevar el aire")
    elif imc <= 16.99:
        print("Mete un poco más de comida, estás delgado")
    elif imc <= 18.49:
        print("Estás un poco delgado, mete más comida")
    elif imc <= 24.99:
        print("Sigue comiendo así, estás en tu peso ideal")
    elif imc <= 29.99:
        print("Estás un poco pasado de peso, haz ejercicio y come más sano")
    elif imc <= 34.99:
        print("Estás pasado de peso, haz ejercicio y come más sano")
    elif imc <= 39.00:
        print("Estás muy pasado de peso, haz ejercicio y come más sano")
    else:
        print("Estás extremadamente pasado de peso, haz ejercicio y come más sano")

    personas -= 1
    print("-" * 40)


print("\nResumen de registros:")
for r in registros:
    print(f"{r['nombre']} - Edad: {r['edad']} - IMC: {r['imc']:.2f}")