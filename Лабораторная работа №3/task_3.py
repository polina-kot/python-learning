# TODO  Напишите функцию count_letters
def count_letters(text):
    letters_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower.isalpha():
            letters_dict[char_lower] = letters_dict.get(char_lower, 0) + 1
    return letters_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(letters_count):
    total_letters = sum(letters_count.values())
    frequency_dict = {}
    for letter, count in letters_count.items():
        frequency = count / total_letters
        frequency_dict[letter] = frequency
    return frequency_dict


def main():
    main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
    letters_count = count_letters(main_str)
    frequency_dict = calculate_frequency(letters_count)

    for letter, frequency in frequency_dict.items():
        rounded_frequency = round(frequency, 2)
        print(f"{letter}: {rounded_frequency:.2f}")

if __name__ == "__main__":
    main()

# TODO Распечатайте в столбик букву и её частоту в тексте
