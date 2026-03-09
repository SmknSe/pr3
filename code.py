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

# Словарь для десятков
TENS = {
    'двадцать': '20',
    'тридцать': '30',
    'сорок': '40',
    'пятьдесят': '50',
    'шестьдесят': '60',
    'семьдесят': '70',
    'восемьдесят': '80',
    'девяносто': '90'
}

# Словарь для сотен
HUNDREDS = {
    'сто': '100',
    'двести': '200',
    'триста': '300',
    'четыреста': '400',
    'пятьсот': '500',
    'шестьсот': '600',
    'семьсот': '700',
    'восемьсот': '800',
    'девятьсот': '900'
}

# Словарь для разрядов (тысячи, миллионы)
ORDERS = {
    'тысяча': '1000', 'тысячи': '1000', 'тысяч': '1000',
    'миллион': '1000000', 'миллиона': '1000000', 'миллионов': '1000000'
}

def convert_simple_number(words):
    """Преобразование простого числа (до 999)"""
    if not words:
        return ""
    
    total = 0
    for word in words:
        if word in HUNDREDS:
            total += int(HUNDREDS[word])
        elif word in TENS:
            total += int(TENS[word])
        elif word in NUMBERS_1_19:
            total += int(NUMBERS_1_19[word])
    
    return str(total) if total > 0 else ""

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
        
        # Тест преобразования
        test_words = ["сто", "одиннадцать"]
        result = convert_simple_number(test_words)
        print(f"\nТест преобразования 'сто одиннадцать': {result}")
    else:
        test_text = "сто одиннадцать тысяч фиолетовых оленей"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(test_text)
        print(f"Создан тестовый файл {filename}")

if __name__ == "__main__":
    main()