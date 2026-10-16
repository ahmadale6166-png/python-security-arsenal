import os

def monitorear_red():
    print("\n🔍 Analizando conexiones de red activas en el dispositivo...")
    print("-" * 60)
    # En Termux/Android, netstat o ss nos muestra las conexiones activas
    resultado = os.popen("ss -tuln || netstat -tuln").read()
    print(resultado)
    print("-" * 60)
    print("💡 Si ves servicios extraños escuchando en puertos no reconocidos, revísalos.")

if __name__ == "__main__":
    monitorear_red()
