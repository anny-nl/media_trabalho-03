# Projeto: Gerenciador de Metadados de Vídeos

Este projeto tem como objetivo armazenar e gerenciar os metadados de vídeos processados, utilizando Python e SQLite. Ele faz parte do trabalho 03 da disciplina de Sistemas Distribuídos.

---

## Estrutura do Projeto



# Este projeto implementa um sistema cliente/servidor em três camadas capaz de enviar, processar e armazenar vídeos de forma organizada.

Camadas:

Cliente (Tkinter) → envia vídeo para o servidor e visualiza resultados.

Servidor (Flask + OpenCV) → recebe, processa e organiza vídeos.

Banco de Dados (SQLite) → guarda os metadados dos vídeos.

#Estrutura de Pasta

trabalho 03/ ├── .venv/ # Ambiente virtual ├── server/ # Lógica de banco de dados │ ├── init.py │ ├── database.py │ ├── videos.sql │ └── controller.py ├── tests/ # Testes automatizados │ └── teste_db.py ├── main.py # Script principal ├── app.db # Banco de dados gerado └── README.md # Este arquivo


---

## Requisitos

- Python 3.10 ou superior
- Git instalado
- SQLite (já incluído no Python via `sqlite3`)
- Ambiente virtual ativo (`.venv`)

---

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/anny-nl/media_trabalho-03.git
cd media_trabalho-03

#Ative o ambiente virtual
& ".venv/Scripts/Activate.ps1"

#Execute o script principal:
 python main.py

#Organização dos arquivos de vídeo
/media/
├── original/
├── processed/
└── trash/

