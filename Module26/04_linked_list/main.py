class Node:
    """
    Узел списка, содержащий значение и ссылку на следующий узел.
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Односвязный список, состоящий из узлов Node.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """
        Представление списка в виде строки.
        """
        current = self.head
        output = '['
        while current is not None:
            output += str(current.value)
            current = current.next
            if current is not None:
                output += ' '
        output += ']'
        return output

    def append(self, value):
        """
        Добавление нового узла с заданным значением в конец списка.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def get(self, index):
        """
        Получение значения узла по заданному индексу.
        """
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def remove(self, index):
        """
        Удаление узла по заданному индексу.
        """
        if index < 0 or index >= self.length:
            raise IndexError("Индекс вне диапазона")
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        self.length -= 1

    def __iter__(self):
        """
        Итератор для прохода по списку.
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
