import re
import requests
from bs4 import BeautifulSoup

def parse_trendyol_product(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.prettify()
    
        # Регулярное выражение для поиска словаря с ключом "images"
        pattern = r'"images":\["[^]]*"]'

        # Поиск совпадений
        matches = re.findall(pattern, content)

        # Проверка, нашлись ли совпадения
        if not matches:
            print("Словарь 'images' не найден.")
        else:
            # Извлечение URL-адресов из найденного фрагмента
            image_urls = re.findall(r'(?<=")/[^"]+', matches[0])

            # Базовый URL для добавления к каждой ссылке изображения
            base_url = "https://cdn.dsmcdn.com"

            # Полные URL-адреса изображений
            full_image_urls = [base_url + url for url in image_urls]

            # # Скачивание изображений
            # for i, url in enumerate(full_image_urls):
            #     response = requests.get(url)
            #     if response.status_code == 200:
            #         # Сохранение изображения в файл
            #         image_path = f'image_{i + 1}.jpg'
            #         with open(image_path, 'wb') as file:
            #             file.write(response.content)
            #         print(f"Изображение {i + 1} сохранено как {image_path}")
            #     else:
            #         print(f"Не удалось скачать изображение по адресу: {url}")
    return full_image_urls

# product_url = 'https://www.trendyol.com/hummel/nielsen-unisex-beyaz-ayakkabi-p-34967998?boutiqueId=61&merchantId=659677'
# parse_trendyol_product(product_url)
