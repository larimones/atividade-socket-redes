#!/usr/bin/env python3
"""
Servidor UDP com Multithreading
"""

import socket
import threading
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5001
BUFFER_SIZE = 1024


def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] {msg}")


def handle_request(data, client_addr, request_id, server_socket):
    log(f"Thread iniciada para Req {request_id} - {client_addr}")
    
    try:
        mensagem = data.decode('utf-8')
        log(f"Req {request_id}: '{mensagem}'")
        
        log(f"Req {request_id} - Processando (sleep 2s)...")
        time.sleep(2)
        
        resposta = f"Resposta UDP req {request_id}: '{mensagem}' OK!"
        server_socket.sendto(resposta.encode('utf-8'), client_addr)
        log(f"Req {request_id} - Resposta enviada")
        
    except Exception as e:
        log(f"Erro req {request_id}: {e}")
    
    log(f"Thread finalizada para Req {request_id}")


def main():
    log("=" * 60)
    log("SERVIDOR UDP COM MULTITHREADING")
    log(f"Host: {HOST} | Porta: {PORT}")
    log("=" * 60)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((HOST, PORT))
        log(f"Servidor UDP iniciado em {HOST}:{PORT}")
        log(f"Aguardando datagramas...")
        log("-" * 60)
        
        request_counter = 0
        
        while True:
            data, client_addr = server_socket.recvfrom(BUFFER_SIZE)
            request_counter += 1
            
            log(f"Datagrama de {client_addr} (Req #{request_counter})")
            
            request_thread = threading.Thread(
                target=handle_request,
                args=(data, client_addr, request_counter, server_socket),
                daemon=True
            )
            request_thread.start()
            
            active_threads = threading.active_count() - 1
            log(f"-> Threads ativas: {active_threads}")
            
    except KeyboardInterrupt:
        log("\n Servidor encerrado")
    finally:
        server_socket.close()
        log("Socket fechado")


if __name__ == "__main__":
    main()