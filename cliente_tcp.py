#!/usr/bin/env python3
"""
Cliente TCP - Dispara múltiplas requisições simultâneas
"""

import socket
import threading
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5000
NUM_REQUESTS = 50


def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] {msg}")


def send_request(request_id):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        
        mensagem = f"Mensagem do cliente {request_id}"
        client_socket.sendall(mensagem.encode('utf-8'))
        
        resposta = client_socket.recv(1024).decode('utf-8')
        log(f"✅ Cliente {request_id:2d}: {resposta[:50]}...")
        
        client_socket.close()
        
    except Exception as e:
        log(f"❌ Cliente {request_id:2d}: Erro - {e}")


def main():
    log("=" * 60)
    log("CLIENTE TCP - TESTE DE CONCORRÊNCIA")
    log(f"{NUM_REQUESTS} requisições simultâneas → {HOST}:{PORT}")
    log("=" * 60)
    
    threads = []
    start_time = time.time()
    
    log("🚀 Disparando threads...")
    
    for i in range(1, NUM_REQUESTS + 1):
        t = threading.Thread(target=send_request, args=(i,))
        threads.append(t)
        t.start()
    
    log(f"📤 {NUM_REQUESTS} requisições enviadas!")
    log("⏳ Aguardando (deve levar ~2s com threads)...")
    
    for t in threads:
        t.join()
    
    total_time = time.time() - start_time
    
    log("=" * 60)
    log(f"✨ CONCLUÍDO em {total_time:.2f}s")
    log(f"🎯 Com threads: ~2s | Sem threads: ~{NUM_REQUESTS*2}s")
    log("=" * 60)


if __name__ == "__main__":
    main()