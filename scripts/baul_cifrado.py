import sys
import os
import base64
import hashlib
from cryptography.fernet import Fernet

ARCHIVO_BAUL = "mi_baul_secreto.enc"

def generar_llave(password):
    # Derivar una llave segura de 32 bytes desde la contraseña maestra
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def guardar_secreto(password, mensaje):
    key = generar_llave(password)
    f = Fernet(key)
    token = f.encrypt(mensaje.encode())
    with open(ARCHIVO_BAUL, "wb") as archivo:
        archivo.write(token)
    print("🔒 [Éxito] Secreto guardado y cifrado con AES-256 en el baúl.")

def leer_secreto(password):
    if not os.path.exists(ARCHIVO_BAUL):
        print("⚠️ [Aviso] No existe ningún baúl cifrado todavía.")
        return
    try:
        key = generar_llave(password)
        f = Fernet(key)
        with open(ARCHIVO_BAUL, "rb") as archivo:
            token = archivo.read()
        mensaje_desencriptado = f.decrypt(token).decode()
        print("\n🔓 [Éxito] Secreto descifrado correctamente:")
        print(f"📄 Contenido: {mensaje_desencriptado}\n")
    except Exception:
        print("❌ [Error] Contraseña maestra incorrecta o archivo alterado.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 baul_cifrado.py [guardar|leer] 'password_maestra' ['mensaje']")
    else:
        accion = sys.argv[1]
        pwd = sys.argv[2]
        if accion == "guardar" and len(sys.argv) > 3:
            guardar_secreto(pwd, sys.argv[3])
        elif accion == "leer":
            leer_secreto(pwd)
        else:
            print("Acción no válida.")
