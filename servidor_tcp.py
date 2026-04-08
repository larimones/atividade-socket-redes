#!/usr/bin/env python3
"""
Servidor TCP com Multithreading
Atividade Prática - Redes de Computadores
"""

import socket
import threading
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5000
MAX_CONNECTIONS = 100


def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] {msg}")


def handle_client(conn, addr, request_id):
    log(f"🟢 Thread iniciada para Cliente {request_id} - {addr}")
    
    try:
        data = conn.recv(1024).decode('utf-8')
        log(f"📥 Cliente {request_id} enviou: '{data}'")
        
        log(f"⏳ Cliente {request_id} - Processando (sleep 2s)...")
        time.sleep(2)
        
        resposta = f"Resposta TCP para req {request_id}: '{data}' processado!"
        conn.sendall(resposta.encode('utf-8'))
        log(f"📤 Cliente {request_id} - Resposta enviada")
        
    except Exception as e:
        log(f"❌ Erro no Cliente {request_id}: {e}")
    finally:
        conn.close()
        log(f"🔴 Thread finalizada para Cliente {request_id}")


def main():
    log("=" * 60)
    log("SERVIDOR TCP COM MULTITHREADING")
    log(f"Host: {HOST} | Porta: {PORT}")
    log("=" * 60)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(MAX_CONNECTIONS)
        log(f"🚀 Servidor TCP iniciado em {HOST}:{PORT}")
        log(f"📋 Aguardando conexões... (Ctrl+C para encerrar)")
        log("-" * 60)
        
        request_counter = 0
        
        while True:
            conn, addr = server_socket.accept()
            request_counter += 1
            
            log(f"🔗 Nova conexão de {addr} (Req #{request_counter})")
            
            client_thread = threading.Thread(
                target=handle_client,
                args=(conn, addr, request_counter),
                daemon=True
            )
            client_thread.start()
            
            active_threads = threading.active_count() - 1
            log(f"📊 Threads ativas: {active_threads}")
            
    except KeyboardInterrupt:
        log("\n⚠️ Servidor encerrado pelo usuário")
    finally:
        server_socket.close()
        log("🔌 Socket fechado")


if __name__ == "__main__":
    main()