class ScheduleObserver:
    def update(self, message):
        raise NotImplementedError

class Student(ScheduleObserver):
    def update(self, message):
        print(f"Студент уведомлен: {message}")

class Teacher(ScheduleObserver):
    def update(self, message):
        print(f"Преподаватель уведомлен: {message}")

class ScheduleNotifier:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for observer in self.observers:
            observer.update(message)


schedule = ScheduleNotifier()
schedule.add_observer(Teacher())
schedule.add_observer(Student())

schedule.notify("Курица")
