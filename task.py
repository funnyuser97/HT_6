# program by Stupka Bogdan

# Class for task 1-4


class Calc(object):
    """
        this class is just calculator
        for addition - obj.add(first_number, second_number)
        for subtraction - obj.sub(first_number, second_number)
        for multiplication - obj.mul(first_number, second_number)
        for division - obj.div(first_number, second_number)
    """

    last_result = None

    def add(self, first, second):
        self.last_result = first + second

    def sub(self, first, second):
        self.last_result = first - second

    def mul(self, first, second):
        self.last_result = first * second

    def div(self, first, second):
        self.last_result = first / second

# Class for task 5-6


class Person(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def show_age(self):
        print("Age :", self.age)

    def print_name(self):
        print ("Name :", self.first_name)

    def show_all_information(self):
        print("First_name :", self.first_name)
        print("Second_name :", self.last_name)
        print("Age :", self.age)

# Classes for task 7
class figure1(object):

    color = "white"

    def change_color(self, color):
        self.color = color


class oval1(figure1):
    def __init__(self, height, width):
        self.height = height
        self.width = width


class square1(figure1):
    def __init__(self, height, width):
        self.height = height
        self.width = width

# Classes for task 8


class figure(object):
    def __init__(self, color="white"):
        self.color = color

    def change_color(self, color):
        self.color = color


class oval(figure):
    def __init__(self, color,  height, width):

        figure.__init__(self, color)
        self.height = height
        self.width = width


class square(figure):
    def __init__(self, color, height, width):
        figure.__init__(self, color)
        self.height = height
        self.width = width

# Class for task 9


class user(object):
    """
        this class registration student in library
        method take_book addition record to list book about book
        method return_book subtraction record from list book about book
        method print_all_inf output all information about student and about
            books, which take student
    """

    list_book = []

    def __init__(self, name, l_name, email, age):
        self.name = name
        self.l_name = l_name
        self.email = email
        self.age = age

    def take_book(self, author, name_book):
        user.list_book.append({"Author": author, "Name_book": name_book})

    def take_book(self, author, name_book):
        user.list_book.append({"Author": author, "Name_book": name_book})

    def return_book(self, author, name_book):
        if {"Author": author, "Name_book": name_book} in user.list_book:
            user.list_book.remove({"Author": author, "Name_book": name_book})

    def print_all_inf(self):
        print("Name :", self.name, " Last_name :", self.l_name, "Age :", self.age)
        for item in user.list_book:
            print("Author :", item["Author"], "Name_book :", item["Name_book"])

# Class for task 11


class count_instance(object):

    count = 0

    def __init__(self):
        count_instance.count += 1

# Classes for task 10


class change_class_1(object):

    count = 0

    def __init__(self):
        count_instance.count += 1


class change_class_2(object):

    count = 0

    def __init__(self):
        change_class_1.count += 2

# Class for task 12


class Thing(object):

    def __init__(self):
        print("init")

# Class for task 13


class Thing2(object):

    letters = "abc"

    def __init__(self):
        print("init")

# Class for task 14


class Thing3(object):

    letters = "xyz"

    def __init__(self):
        print("init")

# Class for task 15


class DefaultClass(object):

    name = "Vasya"
    symbol_number = len(name)

    def __init__(self):
        print("init")

# Class for task 16-17


class DefaultClass1(object):

    def __init__(self, name, l_name, age):
        self.name = name
        self.l_name = l_name
        self.age = age

    def print_info(self):
        print("Name :", self.name)
        print("L_name :", self.l_name)
        print("Age :", self.age)

# Classes for task 18


class Super_class(object):

    def __init__(self, name, l_name, age):
        self.name = name
        self.l_name = l_name
        self.age = age

    def print_info(self):
        print("Name :", self.name)
        print("L_name :", self.l_name)
        print("Age :", self.age)


class Subsidiary_class1(Super_class):

    def print_info(self):
        print("Name :", self.name)


class Subsidiary_class2(Subsidiary_class1):
    # add attribute profession to init superclass
    def __init__(self, name, l_name, age, profession):
        Super_class.__init__(self, name, l_name, age)
        self.profession = profession

    def print_info(self):
        print("Name :", self.name)
        print("Profession :", self.profession)


print("__________task_1-4______________\n")

calculator = Calc()
print(calculator.__doc__)
a = 10
b = 5
print("Last_result = ", calculator.last_result)
calculator.add(a, b)
print("Last_result = ", a, " + ", b, " = ", calculator.last_result)
calculator.sub(a, b)
print("Last_result = ", a, " - ", b, " = ", calculator.last_result)
calculator.mul(a, b)
print("Last_result = ", a, " * ", b, " = ", calculator.last_result)
calculator.div(a, b)
print("Last_result = ", a, " / ", b, " = ", calculator.last_result)

print("____________task_5-6____________\n")

maxim = Person("Max", "Piterson", 12)
ed = Person("Edward", "Piterson", 42)
maxim.profession = "proger"
ed.profession = "it"
maxim.show_all_information()
print("Profession :", maxim.profession)
print ("________________________\n")
ed.show_all_information()
print("Profession :", ed.profession)

print ("___________task_7_____________\n")

first1 = figure1()
print("Color figure1:", first1.color)

first_o1 = oval1(123, 123)
print("Color oval1:", first_o1.color)

first_sq1 = square1(123, 123)
first_sq1.change_color("red")
print("Color square1 :", first_sq1.color)

print ("___________task_8_____________\n")

first = figure()
print("Color figure:", first.color)

first_o = oval("red", 123, 123)
print("Color oval:", first_o.color)

first_sq = square("blue", 123, 123)
print("Color square :", first_sq.color)

print("___________task_9_____________\n")

ivan = user("Ivan", "Pupkin", "email", "21")
ivan.take_book("Dostoevskyi", "Idiot")
ivan.return_book("Dostoevskyi", "Idiot")
ivan.print_all_inf()

print("___________task_11_____________\n")

a = count_instance()
b = count_instance()
print("Amount of instance :", count_instance.count)

print("___________task_10_____________\n")

a = change_class_2()
print("Amount of instance :", change_class_1.count)
b = change_class_2()
print("Amount of instance :", change_class_1.count)
c = change_class_2()
print("Amount of instance :", change_class_1.count)

print("___________task_12_____________\n")

example = Thing()
print("type Thing: ", type(Thing), "\ntype example: ", type(example))

print("____________task_13____________\n")

print("Letters : ", Thing2.letters)

print("____________task_14____________\n")

print("Letters : ", Thing3.letters)

print("____________task_15____________\n")

print("Name :", DefaultClass.name, "\nSymbol_number :", DefaultClass.symbol_number)

print("____________task_16-17____________\n")

vasya = {"name": "Vasya", "l_name": "Pupkin", "age": "20"}
user = DefaultClass1(vasya["name"], vasya["l_name"], vasya["age"])
user.print_info()

print("____________task_18____________\n")

example1 = Super_class("John", "Fonder", "12")
example1.print_info()
print("________________________\n")
example2 = Subsidiary_class2("John", "Fonder", "12", "Programmer")
example2.print_info()

print("________________________\n")
