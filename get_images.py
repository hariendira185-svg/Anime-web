import requests

anime_titles = [
    "Naruto",
    "Attack on Titan",
    "Death Note",
    "My Hero Academia",
    "Fullmetal Alchemist: Brotherhood",
    "One Punch Man"
]

urls = []
for title in anime_titles:
    resp = requests.get(f"https://api.jikan.moe/v4/anime?q={title}&limit=1")
    if resp.status_code == 200:
        data = resp.json()
        if data['data']:
            img_url = data['data'][0]['images']['jpg']['large_image_url']
            print(f"{title}: {img_url}")
            urls.append(img_url)
    import time
    time.sleep(1) # rate limit
