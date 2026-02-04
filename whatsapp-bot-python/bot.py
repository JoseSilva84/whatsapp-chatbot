from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# ===== CONFIG =====
SESSION_NAME = "junior2"
BASE_URL = "http://localhost:21465/api"

API_KEY = os.getenv("API_KEY")
SESSION_TOKEN = os.getenv("SESSION_TOKEN")

SEND_MESSAGE_URL = f"{BASE_URL}/{SESSION_NAME}/send-message"

HEADERS = {
    "Authorization": f"Bearer {SESSION_TOKEN}",  # TOKEN DA SESSÃO
    "apikey": API_KEY,                           # TOKEN GLOBAL DA API
    "Content-Type": "application/json"
}

# ===== ESTADO DOS USUÁRIOS =====
encerrados = {}  # Dicionário para rastrear usuários que encerraram a conversa


# ===== ENVIAR MENSAGEM =====
def enviar_mensagem(numero, texto):
    payload = {
        "phone": numero,
        "message": texto
    }

    try:
        response = requests.post(SEND_MESSAGE_URL, json=payload, headers=HEADERS)
        print("\n📤 Enviando mensagem...")
        print("Número:", numero)
        print("Status:", response.status_code)
        print("Resposta:", response.text)
    except Exception as e:
        print("❌ Erro ao enviar:", e)


# ===== MENU =====
def processar_menu(numero, mensagem):
    msg = mensagem.strip().lower()

    if msg in ["oi", "olá", "ola", "boa noite", "boa tarde", "bom dia", "menu"]:
        enviar_mensagem(numero,
            "🙋🏻‍♂️ Bem-vindo ao meu WhatsApp - Sou José Silva - Desenvolvedor Web\n\n"
            "Digite uma opção:\n"
            "1️⃣ Falar comigo no pessoal\n"
            "2️⃣ Ver horário de trabalho\n"
            "3️⃣ Ver meus serviços\n"
            "4️⃣ Quem sou"
        )

    elif msg == "1":
        encerrados[numero] = True  # Marca o usuário como encerrado
        enviar_mensagem(numero, "🫸🏽 Pronto. Logo será atendido por José Silva. Caso desejar retornar ao menu principal, é só digitar a palavra *menu*")

    elif msg == "2":
        enviar_mensagem(numero, "🕒 Nosso horário é das 08h às 17h.")

    elif msg == "3":
        enviar_mensagem(numero, "👩‍💼 Ofereço serviços especializados em desenvolvimento de software para empresas que precisam de resultados reais: Desenvolvimento Full Stack: Criação de sistemas web completos, escaláveis e sob medida, do banco de dados à interface do usuário. Chatbots Inteligentes: Construção de assistentes virtuais com IA para automatizar seu atendimento, qualificar leads e vender 24h por dia. Integrações: Conecto suas plataformas para garantir que a informação flua sem erros entre o chat e seu sistema interno.O objetivo é simples: Menos trabalho manual e mais eficiência para sua operação.")

    elif msg == "4":
        enviar_mensagem(numero, "🏢 Full Stack Developer | ADS Especialista em desenvolvimento de ponta a ponta. Formado em Análise e Desenvolvimento de Sistemas, trabalho na construção de aplicações modernas e otimizadas. Apaixonado por resolver desafios através da tecnologia e entregar valor em cada linha de código.")

    else:
        enviar_mensagem(numero, "❓ Opção inválida.")
        enviar_mensagem(numero,
            "🙋🏻‍♂️ Bem-vindo ao meu WhatsApp - Sou José Silva - Desenvolvedor Web\n\n"
            "Digite uma opção:\n"
            "1️⃣ Falar comigo no pessoal\n"
            "2️⃣ Ver horário de trabalho\n"
            "3️⃣ Ver meus serviços\n"
            "4️⃣ Quem sou"
        )



# ===== WEBHOOK =====
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("\n📩 Webhook recebido:", data)

    # Só responde mensagens de usuários
    if data.get("event") == "onmessage" and not data.get("fromMe", False):

        numero = data.get("from", "").replace("@c.us", "")
        mensagem = data.get("body", "")

        print(f"💬 Mensagem de {numero}: {mensagem}")

        # Permite reativar a conversa enviando "menu"
        msg = mensagem.strip().lower()
        if msg == "menu" and numero in encerrados:
            del encerrados[numero]
            print(f"🔄 Conversa reativada para {numero}")

        # Verifica se a conversa está encerrada para este usuário
        if numero in encerrados:
            print(f"💬 Mensagem de {numero} ignorada (conversa encerrada): {mensagem}")
            return jsonify({"status": "ok"}), 200

        processar_menu(numero, mensagem)

    else:
        print("ℹ️ Evento ignorado:", data.get("event"))

    return jsonify({"status": "ok"}), 200


# ===== START =====
if __name__ == "__main__":
    print("🚀 Bot rodando na porta 5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
