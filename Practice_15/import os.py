import os
import zipfile
from collections import Counter

# Шляхи до архіву і розпакованих файлів
archive_path = r'C:\Users\Nestors\Desktop\python-practice-km-41-2-ValyaTkachenko\Practice_15\archive.zip'
extract_path = r'C:\Users\Nestors\Desktop\python-practice-km-41-2-ValyaTkachenko\Practice_15\extracted_files'

# Розпаковуємо архів, якщо ще не розпакований
if not os.path.exists(extract_path):
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

# Ініціалізація лічильників для імен
male_counts = Counter()
female_counts = Counter()

# Обробка кожного txt-файлу в розпакованій папці
for file_name in sorted(os.listdir(extract_path)):
    if file_name.endswith('.txt'):  # Обробляємо лише txt-файли
        file_path = os.path.join(extract_path, file_name)
        
        # Читання файлу
        with open(file_path, 'r') as file:
            for line in file:
                name, sex, count = line.strip().split(",")
                count = int(count)
                
                if sex == "M":
                    male_counts[name] += count
                elif sex == "F":
                    female_counts[name] += count

# Виведення результатів
print("Перші 5 чоловічих імен за частотою:")
for name, count in male_counts.most_common(5):
    print(f"{name}: {count}")

print("\nОстанні 5 чоловічих імен за частотою:")
for name, count in male_counts.most_common()[-5:]:
    print(f"{name}: {count}")

print("\nПерші 5 жіночих імен за частотою:")
for name, count in female_counts.most_common(5):
    print(f"{name}: {count}")

print("\nОстанні 5 жіночих імен за частотою:")
for name, count in female_counts.most_common()[-5:]:
    print(f"{name}: {count}")

