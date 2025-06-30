# 🤖 Chatbot IA estilo Gemini/ChatGPT

<img src="https://user-images.githubusercontent.com/25181517/266887956-1b5a5e7b-6b7e-4b2e-8b7e-2b7e6e6e6e6e.gif" width="100%" alt="Chatbot Animation"/>

Este projeto é um exemplo simples de chatbot IA usando FastAPI (backend) e um modelo open-source (Falcon 7B Instruct) via Hugging Face Transformers. Inclui um frontend HTML/JS para interação.

## Demonstração

![Demonstração do Chatbot](https://github.com/rocketseat-education/nlw-ia-2024-01/blob/main/.github/demo.gif?raw=true)

---

## Exemplo de uso

**Pergunta:**
```
Qual a capital da França?
```
**Resposta da IA:**
```
A capital da França é Paris.
```

---

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
