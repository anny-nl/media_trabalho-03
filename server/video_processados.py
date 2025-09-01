
import cv2
import os
import argparse

def aplicar_filtro(video_path: str, filtro: str, output_path: str):
    """
    Aplica um filtro ao vídeo e salva em output_path.
    Filtros: 'grayscale', 'pixelizar', 'bordas'
    Retorna: caminho do arquivo de saída.
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Não foi possível abrir o vídeo: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height), isColor=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if filtro == "grayscale":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)  # mantém 3 canais
        elif filtro == "pixelizar":
            h, w = frame.shape[:2]
            # evita dividir por zero em vídeos muito pequenos
            fx = max(1, w // 16)
            fy = max(1, h // 16)
            temp = cv2.resize(frame, (fx, fy), interpolation=cv2.INTER_LINEAR)
            frame = cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)
        elif filtro == "bordas":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, 100, 200)
            frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        else:
            cap.release()
            out.release()
            raise ValueError("Filtro inválido. Use: 'grayscale', 'pixelizar' ou 'bordas'.")

        out.write(frame)

    cap.release()
    out.release()
    return output_path


def gerar_thumbnail(video_path: str, thumb_path: str):
    """Salva o primeiro frame como thumbnail (JPG) e retorna o caminho."""
    cap = cv2.VideoCapture(video_path)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        raise RuntimeError("Não foi possível ler um frame do vídeo para gerar thumbnail.")

    os.makedirs(os.path.dirname(thumb_path), exist_ok=True)
    cv2.imwrite(thumb_path, frame)
    return thumb_path


def extrair_metadados(video_path: str):
    """
    Retorna dict com: duration_sec, fps, width, height, size_bytes
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Não foi possível abrir o vídeo: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
    frames = cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 0)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 0)
    cap.release()

    duration = float(frames / fps) if fps > 0 else None
    size_bytes = os.path.getsize(video_path) if os.path.exists(video_path) else None

    return {
        "duration_sec": duration,
        "fps": float(fps) if fps else None,
        "width": width,
        "height": height,
        "size_bytes": size_bytes,
    }



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processar vídeo com filtros OpenCV")
    parser.add_argument("--input", required=True, help="Caminho do vídeo de entrada")
    parser.add_argument("--filtro", required=True, choices=["grayscale", "pixelizar", "bordas"])
    parser.add_argument("--saida", required=True, help="Caminho do vídeo processado (mp4)")
    parser.add_argument("--thumb", help="Caminho para salvar a thumbnail (jpg)")
    args = parser.parse_args()

    saida = aplicar_filtro(args.input, args.filtro, args.saida)
    print("Vídeo processado em:", saida)

    if args.thumb:
        thumb = gerar_thumbnail(saida, args.thumb)
        print("Thumbnail gerada em:", thumb)

    meta = extrair_metadados(args.input)
    print("Metadados do original:", meta)
