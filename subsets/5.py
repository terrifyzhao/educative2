class String:
    def __init__(self, str, open, close):
        self.close = close
        self.open = open
        self.str = str


from collections import deque


def generate_valid_parentheses(num):
    result = []
    string = String('', 0, 0)
    queue = deque()
    queue.append(string)

    while queue:
        s = queue.popleft()

        if s.open == num and s.close == num:
            result.append(s.str)

        if s.open < num:
            queue.append(String(s.str + '(', s.open + 1, s.close))
        if s.open > s.close:
            queue.append(String(s.str + ')', s.open, s.close + 1))

    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
