# WPPConnect Server com Bot Python

![Logo ou Banner](https://via.placeholder.com/800x200?text=WPPConnect+Server+Bot) <!-- Substitua por uma imagem real se disponível -->

Um projeto completo para integração com WhatsApp usando WPPConnect, incluindo um servidor API em Node.js/TypeScript e um bot automatizado em Python com Flask.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [API Endpoints](#api-endpoints)
- [Webhook](#webhook)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## 🎯 Sobre o Projeto

Este projeto oferece uma solução completa para automação de mensagens no WhatsApp. O **WPPConnect Server** versão 2.20 fornece uma API RESTful para interagir com o WhatsApp Web, enquanto o **Bot Python** implementa um assistente virtual simples com menu interativo.

O bot responde automaticamente a mensagens recebidas via webhook, oferecendo informações sobre serviços de desenvolvimento web e atendimento personalizado.

## ✨ Funcionalidades

### Servidor WPPConnect
- ✅ Conexão com WhatsApp Web via qrcode gerado pela api
- ✅ Envio e recebimento de mensagens
- ✅ Gerenciamento de sessões
- ✅ Suporte a mídia (imagens, vídeos, documentos)
- ✅ Controle de grupos e contatos
- ✅ API RESTful completa
- ✅ Documentação Swagger
- ✅ Logs detalhados

### Bot Python
- 🤖 Respostas automáticas via webhook
- 📱 Menu interativo com opções numeradas
- 👤 Atendimento personalizado
- 🕒 Informações de horário de trabalho
- 💼 Descrição de serviços oferecidos
- 🏢 Perfil profissional do desenvolvedor

## 🛠 Tecnologias Utilizadas

### Backend (Servidor)
- **Node.js** - Runtime JavaScript
- **TypeScript** - Superset tipado do JavaScript
- **Express.js** - Framework web para Node.js
- **WPPConnect** - Biblioteca para integração WhatsApp
- **Swagger** - Documentação da API
- **Jest** - Framework de testes
- **Docker** - Containerização

### Bot
- **Python 3.x** - Linguagem de programação
- **Flask** - Microframework web para Python
- **Requests** - Biblioteca HTTP para Python

### Outros
- **Docker Compose** - Orquestração de containers
- **Nodemon** - Monitoramento de mudanças em desenvolvimento

## 📋 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

- [Node.js](https://nodejs.org/) (versão 22 ou superior)
- [Python](https://www.python.org/) (versão 3.8 ou superior)
- [Docker](https://www.docker.com/) (opcional, para execução em containers)
- [Git](https://git-scm.com/) (para clonar o repositório)

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/JoseSilva84/chatbot-teste.git
cd wppconnect-server-bot
```

### 2. Instale as dependências do servidor
```bash
cd wppconnect-server
npm install
```

### 3. Instale as dependências do bot
```bash
cd ../whatsapp-bot-python
pip install flask requests
```

### 4. (Opcional) Usando Docker
```bash
# Na raiz do projeto
docker-compose up --build
```

## ⚙️ Configuração

### Servidor WPPConnect

1. **Arquivo de configuração**: Edite `wppconnect-server/src/config.ts`
2. **Tokens**: Configure suas chaves de API em `wppconnect-server/src/config.ts`
3. **Porta**: O servidor roda na porta 21465 por padrão

### Bot Python

1. **Arquivo de configuração**: Edite `whatsapp-bot-python/bot.py`
2. **Tokens de API**:
   - `API_KEY`: Token global da API
   - `SESSION_TOKEN`: Token da sessão WhatsApp
   - `SESSION_NAME`: Nome da sessão (ex: "carlos")
3. **URLs**: Ajuste `BASE_URL` se necessário

## 🎮 Uso

### Iniciando o Servidor

```bash
cd wppconnect-server
npm run dev
```

Ler o qrcode gerado pela api

O servidor estará disponível em: `http://localhost:21465`

### Iniciando o Bot

```bash
cd whatsapp-bot-python
python bot.py
```

O bot estará disponível em: `http://localhost:5000`

### Primeiro Uso

1. **Conecte o WhatsApp**:
   - Acesse `http://localhost:21465` no navegador
   - Escaneie o QR code com seu WhatsApp
   - Aguarde a conexão ser estabelecida

2. **Configure o Webhook**:
   - No painel do WPPConnect, configure o webhook para: `http://localhost:5000/webhook`
   - Leia a documentação da wppconnect-server: [Click aqui](https://github.com/wppconnect-team/wppconnect-server)

3. **Teste o Bot**:
   - Envie uma mensagem para o número conectado
   - Digite "menu" ou "oi" para ver as opções

## 📁 Estrutura do Projeto

```
wppconnect-server-api/
├── whatsapp-bot-python/
│   └── bot.py                 # Bot Flask em Python
├── wppconnect-server/
│   ├── src/
│   │   ├── config.ts          # Configurações do servidor
│   │   ├── index.ts           # Ponto de entrada
│   │   ├── server.ts          # Servidor Express
│   │   ├── swagger.ts         # Documentação API
│   │   ├── config/
│   │   │   └── upload.ts      # Config upload
│   │   ├── controller/        # Controladores da API
│   │   │   ├── messageController.ts
│   │   │   ├── sessionController.ts
│   │   │   └── ...
│   │   ├── mapper/            # Mapeadores de dados
│   │   ├── middleware/        # Middlewares
│   │   ├── routes/            # Rotas da API
│   │   ├── types/             # Tipos TypeScript
│   │   └── util/              # Utilitários
│   ├── tests/                 # Testes
│   ├── tokens/                # Tokens de sessão
│   ├── uploads/               # Arquivos enviados
│   ├── userDataDir/           # Dados do navegador
│   ├── WhatsAppImages/        # Imagens do WhatsApp
│   ├── wppconnect_tokens/     # Tokens WPPConnect
│   ├── package.json           # Dependências Node.js
│   ├── tsconfig.json          # Config TypeScript
│   ├── Dockerfile             # Docker do servidor
│   └── docker-compose.yml     # Orquestração
├── README.md                  # Este arquivo
└── .gitignore                 # Arquivos ignorados
```

## 🔗 API Endpoints

### Principais Endpoints

- `GET /api/{session}/status` - Status da sessão
- `POST /api/{session}/send-message` - Enviar mensagem
- `GET /api/{session}/contacts` - Listar contatos
- `GET /api/{session}/chats` - Listar conversas

### Documentação Completa

Acesse `http://localhost:21465/api-docs` para ver a documentação Swagger completa.

## 🪝 Webhook

O bot utiliza webhooks para receber mensagens em tempo real. Configure o webhook no painel do WPPConnect para apontar para `http://localhost:5000/webhook`.

### Estrutura do Payload

```json
{
  "event": "onmessage",
  "from": "5511999999999@c.us",
  "body": "Olá",
  "fromMe": false,
  "timestamp": 1640995200
}
```

## 🧪 Testes

### Servidor
```bash
cd wppconnect-server
npm test
```

### Bot
```bash
cd whatsapp-bot-python
python -m pytest  # Se houver testes
```

## 🤝 Contribuição

Contribuições são bem-vindas! Siga estes passos:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

**José Silva** - Desenvolvedor Web

- LinkedIn: [LinkedIn](https://www.linkedin.com/in/jos%C3%A9-silva-dev/)
- Email: juniornyanata@gmail.com
- WhatsApp: +55 75 99245-6130

---

⭐ **Dê uma estrela se este projeto te ajudou!**

*Última atualização: Fevereiro 2026*
