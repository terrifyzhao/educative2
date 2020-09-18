from collections import deque


class Abbreviation:
    def __init__(self, str, char_len, abb_len):
        self.str = str
        self.char_len = char_len
        self.abb_len = abb_len


def generate_generalized_abbreviation(word):
    l = len(word)
    result = []
    queue = deque()
    queue.append(Abbreviation([], 0, 0))
    while queue:
        abb = queue.popleft()
        if abb.char_len == l:
            if abb.abb_len != 0:
                abb.str.append(str(abb.abb_len))
            result.append(''.join(abb.str))
        else:
            queue.append(Abbreviation(list(abb.str), abb.char_len + 1, abb.abb_len + 1))
            if abb.abb_len != 0:
                abb.str.append(str(abb.abb_len))
            new_word = list(abb.str)
            new_word.append(word[abb.char_len])
            queue.append(Abbreviation(list(new_word), abb.char_len + 1, 0))
    return result


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
