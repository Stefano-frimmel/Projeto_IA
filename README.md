# Chatbot IA estilo Gemini/ChatGPT

Este projeto é um exemplo simples de chatbot IA usando FastAPI (backend) e um modelo open-source (Llama 2 ou similar) via Hugging Face Transformers. Inclui um frontend HTML/JS para interação.

## Como rodar o backend

1. Instale as dependências:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
2. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

> O download do modelo pode demorar na primeira execução.

## Como rodar o frontend

Abra o arquivo `frontend/index.html` no navegador.

## Observações
- O backend roda por padrão em http://localhost:8000
- O frontend faz requisições para o backend via API REST.
- Você pode trocar o modelo no backend por outro disponível no Hugging Face.

---

Projeto inicial para estudos de IA conversacional.
