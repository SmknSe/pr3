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
    'тысяча': 1000, 'тысячи': 1000, 'тысяч': 1000,
    'миллион': 1000000, 'миллиона': 1000000, 'миллионов': 1000000
}

def is_number_word(word):
    """Проверка, является ли слово числительным"""
    return (word in NUMBERS_1_19 or word in TENS or 
            word in HUNDREDS or word in ORDERS)

def convert_number_group(words):
    """Преобразование группы слов в число"""
    if not words:
        return 0
    
    total = 0
    for word in words:
        if word in HUNDREDS:
            total += int(HUNDREDS[word])
        elif word in TENS:
            total += int(TENS[word])
        elif word in NUMBERS_1_19:
            total += int(NUMBERS_1_19[word])
    
    return total

def process_text(text):
    """Основная функция обработки текста"""
    words = text.split()
    result = []
    i = 0
    
    while i < len(words):
        if is_number_word(words[i]):
            # Начало числовой группы
            number_group = []
            current_order = 1
            total = 0
            
            # Собираем все слова числа
            while i < len(words) and is_number_word(words[i]):
                if words[i] in ORDERS:
                    # Встретили разряд (тысячи, миллионы)
                    group_value = convert_number_group(number_group)
                    total += group_value * ORDERS[words[i]]
                    number_group = []
                else:
                    number_group.append(words[i])
                i += 1
            
            # Обрабатываем остаток числа
            if number_group:
                total += convert_number_group(number_group)
            
            result.append(str(total))
        else:
            result.append(words[i])
            i += 1
    
    return ' '.join(result)

def read_file(filename):
    """Чтение текста из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None

def write_file(filename, text):
    """Запись текста в файл"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def main():
    input_filename = "input.txt"
    output_filename = "output.txt"
    
    text = read_file(input_filename)
    
    if text:
        print("Исходный текст:")
        print(text)
        
        # Обрабатываем текст
        processed_text = process_text(text)
        
        print("\nОбработанный текст:")
        print(processed_text)
        
        # Сохраняем результат
        write_file(output_filename, processed_text)
        print(f"\nРезультат сохранен в файл {output_filename}")
    else:
        # Создаем тестовый файл
        test_text = "сто одиннадцать тысяч фиолетовых оленей"
        write_file(input_filename, test_text)
        print(f"Создан тестовый файл {input_filename}")

if __name__ == "__main__":
    main()