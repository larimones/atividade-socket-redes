#!/usr/bin/env python3
"""
Cliente UDP - Dispara múltiplas requisições simultâneas
"""

import socket
import threading
import time
from datetime import datetime

HOST = '127.0.0.1'
PORT = 5001
NUM_REQUESTS = 50
BUFFER_SIZE = 1024
TIMEOUT = 5


def log(msg):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    print(f"[{timestamp}] {msg}")


def send_request(request_id):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(TIMEOUT)
        
        mensagem = f"Mensagem UDP {request_id}"
        client_socket.sendto(mensagem.encode('utf-8'), (HOST, PORT))
        
        resposta, server = client_socket.recvfrom(BUFFER_SIZE)
        log(f"✅ Cliente {request_id:2d}: {resposta.decode('utf-8')[:50]}...")
        
        client_socket.close()
        
    except socket.timeout:
        log(f"⏱️ Cliente {request_id:2d}: Timeout")
    except Exception as e:
        log(f"❌ Cliente {request_id:2d}: Erro - {e}")


def main():
    log("=" * 60)
    log("CLIENTE UDP - TESTE DE CONCORRÊNCIA")
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
    
    for t in threads:
        t.join()
    
    total_time = time.time() - start_time
    
    log("=" * 60)
    log(f"✨ CONCLUÍDO em {total_time:.2f}s")
    log(f"🎯 Com threads: ~2s | Sem threads: ~{NUM_REQUESTS*2}s")
    log("=" * 60)


if __name__ == "__main__":
    main()