#!/usr/bin/env python3
"""
=============================================================================
  🤖 PYTHON WHATSAPP BOT (neonize Multi-Device)
=============================================================================
Bot para WhatsApp em Python com suporte nativo a Multi-Device e QR Code
utilizando a biblioteca neonize (Go whatsmeow bindings). Compatível com Discloud.
"""

import os
import sys
import time
from datetime import datetime
from dotenv import load_dotenv

from neonize.client import NewClient
from neonize.events import ConnectedEv, MessageEv

load_dotenv()

DB_NAME = os.getenv("SESSION_DB", "whatsapp_session.db")
START_TIME = time.time()


def format_uptime(seconds: float) -> str:
    total_seconds = int(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    rem_seconds = total_seconds % 60
    return f"{hours}h {minutes}m {rem_seconds}s"


client = NewClient(DB_NAME)


@client.event(ConnectedEv)
def on_connected(_: NewClient, __: ConnectedEv) -> None:
    print("==================================================")
    print("🤖 Bot WhatsApp Conectado com Sucesso!")
    print("⚡ Framework:     neonize (Python + whatsmeow engine)")
    print(f"🐍 Python:        v{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    print("==================================================")
    print("🟢 Bot online e pronto para responder a comandos (!ping ou /ping)!")


@client.event(MessageEv)
def on_message(c: NewClient, message: MessageEv) -> None:
    # Ignora mensagens enviadas pelo próprio bot
    if message.Info.MessageSource.IsFromMe:
        return

    # Extrai o texto da mensagem
    text = ""
    if message.Message.conversation:
        text = message.Message.conversation
    elif message.Message.extendedTextMessage and message.Message.extendedTextMessage.text:
        text = message.Message.extendedTextMessage.text
    elif message.Message.imageMessage and message.Message.imageMessage.caption:
        text = message.Message.imageMessage.caption
    elif message.Message.videoMessage and message.Message.videoMessage.caption:
        text = message.Message.videoMessage.caption

    clean_text = text.strip().lower()

    if clean_text in ["!ping", "/ping"]:
        start_process = time.perf_counter()

        uptime_str = format_uptime(time.time() - START_TIME)
        latency_ms = round((time.perf_counter() - start_process) * 1000)

        response_text = (
            "🏓 *Pong! Estatísticas do Bot (Python)*\n\n"
            f"⚡ *Latência de Processamento:* `{latency_ms}ms`\n"
            f"⏱️ *Tempo Ativo (Uptime):* `{uptime_str}`\n"
            "🐍 *Framework:* `neonize (Python SDK)`\n"
            "🟢 *Status:* `Online & Conectado via WhatsApp Multi-Device`\n"
            f"⚙️ *Versão Python:* `v{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}`\n"
            "🧠 *Motor Criptográfico:* `Go whatsmeow FFI (Zero-Copy)`\n\n"
            "_Automação veloz em Python!_"
        )

        chat_jid = message.Info.MessageSource.Chat
        c.send_message(chat_jid, response_text)
        print(f"📩 Comando !ping respondido para {chat_jid}")


if __name__ == "__main__":
    print("🔄 Inicializando cliente do WhatsApp em Python...")
    print("📲 Caso seja o primeiro acesso, o QR Code será exibido no terminal:")
    client.connect()
