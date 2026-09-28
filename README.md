# 🐍 Python WhatsApp Bot (`neonize Multi-Device`)

Um bot moderno para **WhatsApp Multi-Device** em **Python 3.10+** utilizando a biblioteca [`neonize`](https://github.com/krypton-byte/neonize), que integra a consagrada engine em Go `whatsmeow` através de FFI de alta performance (Zero-Copy).

Totalmente preparado para hospedagem local e nuvem como **Discloud**.

---

## 🚀 Funcionalidades

- 📲 **Conexão Multi-Device**: Escaneie o QR Code exibido diretamente no seu terminal.
- 💾 **Persistência de Sessão**: Armazena as chaves no banco SQLite `whatsapp_session.db`, mantendo a conexão ativa mesmo após reiniciar.
- 🏓 **Comando `!ping` ou `/ping`**:
  - Latência de processamento em milissegundos.
  - Tempo de atividade do bot (*Uptime* formatado em horas, minutos e segundos).
  - Informações de versão do Python e motor criptográfico.
- ☁️ **Compatível com Discloud**: Arquivo `discloud.config` pronto para deploy na Discloud com apenas 100MB de RAM.

---

## 📁 Estrutura do Projeto

```text
python-whatsapp-bot/
├── bot.py                 # Código principal do bot e eventos
├── requirements.txt       # Dependências (neonize, python-dotenv, segno)
├── discloud.config        # Arquivo de configuração da Discloud
├── .env.example           # Modelo de variáveis de ambiente
├── .gitignore             # Arquivos e sessões ignorados pelo Git
└── README.md              # Documentação do projeto
```

---

## 🛠️ Pré-requisitos

- **Python 3.10 ou superior** instalado.
- Smartphone com o aplicativo do **WhatsApp** instalado.

---

## ⚙️ Configuração e Instalação Local

### 1. Clonar o Repositório
```bash
git clone https://github.com/jjuniornoc-rgb/python-whatsapp-bot.git
cd python-whatsapp-bot
```

### 2. Criar Ambiente Virtual (Recomendado)
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o Bot

```bash
python bot.py
```

1. Um **QR Code** será exibido no seu terminal.
2. Abra o WhatsApp no seu celular:
   - **Android**: Toque nos três pontinhos no canto superior direito > **Aparelhos conectados** > **Conectar um aparelho**.
   - **iPhone (iOS)**: Toque em **Configurações** > **Aparelhos conectados** > **Conectar um aparelho**.
3. Aponte a câmera para o QR Code no terminal.
4. Quando autenticar, envie `!ping` ou `/ping` em qualquer chat para receber a resposta do bot!

---

## ☁️ Hospedagem na Discloud

1. Comprima os seguintes arquivos num arquivo `.zip`:
   - `bot.py`
   - `requirements.txt`
   - `discloud.config`
   - `.env`
2. No painel da [Discloud](https://discloudbot.com) ou via CLI da Discloud:
   ```bash
   discloud upload
   ```
3. O bot iniciará automaticamente utilizando o arquivo `bot.py`.

---

## 📜 Licença

Distribuído sob a licença MIT. Consulte `LICENSE` para mais informações.
