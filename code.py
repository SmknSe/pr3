# filename: text_processor.py

# Словарь для чисел от 0 до 19
NUMBERS_1_19 = {
    'ноль': '0',
    'один': '1', 'одна': '1',
    'два': '2', 'две': '2',
    'три': '3',
    'четыре': '4',
    'пять': '5',
    'шесть': '6',
    'семь': '7',
    'восемь': '8',
    'девять': '9',
    'десять': '10',
    'одиннадцать': '11',
    'двенадцать': '12',
    'тринадцать': '13',
    'четырнадцать': '14',
    'пятнадцать': '15',
    'шестнадцать': '16',
    'семнадцать': '17',
    'восемнадцать': '18',
    'девятнадцать': '19'
}

def read_file(filename):
    """Чтение текста из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None

def main():
    filename = "input.txt"
    text = read_file(filename)
    
    if text:
        print("Исходный текст:")
        print(text)
        print("\nСловарь чисел 1-19:")
        print(NUMBERS_1_19)
    else:
        test_text = "сто одиннадцать тысяч фиолетовых оленей"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(test_text)
        print(f"Создан тестовый файл {filename}")

if __name__ == "__main__":
    main()