class Queue:
    """initiating class"""
    def __init__(self):
        self.items = [] #создаем в классе своем в свое поле обьекту

    def enqueue(self, element):
        self.items.append(element)

    def dequeue(self):
        return self.items.pop(1)

    def head(self):
        if len(self.items) == 0:
            return None
        return self.items[0]

    def tail(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    """create class object"""
    queue_to_doctor = Queue()
    queue_to_bank = Queue()

    print(queue_to_doctor.size())
    queue_to_doctor.enqueue('Vasya') # element - Vasya
    queue_to_doctor.enqueue('Rahim')
    print(queue_to_doctor.size())
    print(queue_to_doctor.head())
    print(queue_to_doctor.tail())
    print(queue_to_doctor.dequeue())
    print(queue_to_doctor.size())