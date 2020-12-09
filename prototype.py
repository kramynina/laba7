import xml.etree.ElementTree as ET
from abc import abstractmethod, ABC
from copy import deepcopy
from xml.dom.minidom import parse
import xml.dom.minidom
import os

class Cloneable(ABC):
    @abstractmethod
    def clone(self):
        pass


class Prototype(Cloneable):
    def __init__(self, ETobject):
        self.obj = ETobject

    def clone(self):
        return Prototype(self.obj)

    def createTag(self, tree, tag):
        root = tree.getroot()
        for k,v in tag.items():
            # добавляем элемент к корневому узлу
            attrib = v['attr']
            element = root.makeelement(k,  attrib)
            if k == 'text':
                element.text = v['text']
            root.append(element)
        return root

    def writeXML(self, obj, name):
        mydata = ET.tostring(obj)
        myfile = open(name, "wb")
        myfile.write(mydata)


if __name__ == "__main__":
    print("Выберете один из типов xml документа:\n","1. Досуг\n","2. Праздник\n","3. Утренник\n")
    typexml = input("Ввод: ")
    if typexml == '1':
        namexml = 'dosug.xml'
        path = os.path.abspath(os.curdir) + os.path.sep + 'Досуг' + os.path.sep
        tree = ET.parse(path+namexml)
        doc = Prototype(tree)
    elif typexml == '2':
        namexml = 'prazdnik.xml'
        path = os.path.abspath(os.curdir) + os.path.sep + 'Праздник' + os.path.sep
        tree = ET.parse(path + namexml)
        doc = Prototype(tree)
    elif typexml == '3':
        namexml = 'utrennik.xml'
        path = os.path.abspath(os.curdir) + os.path.sep + 'Утренник' + os.path.sep
        tree = ET.parse(path + namexml)
        doc = Prototype(tree)

    doc1 = doc.clone()
    print("\nСравним содержимое исходного объекта с клоном: \n")
    print(doc.obj == doc1.obj)
    print("\nВидим 'True', значит содержимое объектов совпадает.")
    print("\nТеперь в клон добавим тег и сравним снова.\n")
    newtags = {
               'newElem': {
                          'text': 'blabla',
                          'attr': {
                                  'name': 'heh'
                                  },
                          }
              }
    print(f"Введенный тег в виде списка: {newtags}\n")
    doc1.obj = doc1.createTag(doc1.obj, newtags)
    print(doc.obj == doc1.obj)
    print("\nВидим значение 'False', получается что содержимое объектов разное.\n")
    print("Присвоим клону содержимое исходного объекта, тем самым вернем его в исходное состояние.\n")
    doc1.obj = doc.obj
    print("Сравним содержимое исходного объекта с клоном: \n")
    print(doc.obj == doc1.obj)
    print("\nВидим 'True', значит содержимое объектов совпадает.\n")
