from threading import Thread, Event


class Handler(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.terminated = Event()

    def terminate(self):
        self.terminated.set()

    def revive(self):
        self.terminated.clear()

    def is_terminated(self):
        return self.terminated.is_set()
