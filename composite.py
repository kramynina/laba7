
class ChildElement:

    def __init__(self, *args):
        self.name = args[0]

    def printDetails(self):
        print("\t", end="")
        print(self.name)


class CompositeElement:

    def __init__(self, *args):
        self.name = args[0]
        self.children = []

    def appendChild(self, child):
        self.children.append(child)

    def removeChild(self, child):
        self.children.remove(child)

    def printDetails(self):
        print(self.name)
        for child in self.children:
            print("\t", end="")
            child.printDetails()


if __name__ == "__main__":
    print("\nСоздаем главную папку проекта, называем 'Project'\n")
    project = CompositeElement("Project")
    print("Создаем папки 'venv','DataBase','Picture','Templates' и файл 'composite.py'\n")
    sub1 = CompositeElement("venv")
    sub2 = CompositeElement("DataBase")
    sub3 = CompositeElement("Picture")
    sub4 = CompositeElement("Templates")
    projectsub = CompositeElement("composite.py")
    print("Для папки 'venv' создаем вложенные файлы, папку 'Include' и файл 'pyvenv.cfg'\n")
    sub11 = ChildElement("Include")
    sub12 = ChildElement("pyvenv.cfg")
    print("Для папки 'DataBase' создаем вложенные файлы, файл подключения 'Include' и файл копии базы 'dump.sql'\n")
    sub21 = ChildElement("connect.py")
    sub22 = ChildElement("dump.sql")
    print("Для папки 'Picture' создаем вложенные файлы, фото 'Me.png' и фото 'We.jpeg'\n")
    sub31 = ChildElement("Me.png")
    sub32 = ChildElement("We.jpeg")
    print("Для папки 'Templates' создаем вложенные файлы, файл 'main.html'\n")
    sub41 = ChildElement("main.html")
    print("Вкладываем наши файлы в папки\n")
    sub1.appendChild(sub11)
    sub1.appendChild(sub12)
    sub2.appendChild(sub21)
    sub2.appendChild(sub22)
    sub3.appendChild(sub31)
    sub3.appendChild(sub32)
    sub4.appendChild(sub41)
    print("Вкладываем наши полученные папки в главную папку проекта и файлы\n")
    project.appendChild(sub1)
    project.appendChild(sub2)
    project.appendChild(sub3)
    project.appendChild(sub4)
    project.appendChild(projectsub)
    print("Наша файловая система: \n")
    project.printDetails()
