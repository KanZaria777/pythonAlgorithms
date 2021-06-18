"""
Задание 6.
Задание на закрепление навыков работы с очередью
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например,
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

# интерфейс стэка
class Queue:
    def __init__(self):
        """инициализация списка"""
        self.elems = []

    def is_empty(self):
        """очистка списка"""
        return self.elems == []

    def to_queue(self, item):
        """вставка в начало списка"""
        self.elems.insert(0, item)

    def from_queue(self):
        """удаление из списка"""
        return self.elems.pop()

    def size(self):
        """длина списка"""
        return len(self.elems)

class TaskBoard:
    def __init__(self):
        self.cur_queue = Queue()  # Задачи
        self.revision_queue = Queue()  # Необходимые доработать
        self.log = []  # Решенные задачи

    def resolve_task(self):
        """Законченную задачу добавляем в лог"""
        # используем функцию ранее инициализированного класса
        task = self.cur_queue.from_queue()
        self.log.append(task)

    def to_revision_task(self):
        """
        немного сложно понять логику двух строк ниже...
        почему не тоже самое,но без присвоения
        self.cur_queue.from_queue()
        они обе по идее примут один аргумент, разве нет?
        Если верно, значит ли это что ниже представлен более зрелый вариант реализации?
        """
        task = self.cur_queue.from_queue()
        self.revision_queue.to_queue(task)

    def to_current_queue(self, item):
        """Добавляем задачу в текущие"""
        self.cur_queue.to_queue(item)

    def from_revision(self):
        """Возврат задачи с доработки в текущую"""
        # ощущение что должно быть два списка. Основной и доработки,иначе не ясно
        task = self.revision_queue.from_queue()
        self.cur_queue.to_queue(task)

    def current_task(self):
        """Текущая задача"""
        return self.cur_queue.elems[len(self.cur_queue.elems) - 1]

    def current_revision(self):
        """Задача в доработке"""
        return self.revision_queue.elems[len(self.revision_queue.elems) - 1]


if __name__ == '__main__':
    taskBoard = TaskBoard()
    taskBoard.to_current_queue('123')
    taskBoard.to_current_queue('1234')
    print(taskBoard.current_task())
    print(taskBoard.cur_queue.elems)
    taskBoard.to_revision_task()
    taskBoard.resolve_task()
    taskBoard.from_revision()
    print(taskBoard.cur_queue.elems)
    print(taskBoard.current_task())
    print(taskBoard.log)