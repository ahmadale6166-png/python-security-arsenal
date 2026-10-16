import sys
import hashlib
import base64

def procesar_texto(texto):
    print("\n" + "="*40)
    print("⚙️ INFORME CRIPTOGRÁFICO DE TEXTO")
    print("="*40)
    print(f"Texto original : {texto}")
    print(f"MD5            : {hashlib.md5(texto.encode()).hexdigest()}")
    print(f"SHA-256        : {hashlib.sha256(texto.encode()).hexdigest()}")
    b64_enc = base64.b64encode(texto.encode()).decode()
    print(f"Base64 (Enc)   : {b64_enc}")
    try:
        b64_dec = base64.b64decode(texto.encode()).decode()
        print(f"Base64 (Dec)   : {b64_dec}")
    except Exception:
        pass
    print("="*40 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python3 util_crypto.py 'texto_a_procesar'")
    else:
        procesar_texto(sys.argv[1])
