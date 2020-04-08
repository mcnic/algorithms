#from deque import Deque
from deque2 import Deque


class Polyndrome:

    def check(self, str):
        # fill
        deque = Deque()
        for ch in str:
            deque.addTail(ch)

        # check
        iter = deque.size() // 2    # get middle
        while iter > 0:
            if deque.removeFront() != deque.removeTail():
                return False
            iter -= 1
        return True
