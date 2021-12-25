class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min = 2**31

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self):
        """
        :rtype: None
        """
        if self.min == self.stack.pop(-1):
            self.min = 2**31
        for val in self.stack:
            if val < self.min:
                self.min = val

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
