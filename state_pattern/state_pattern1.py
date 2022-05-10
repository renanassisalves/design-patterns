from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    @abstractmethod
    def manipular(self):
        pass

class StateConcretaA(State):
    def manipular(self):
        print("State concretaA")

class StateConcretaB(State):
    def manipular(self):
        print("State concretaB")

class Context(State):
    def __init__(self):
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def manipular(self):
        self.state.manipular()

context = Context()
state_a = StateConcretaA()
state_b = StateConcretaB()

context.set_state(state_a)
context.manipular()

context.set_state(state_b)
context.manipular()