import re
class Interpreter(object):
    def __init__(self):
        self.grammar = {
          'and': '&',
          'or': '|',
          'not': '~',
          }

    def interpret(self, text):
        for k,d in self.grammar.items():
            text = re.sub(k, d, text)
        return text


if __name__ == "__main__":
    print("Указываем путь к файлу\n")
    pathfile = input("Ввод:")

    print("\nСчитываем текст из файла\n")
    with open(pathfile, "r") as file:
        text = file.read()

    print("Содержимое файла:\n")

    print(f"{text}\n")

    print("Создаём объект Interpreter для змены операций\n")
    operation = Interpreter()

    print("Передаём в функцию интерпретатора полученный из файла текст\n")

    result_text = operation.interpret(text)

    print("Получаем следующий результат:\n")

    print(f"{result_text}\n")

    print("Создадим новый файл и запишем в него результат")

    with open('IntrepText.txt', 'w') as new_file:
        new_file.write(result_text)

    print("\nГотово")