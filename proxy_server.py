import http.server
import socketserver
import requests
from urllib.parse import urlparse

# Proxy settings
HOST = "127.0.0.1"
PORT = 8080
TARGET_HOST = "www.example.com"

class MITMProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.proxy_request("GET")

    def do_POST(self):
        self.proxy_request("POST")

    def do_PUT(self):
        self.proxy_request("PUT")

    def do_DELETE(self):
        self.proxy_request("DELETE")

    def proxy_request(self, method):
        """Handles proxying requests while preserving paths and query parameters."""
        parsed_url = urlparse(self.path)
        target_url = f"https://{TARGET_HOST}{self.path}"  # Preserve full path & query

        # Extract headers and body from the client's request
        client_headers = {key: self.headers[key] for key in self.headers.keys()}
        body = self.rfile.read(int(self.headers.get('Content-Length', 0))) if 'Content-Length' in self.headers else None

        # Logging the incoming request from the client
        print("\n============================")
        print(f"Incoming {method} Request (From Client):")
        print(f"URL: {self.path}")
        print(f"Headers: {client_headers}")
        if body:
            print(f"Body: {body.decode('utf-8', errors='ignore')}")
        print("============================\n")

        # Modify headers if necessary (e.g., remove hop-by-hop headers)
        proxy_headers = client_headers.copy()
        proxy_headers["Host"] = TARGET_HOST  # Ensure Host header matches target API

        # Logging the request the proxy is sending to the target server
        print("\n----------------------------")
        print(f"Forwarding {method} Request (To {TARGET_HOST}):")
        print(f"URL: {target_url}")
        print(f"Headers: {proxy_headers}")
        if body:
            print(f"Body: {body.decode('utf-8', errors='ignore')}")
        print("----------------------------\n")

        try:
            # Forward request to target server
            response = requests.request(method, target_url, headers=proxy_headers, data=body, allow_redirects=False)

            # Logging the full response from the target server
            print("\n********** Response from Target Server **********")
            print(f"Status Code: {response.status_code}")
            print(f"Headers: {dict(response.headers)}")
            # Full response body without truncation
            response_text = response.content.decode('utf-8', errors='ignore')
            print(f"Body:\n{response_text}")
            print("************************************************\n")

            # Send response back to the client
            self.send_response(response.status_code)
            for key, value in response.headers.items():
                self.send_header(key, value)
            self.end_headers()
            self.wfile.write(response.content)

        except requests.RequestException as e:
            print(f"Error: {e}")
            self.send_error(502, f"Bad Gateway: {str(e)}")

# Start the proxy server
with socketserver.ThreadingTCPServer((HOST, PORT), MITMProxyHandler) as server:
    print(f"MITM Proxy running on {HOST}:{PORT}")
    server.serve_forever()
