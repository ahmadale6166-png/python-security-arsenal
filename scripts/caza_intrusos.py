import http.server
import socketserver
from datetime import datetime

PORT = 8080

class HoneypotHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Capturar IP real (manejando Cloudflare)
        client_ip = (
            self.headers.get('CF-Connecting-IP') or 
            self.headers.get('X-Forwarded-For') or 
            self.client_address[0]
        )
        user_agent = self.headers.get('User-Agent', 'Desconocido')
        ruta = self.path
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 2. Clasificar el tráfico
        nivel = "INFO"
        if "SqlMap" in user_agent or "/admin" in ruta or "wp-login" in ruta:
            nivel = "ALERTA_ROJA"

        # 3. Registrar en archivo de logs
        log_line = f"[{timestamp}] [{nivel}] IP: {client_ip} | Ruta: {ruta} | UA: {user_agent}\n"
        print(log_line.strip())
        
        with open("intrusos_log.txt", "a") as f:
            f.write(log_line)

        # 4. Responder al atacante (Señuelo / Honeypot trap)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Página señuelo para atrapar la interacción del escáner
        html_trap = b"""
        <!DOCTYPE html>
        <html>
        <head><title>Admin Portal</title></head>
        <body>
          <h2>Acceso Restringido</h2>
          <form method="POST">
            <input type="text" name="user" placeholder="Usuario">
            <input type="password" name="pass" placeholder="Password">
            <button type="submit">Entrar</button>
          </form>
        </body>
        </html>
        """
        self.wfile.write(html_trap)

    def do_POST(self):
        # Mismo manejo para peticiones POST (como envíos de formularios de login)
        self.do_GET()

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), HoneypotHandler) as httpd:
        print(f"[*] Honeypot activo en puerto {PORT}...")
        httpd.serve_forever()
