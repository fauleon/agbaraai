# Agbara

Landing page em Flask para a Agbara, com foco em chatbot premium para vendas,
atendimento e automacao conversacional.

## Estrutura

```text
agbara/
├── app.py
├── requirements.txt
├── run.bat
├── static/
│   ├── css/
│   └── img/
└── templates/
```

## Rodar localmente

Instale o Python 3.11+ e rode:

```powershell
python -m pip install -r requirements.txt
python app.py
```

Depois acesse:

```text
http://127.0.0.1:5000
```

Tambem da para executar o arquivo `run.bat`.

## Deploy

Este projeto e uma aplicacao Flask. Para publicar, use uma plataforma com suporte
a Python, como Render, Railway, Fly.io, VPS ou similar.
