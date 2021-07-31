from config import videos_urls
import requests

for video_url in videos_urls:
    r = requests.get(video_url, stream=True)
    file_name = r.headers.get('Content-Disposition').split("inline; filename=\"")[1][:-1]
    total_size = r.headers.get('content-length')
    print(file_name)
    with open(file_name, 'wb') as f:
        downloaded_chunks = 0
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)
                downloaded_chunks += len(chunk)
                print(end='\r')
                print(f'{int((downloaded_chunks / int(total_size)) * 100)}%', end='')
    print(end='\r')
    print("Downloaded")