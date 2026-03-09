def read_file(filename):
    """Чтение текста из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None

def main():
    # Тестовый файл
    filename = "input.txt"
    text = read_file(filename)
    
    if text:
        print("Исходный текст:")
        print(text)
    else:
        # Создадим тестовый файл, если его нет
        test_text = "сто одиннадцать тысяч фиолетовых оленей"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(test_text)
        print(f"Создан тестовый файл {filename}")

if __name__ == "__main__":
    main()