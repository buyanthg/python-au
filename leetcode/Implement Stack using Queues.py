class MyStack(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack == []

