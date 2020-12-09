import xml.etree.ElementTree as ET
import os


class Memento(object):
    def __init__(self, tree):
        self._tree = tree

    def get_saved_state(self):
        return self._tree


class Originator(object):
    _tree = ET.ElementTree()

    def set(self, tree):
        self._tree = tree

    def createTag(self, tags):
        root = self._tree.getroot()
        for key, data in tags.items():
            attrib = data['attr']
            element = root.makeelement(key, attrib)
            element.text = data['text']
            root.append(element)
        return tree

    def save_to_memento(self):
        return Memento(self._tree)

    def restore_from_memento(self, memento):
        self._tree = memento.get_saved_state()


if __name__ == "__main__":
    print("Выберете один из типов xml документа:\n", "1. Досуг\n", "2. Праздник\n", "3. Утренник\n")
    typexml = input("Ввод: ")
    if typexml == '1':
        namexml = 'dosug.xml'
        path = os.path.abspath(os.curdir) + os.path.sep + 'Досуг' + os.path.sep + namexml
    elif typexml == '2':
        namexml = 'prazdnik.xml'
        path = os.path.abspath(os.curdir) + os.path.sep + 'Праздник' + os.path.sep + namexml
    elif typexml == '3':
        namexml = 'utrennik.xml'
        path = os.path.abspath(os.curdir) + os.path.sep + 'Утренник' + os.path.sep + namexml

    print("\nПолучаем дерево из xml документа")
    tree = ET.parse(path)
    print("\nСоздаем список состояний Memento")
    saved_states = []
    print("\nИнициализируем класс Originator")
    originator = Originator()
    print("\nПрисваеваем ему наше полученное дерево")
    originator.set(tree)
    print("\nСохраняем наше дерево в список состояний Memento")
    saved_states.append(originator.save_to_memento())
    print("\nСохраняемый объект: ", saved_states[0])
    obj1 = originator._tree
    print("\nХранимое дерево в объекте: ", originator._tree)
    newtags = {'newTag': {
        'text': 'sometext',
        'attr': {
            'color': 'green'
        }
    }
    }
    print(f"\nСоздём новый тег в виде списка {newtags}")

    print("\nДобавляем в дерево новый тег")
    originator.set(originator.createTag(newtags))
    print("\nСохраняем наше дерево в список состояний Memento")
    saved_states.append(originator.save_to_memento())
    print("\nСохраняемый объект: ", saved_states[-1])
    obj2 = originator._tree
    print("\nХранимое дерево в объекте: ", originator._tree)
    print("\nВозвращаем нашему объекту Originator начальное состояние")
    originator.restore_from_memento(saved_states[0])
    obj3 = originator._tree
    print("\nХранимое дерево в объекте: ", originator._tree)
    print("\nСравним деревья изначального объекта и возвращенного к начальному состоянию\n")
    print(obj1 == obj3)
    print("\nЕсли видим 'True', значит объект успешно вернулся к исходному состоянию")