import sys
import os

def inspeccionar_archivo(ruta):
    if not os.path.exists(ruta):
        print(f"❌ [Error] El archivo '{ruta}' no existe.")
        return
    print(f"\n🔍 Analizando metadatos de: {ruta}")
    print("-" * 50)
    # Ejecuta exiftool para ver los metadatos
    os.system(f"exiftool '{ruta}'")
    print("-" * 50)

def limpiar_archivo(ruta):
    if not os.path.exists(ruta):
        print(f"❌ [Error] El archivo '{ruta}' no existe.")
        return
    print(f"\n🧹 Eliminando todos los metadatos sensibles de: {ruta}...")
    # El comando -all= borra todos los metadatos de la imagen/archivo y crea un respaldo original (_original)
    resultado = os.system(f"exiftool -all= '{ruta}'")
    if resultado == 0:
        print("✅ [Éxito] Metadatos eliminados correctamente. Tu archivo ahora es anónimo.")
        # Limpiar el archivo de respaldo automático que crea exiftool
        respaldo = ruta + "_original"
        if os.path.exists(respaldo):
            os.remove(respaldo)
    else:
        print("❌ [Error] No se pudieron eliminar los metadatos.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 limpiador_metadatos.py [ver|limpiar] 'ruta/al/archivo'")
    else:
        accion = sys.argv[1]
        archivo = sys.argv[2]
        if accion == "ver":
            inspeccionar_archivo(archivo)
        elif accion == "limpiar":
            limpiar_archivo(archivo)
        else:
            print("Acción no válida. Usa 'ver' o 'limpiar'.")
