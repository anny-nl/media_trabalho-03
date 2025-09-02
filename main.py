from server import init_db, insert_video, list_videos, get_video, mark_video_deleted
import uuid

def main():
    print("🔧 Inicializando banco de dados...")
    init_db("server/videos.sql")

    # Gerar ID único
    video_id = str(uuid.uuid4())

    # Dados fictícios
    video_data = {
        "id": video_id,
        "original_name": "demo_video",
        "original_ext": "mp4",
        "mime_type": "video/mp4",
        "size_bytes": 1024000,
        "duration_sec": 45.0,
        "fps": 24.0,
        "width": 1280,
        "height": 720,
        "filter": "processed",
        "path_original": f"/media/original/{video_id}.mp4",
        "path_processed": f"/media/processed/{video_id}.mp4"
    }

    print("📥 Inserindo vídeo...")
    insert_video(video_data)

    print("🔍 Buscando vídeo por ID...")
    video = get_video(video_id)
    print(video)

    print("📋 Listando vídeos com filtro 'processed'...")
    for v in list_videos(limit=5, filter_value="processed"):
        print(v)

    print("🗑️ Marcando vídeo como 'trash'...")
    mark_video_deleted(video_id)

    print("🔁 Estado final do vídeo:")
    print(get_video(video_id))

if __name__ == "__main__":
    main()
