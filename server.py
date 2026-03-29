import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def log_message(self, format, *args):
        print(f"  [{self.command}] {self.path}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    for port in [8000, 8080, 8888, 3000]:
        try:
            httpd = socketserver.TCPServer(("", port), CORSHandler)
            httpd.allow_reuse_address = True
            print(f"\n  🐾 PawVision rodando em: http://localhost:{port}")
            print("  Ctrl+C para encerrar\n")
            webbrowser.open(f"http://localhost:{port}")
            httpd.serve_forever()
            break
        except OSError as e:
            print(f"  Porta {port} ocupada, tentando próxima...")
    else:
        print("  ERRO: Nenhuma porta disponível (8000, 8080, 8888, 3000)")
        sys.exit(1)