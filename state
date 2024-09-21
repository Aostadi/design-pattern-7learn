from abc import ABC, abstractmethod


class SentenceState(ABC):
    @abstractmethod
    def print_sentence(self, s):
        pass


class NormalState(SentenceState):
    def print_sentence(self, s):
        print(f"normal: {s}")


class ReverseState(SentenceState):
    def print_sentence(self, s):
        print(f" reversed: {s[::-1]}")


class SentenceContext:
    def __init__(self, state: SentenceState):
        self.state = state

    def print_sentence(self, sentence):
        self.state.print_sentence(sentence)


sentence = input("enter your sentence: ")
choice = input("print type ('n' for normal and 'r' for reversed): ")
if choice == 'r':
    state = ReverseState()
    context = SentenceContext(state)
    context.print_sentence(sentence)
else:
    state = NormalState()
    context = SentenceContext(state)
    context.print_sentence(sentence)

