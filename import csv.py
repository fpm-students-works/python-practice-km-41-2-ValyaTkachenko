import os
import zipfile
import json

# Шлях до архіву
zip_path = r"C:\\Users\\Nestors\\Desktop\\python-practice-km-41-2-ValyaTkachenko\\image_info_test2017.zip"

# Перевірка та розпаковка архіву
if not os.path.exists(zip_path):
    raise FileNotFoundError(f"Файл {zip_path} не знайдено.")
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(os.path.dirname(zip_path))

# Завантаження JSON-файлу
json_path = os.path.join(os.path.dirname(zip_path), 'annotations', 'image_info_test-dev2017.json')
if not os.path.exists(json_path):
    raise FileNotFoundError(f"JSON-файл {json_path} не знайдено.")
with open(json_path, 'r') as file:
    data = json.load(file)

# Отримання результатів
num_images = len(data.get("images", []))
num_categories = len(data.get("categories", []))
photo = next((img for img in data["images"] if img["file_name"] == "000000000001.jpg"), {})

# Виведення результатів
print(f"Кількість фотографій: {num_images}")
print(f"Кількість категорій: {num_categories}")
print(f"Посилання: {photo.get('coco_url', 'Не знайдено')}")
print(f"Розмір: {photo.get('height', 'N/A')}x{photo.get('width', 'N/A')}")
print(f"ID: {photo.get('id', 'Не знайдено')}")
print(f"Найбільший номер фото: {max(data['images'], key=lambda x: int(x['file_name'].split('.')[0]))['file_name']}")
