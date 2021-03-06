from abc import ABC, abstractmethod
import time


class AbstractWorker(ABC):
    @abstractmethod
    def work(self):
        raise NotImplementedError()


class EatMixin(ABC):
    @abstractmethod
    def eat(self):
        raise NotImplementedError()


class Worker(AbstractWorker, EatMixin):

    def work(self):
        print("I'm normal worker_lab. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(AbstractWorker, EatMixin):

    def work(self):
        print("I'm super worker_lab. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWorker), "`worker_lab` must be of type {}".format(AbstractWorker)

        self.worker = worker


class WorkManager(Manager):
    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def lunch_break(self):
        self.worker.eat()


class Robot(AbstractWorker):
    def work(self):
        print("I'm a robot. I'm working....")



robot = Robot()
print(robot.eat())


# Може би eat да не е abstracten в бащиния клас. Също може да се създадат два отделни класа, един абстрактен с work и втори наследяващ първия и разширяващ с eat

