from db import init_db, insert_video, list_videos, get_video, mark_video_deleted
import uuid

# Inicializa o banco (executa o videos.sql)
init_db("db/schema/videos.sql")

# Gera um UUID único para o vídeo
video_id = str(uuid.uuid4())

# Dados fictícios para teste
video_data = {
    "id": video_id,
    "original_name": "teste_video",
    "original_ext": "mp4",
    "mime_type": "video/mp4",
    "size_bytes": 2048000,
    "duration_sec": 60.0,
    "fps": 30.0,
    "width": 1280,
    "height": 720,
    "filter": "processed",
    "path_original": f"/media/original/{video_id}.mp4",
    "path_processed": f"/media/processed/{video_id}.mp4"
}

# Insere o vídeo no banco
insert_video(video_data)
print("✅ Vídeo inserido com sucesso!")

# Consulta pelo ID
video = get_video(video_id)
print("🔍 Consulta por ID:")
print(video)

# Lista vídeos com filtro
videos = list_videos(limit=5, filter_value="processed")
print("📋 Lista de vídeos filtrados:")
for v in videos:
    print(v)

# Marca como excluído
mark_video_deleted(video_id)
print("🗑️ Vídeo marcado como 'trash'.")

# Verifica se foi atualizado
video_after = get_video(video_id)
print("🔁 Estado após exclusão lógica:")
print(video_after)
