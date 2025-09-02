import sqlite3
from contextlib import closing

DB_PATH = "app.db"  # Caminho do arquivo do banco de dados SQLite

def get_conn():
    """Abre conexão com o banco SQLite"""
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas como dicionário
    return conn

def init_db(schema_path="db/schema/videos.sql"):
    """Inicializa o banco de dados usando o script SQL"""
    with open(schema_path, "r", encoding="utf-8") as f, closing(get_conn()) as conn:
        conn.executescript(f.read())
        conn.commit()

def insert_video(data: dict):
    """Insere um novo vídeo no banco"""
    cols = ", ".join(data.keys())
    placeholders = ", ".join([":" + k for k in data.keys()])
    sql = f"INSERT INTO videos ({cols}) VALUES ({placeholders})"
    with closing(get_conn()) as conn, conn:
        conn.execute(sql, data)

def list_videos(limit=50, offset=0, filter_value=None):
    """Lista vídeos com paginação e filtro opcional"""
    base = "SELECT * FROM videos"
    params = {"limit": limit, "offset": offset}

    if filter_value:
        base += " WHERE filter LIKE :filter_value"
        params["filter_value"] = f"%{filter_value}%"

    base += " ORDER BY datetime(created_at) DESC LIMIT :limit OFFSET :offset"

    with closing(get_conn()) as conn:
        cur = conn.execute(base, params)
        return [dict(row) for row in cur.fetchall()]

def get_video(video_id: str):
    """Busca um vídeo pelo ID"""
    with closing(get_conn()) as conn:
        cur = conn.execute("SELECT * FROM videos WHERE id = :id", {"id": video_id})
        row = cur.fetchone()
        return dict(row) if row else None

def mark_video_deleted(video_id: str):
    """Marca um vídeo como 'trash'"""
    with closing(get_conn()) as conn, conn:
        conn.execute("UPDATE videos SET filter = 'trash' WHERE id = :id", {"id": video_id})
