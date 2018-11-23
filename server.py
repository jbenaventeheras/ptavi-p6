#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""
import os
import sys
import socketserver

VALID_METHODS = 'INVITE', 'ACK', 'BYE'

if len(sys.argv) != 4:
        sys.exit('Usage: python3 server.py IP port audio_file')
else:
    if os.path.exists(sys.argv[3]):
        audio_file = sys.argv[3]
    else:
        sys.exit('File not found')
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])

class RTPHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            if not line:
                break
            line_lista = line.decode('utf-8').split()
            method = line.decode('utf-8').split(' ')[0]
            print (line_lista)
            print (len(line_lista))
            print(method)
            if method == 'INVITE':
                self.wfile.write(b'SIP/2.0 100 Trying, SIP/2.0 180 Ringing y SIP/2.0 200 OK\r\n\r\n')
            elif method == 'ACK':
            elif method not in VALID_METHODS:
                self.wfile.write(b'SIP/2.0 405 Method Not Allowed\r\n\r\n')
            else:
                self.wfile.write(b"SIP/2.0 400 Bad Request\r\n\r\n")

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer((SERVER, 6001), RTPHandler)
    print("listening....")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('End server')
