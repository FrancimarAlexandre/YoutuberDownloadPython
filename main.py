import yt_dlp

url = "https://youtu.be/YrQLmElRT-E?si=hyCcEmTn9c0EXoYV" # url (Tribo da Periferia - Imprevisível (Official Music Video))

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # força vídeo MP4 e áudio M4A
    'outtmpl': '%(title)s.%(ext)s',  # nome do arquivo = título do vídeo
    'merge_output_format': 'mp4',    # converte automaticamente para .mp4 se necessário
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
