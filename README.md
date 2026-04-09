# Atividade Prática: Cliente/Servidor TCP e UDP com Multithreading

## 📚 Disciplina de  REDES DE COMUNICAÇÃO E APLICAÇÕES DISTRIBUIDAS (IOT)
Um servidor TCP é um programa de rede que aguarda e gerencia conexões de clientes usando o Transmission Control Protocol (TCP). Ele garante a entrega confiável, ordenada e sem erros de pacotes de dados, sendo fundamental para serviços como HTTP, e-mail (SMTP) e transferência de arquivos (FTP).

Já um servidor UDP é um programa de rede que utiliza o User Datagram Protocol (UDP) para receber dados sem estabelecer uma conexão prévia, oferecendo alta velocidade e baixa latência. Diferente do TCP, ele não garante a entrega, a ordem dos pacotes ou a correção de erros, sendo ideal para streaming de vídeo, jogos online e VoIP.

## Objetivo

Desenvolver em Python dois servidores (um TCP e um UDP) e dois scripts de cliente.
*Servidores*: Devem utilizar a biblioteca threading para processar múltiplas requisições ao mesmo tempo. Adicione um atraso simulado (ex: time.sleep(2)) no atendimento de cada requisição.
*Clientes*: Devem disparar N requisições simultâneas (ex: 50 requisições ao mesmo tempo) contra o servidor.
*Objetivo*: Provar no terminal que o servidor não trava esperando o sleep de um cliente acabar para atender o próximo, mas sim que atende todos em paralelo usando as threads.

Vídeo de Demonstração (YouTube):

## 📁 Arquivos

| Arquivo | Descrição |
|---------|-----------|
| `servidor_tcp.py` | Servidor TCP com threads |
| `cliente_tcp.py` | Cliente TCP que dispara 50 requisições |
| `servidor_udp.py` | Servidor UDP com threads |
| `cliente_udp.py` | Cliente UDP que dispara 50 requisições |

## 🚀 Como Executar

### Terminal 1 - Servidor TCP:

```bash
python servidor_tcp.py
```

### Terminal 2 - Cliente TCP:

```bash
python cliente_tcp.py
```

### Terminal 3 - Servidor UDP:

```bash
python servidor_udp.py
```

### Terminal 4 - Cliente UDP:

```bash
python cliente_udp.py
```

## Resultado esperado

Com multithreading: ~2 segundos para 50 requisições
Sem multithreading: ~100 segundos (sequencial)
Speedup: 50x mais rápido
