# media_trabalho-03

# Este projeto implementa um sistema cliente/servidor em três camadas capaz de enviar, processar e armazenar vídeos de forma organizada.

Camadas:

Cliente (Tkinter) → envia vídeo para o servidor e visualiza resultados.

Servidor (Flask + OpenCV) → recebe, processa e organiza vídeos.

Banco de Dados (SQLite) → guarda os metadados dos vídeos.

#Estrutura de Pasta

/projeto/
│── client/                     # Cliente Tkinter
│── server/                     # Servidor Flask
│   ├── app.py                  # Flask principal
│   ├── db.py                   # Banco SQLite
│   ├── videos.sql              # Schema SQL
│   ├── video_processados.py    # Processamento de vídeos (OpenCV)
│   ├── armazenamento.py        # Organização de pastas + meta.json
│── media/                      # Onde ficam os vídeos
│── tests/                      # Scripts de teste
│   ├── test_db.py


