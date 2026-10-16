const https = require('https');
const fs = require('fs');

// Carga los certificados para mantener el HTTPS seguro
const options = {
  key: fs.readFileSync('auto.key'),
  cert: fs.readFileSync('auto.crt')
};

https.createServer(options, (req, res) => {
  // Captura la IP y los datos del navegador del visitante
  const ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
  const userAgent = req.headers['user-agent'] || 'Desconocido';
  const fechaHora = new Date().toISOString();

  // Crea el texto del registro de la visita
  const registro = `[${fechaHora}] IP: ${ip} | Navegador: ${userAgent}\n`;

  // Guarda la información silenciosamente en un archivo llamado 'intrusos.txt'
  fs.appendFile('intrusos.txt', registro, (err) => {
    if (err) console.error('Error al guardar el registro', err);
  });

  // Muestra una página falsa para despistar al visitante
  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.end(`
    <!DOCTYPE html>
    <html>
    <head><title>Sitio en Mantenimiento</title></head>
    <body style="font-family: Arial; text-align: center; padding-top: 50px;">
      <h1>🔒 Sitio Privado</h1>
      <p>Este espacio se encuentra bajo mantenimiento o acceso restringido.</p>
    </body>
    </html>
  `);
}).listen(3000, () => {
  console.log('🛡️ Panel fantasma / Honeypot activo en https://localhost:3000');
});

