import sys
import string
import random
import math

def calcular_entropia(longitud, tam_conjunto):
    # Fórmula de entropía de la información: H = L * log2(R)
    if tam_conjunto == 0:
        return 0
    bits = longitud * math.log2(tam_conjunto)
    return round(bits, 2)

def estimar_tiempo(bits_entropia):
    # Estimación basada en 10 mil millones de intentos por segundo (hardware moderno)
    intentos_totales = 2 ** bits_entropia
    intentos_por_segundo = 10_000_000_000
    segundos = intentos_totales / intentos_por_segundo
    
    if segundos < 60:
        return f"{round(segundos, 2)} segundos"
    elif segundos < 3600:
        return f"{round(segundos / 60, 2)} minutos"
    elif segundos < 86400:
        return f"{round(segundos / 3600, 2)} horas"
    elif segundos < 31536000:
        return f"{round(segundos / 86400, 2)} días"
    elif segundos < 31536000 * 1000:
        return f"{round(segundos / 31536000, 2)} años"
    else:
        return "Prácticamente imposible (Miles de millones de años)"

def generar_password(longitud=16):
    letras_min = string.ascii_lowercase
    letras_may = string.ascii_uppercase
    numeros = string.digits
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Asegurar al menos un carácter de cada tipo
    password = [
        random.choice(letras_min),
        random.choice(letras_may),
        random.choice(numeros),
        random.choice(simbolos)
    ]
    
    # Rellenar el resto de la longitud
    todos_caracteres = letras_min + letras_may + numeros + simbolos
    for _ in range(longitud - 4):
        password.append(random.choice(todos_caracteres))
        
    random.shuffle(password)
    return "".join(password)

def auditar_password(pwd):
    longitud = len(pwd)
    tiene_min = any(c.islower() for c in pwd)
    tiene_may = any(c.isupper() for c in pwd)
    tiene_num = any(c.isdigit() for c in pwd)
    tiene_sim = any(c in string.punctuation for c in pwd)
    
    # Calcular tamaño del conjunto de caracteres (R) según complejidad
    r = 0
    if tiene_min: r += 26
    if tiene_may: r += 26
    if tiene_num: r += 10
    if tiene_sim: r += len(string.punctuation)
    
    entropia = calcular_entropia(longitud, r)
    tiempo = estimar_tiempo(entropia)
    
    print("\n" + "="*40)
    print("🔐 INFORME DE AUDITORÍA DE CONTRASEÑA")
    print("="*40)
    print(f"🔑 Clave analizada : {pwd}")
    print(f"📏 Longitud         : {longitud} caracteres")
    print(f"🧮 Entropía         : {entropia} bits")
    print(f"⏱️ Tiempo de ataque : {tiempo}")
    print("-" * 40)
    
    if entropia < 60:
        print("⚠️  Nivel: DÉBIL (Vulnerable a ataques rápidos)")
    elif entropia < 80:
        print("⚡ Nivel: MODERADO (Aceptable, pero mejorable)")
    else:
        print("🛡️ Nivel: FUERTE / ROBUSTA (Altamente segura)")
    print("="*40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Si pasas una contraseña como argumento, la audita
        pwd_usuario = sys.argv[1]
        auditar_password(pwd_usuario)
    else:
        # Si no, genera una clave robusta por defecto y la audita
        print("\n✨ Generando contraseña segura automática...")
        nueva_pwd = generar_password(16)
        auditar_password(nueva_pwd)
