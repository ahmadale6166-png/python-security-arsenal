import sys
import socket
import socks
import time

def escanear_objetivo(host, puertos):
    print(f"\n🛡️ Iniciando escaneo anónimo vía Tor (SOCKS5: 127.0.0.1:9050)")
    print(f"🎯 Objetivo: {host}")
    print("-" * 45)

    # Configurar el socket global para usar el proxy SOCKS5 de Tor
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

    puertos_abiertos = []
    
    inicio = time.time()
    for puerto in puertos:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(4)  # Timeout de 4 segundos por puerto
        try:
            # Intento de conexión TCP a través de Tor
            s.connect((host, puerto))
            print(f"  [+] Puerto {puerto}: ABIENTO")
            puertos_abiertos.append(puerto)
            s.close()
        except socket.timeout:
            print(f"  [-] Puerto {puerto}: Filtrado / Timeout")
        except socket.error:
            print(f"  [-] Puerto {puerto}: Cerrado")
        except Exception as e:
            print(f"  [!] Error en puerto {puerto}: {e}")

    fin = time.time()
    print("-" * 45)
    print(f"✅ Escaneo completado en {round(fin - inicio, 2)} segundos.")
    if puertos_abiertos:
        print(f"Puertos abiertos detectados: {puertos_abiertos}")
    else:
        print("No se encontraron puertos abiertos en la lista especificada.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 escaner_puertos_tor.py <dominio_o_ip> [puerto1,puerto2,...]")
    else:
        objetivo = sys.argv[1]
        
        # Puertos por defecto si no se especifican (ej. 80, 443, 22, 21, 8080)
        puertos_comunes = [21, 22, 80, 443, 8080]
        
        if len(sys.argv) > 2:
            try:
                puertos_comunes = [int(p) for p in sys.argv[2].split(",")]
            except ValueError:
                print("[!] Formato de puertos inválido. Usando lista predeterminada.")

        escanear_objetivo(objetivo, puertos_comunes)
