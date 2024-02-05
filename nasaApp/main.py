import requests
import os

def download_mars_photos(api_key, sol, camera, save_path):
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    
    params = {
        'sol': sol,         # номер сола (дня) на Марсе
        'camera': camera,   # камера ровера
        'api_key': api_key  # ваш API-ключ NASA
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        photos = data['photos']

        if not os.path.exists(save_path):
            os.makedirs(save_path)

        for photo in photos:
            img_url = photo['img_src']
            img_name = os.path.join(save_path, f"{photo['id']}.jpg")

            img_data = requests.get(img_url).content
            with open(img_name, 'wb') as img_file:
                img_file.write(img_data)
                
            print(f"Сохранено: {img_name}")

    else:
        print(f"Ошибка при получении данных: {response.status_code}")

if __name__ == "__main__":
    api_key = "kxeQwOfrl7pWjiXKPIQmDbBf9draucQVIjKh9cRg"
    sol = 1000
    camera = "FHAZ"
    save_path = "nasaApp\mars_photos"

    download_mars_photos(api_key, sol, camera, save_path)
