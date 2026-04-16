import http.server
import socketserver
import os
import json
import smtplib
import urllib.parse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PORT = 5000
HOST = "0.0.0.0"

RECIPIENT_EMAIL = "suhagraphics145@gmail.com"
SENDER_EMAIL = os.environ.get("GMAIL_ADDRESS", "")
SENDER_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "")

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

    def do_POST(self):
        if self.path == "/contact":
            try:
                length = int(self.headers.get("Content-Length", 0))
                raw = self.rfile.read(length).decode("utf-8")
                content_type = self.headers.get("Content-Type", "")

                if "application/json" in content_type:
                    data = json.loads(raw)
                else:
                    data = dict(urllib.parse.parse_qsl(raw))

                name    = data.get("name", "N/A")
                company = data.get("company", "N/A")
                phone   = data.get("phone", "N/A")
                service = data.get("service", "N/A")
                message = data.get("message", "N/A")

                body = f"""
New enquiry from the Suhada Graphics website:

Name    : {name}
Company : {company}
Phone   : {phone}
Service : {service}

Message:
{message}
"""

                if SENDER_EMAIL and SENDER_PASSWORD:
                    msg = MIMEMultipart()
                    msg["From"] = SENDER_EMAIL
                    msg["To"] = RECIPIENT_EMAIL
                    msg["Subject"] = f"New Enquiry from {name} — Suhada Graphics"
                    msg.attach(MIMEText(body, "plain"))

                    with smtplib.SMTP("smtp.gmail.com", 587) as server:
                        server.starttls()
                        server.login(SENDER_EMAIL, SENDER_PASSWORD)
                        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())

                    print(f"Email sent for enquiry from {name}")
                    self._json_response(200, {"ok": True})
                else:
                    print("GMAIL_ADDRESS or GMAIL_APP_PASSWORD not set — cannot send email.")
                    self._json_response(500, {"ok": False, "error": "Email not configured"})

            except Exception as e:
                print(f"Contact form error: {e}")
                self._json_response(500, {"ok": False, "error": str(e)})
        else:
            self.send_error(404)

    def _json_response(self, code, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer((HOST, PORT), Handler) as httpd:
    print(f"Serving on http://{HOST}:{PORT}")
    httpd.serve_forever()
