class Converter():
    def __init__(self):
        with open('converted files/task.txt') as file:
            self.data = file.read()
        self.start_solution = self.data.find('python')
        self.res = ''

    def get_condition(self):
        condition = '#' + self.data[:self.start_solution] + "\n"
        self.res += condition

    def get_tests(self):
        with open('converted files/test.py', 'r') as file:
            test = "<details><summary>Test cases</summary><blockquote>\n\n```python\n"
            for line in file:
                test += line
        test += "\n```\n</blockquote></details>\n\n"
        self.res += test

    def get_solution(self):
        solution = "```" + self.data[self.start_solution:] + "\n```"
        self.res += solution

    def convert(self, file):
        file.write(self.res)


a = Converter()
a.get_condition()
a.get_tests()
a.get_solution()
a.convert(open('result.md', 'w'))


def main():
    print('hello')


if __name__ == '__main__':
    main()
