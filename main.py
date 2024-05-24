from random import randint

#Сложность 0 - 1
mode = 0.8

def write_to_file(data: list) -> None:
    with open("dict.txt", "a", encoding="utf-8") as file:
        data = helper_1(data)
        print(data)
        write_data = "\n".join(data)
        file.write('\n' + write_data)

def get_data_from_file() -> list:
    with open("dict.txt", "r", encoding="utf-8") as file:
        data = file.read()
        data = data.split('\n')
        data = helper_2(data[1:])
    return data

def clear_file() -> None:
    with open("dict.txt", "w", encoding="utf-8") as file:
        file.write("")

def helper_1(array: list) -> list:
    result = []
    for el in array:
        for word in el:
            result.append(word)
    return result

def helper_2(array: list) -> list:
    result = []
    for i in range(len(array) // 2):
        result.append([[], []])
        result[i][0] = array[i*2]
        result[i][1] = array[i*2 + 1]
    return result

def helper_3(ref_word: str, word: str) -> int:
    scope = 0
    for char in word:
        if char in ref_word:
            scope += 1
    return scope / len(ref_word)

print("Это простая программа для запоминания слов")

while True:
    x = input("\n1) Начать обучение\n"
          "2) Расширить словарь\n"
          "3) Сократить словарь\n"
          "4) Выход\n")
    if x == "1":
        words = get_data_from_file()
        usage = []
        print("\nСейчас вам будет предложенно правильно ввести представленные слова\nЧтобы прекратить обучение введите - выход")
        while True:
            if len(usage) == len(words):
                usage = []
            while True:
                x = randint(0, len(words) - 1)
                if x not in usage:
                    break
            usage.append(x)
            inp = input(f" > {words[x][0]}\n < ")
            if inp.lower() == "выход":
                break
            else:
                result = helper_3(words[x][1], inp)
                if result > mode:
                    print(f"Правильно! - {words[x][1]}")
                else:
                    print(f"Неправильно - {words[x][1]}")
    elif x == "2":
        words = []
        print("\nВводите пары слов по типу: слово с пропущенной буквой, слово с вставленной буквой.\nНапример < Выкач*нная бочка, Выкачанная бочка\nЧтобы прекратить введите - выход")
        while True:
            x = input(" < ")
            if x.lower() == "выход":
                break
            else:
                words.append(x.split(","))
        x = input("\nВы желаете добавить в список слов эти слова: " + str(words) + " (Д/н): ")
        if x.lower() == 'д' or x.lower() == "да":
            write_to_file(words)
    elif x == "3":
        words = get_data_from_file()
        print("\nВыберите из списка слова, которые следует удалить: ")
        for word in words:
            print(f"{words.index(word) + 1}) {word}")
        inp = input(" < ")
        words.remove(words[int(inp) - 1])
        clear_file()
        write_to_file(words)
    elif x == "4":
        break
    