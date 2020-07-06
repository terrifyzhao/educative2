def find_word_concatenation(str1, words):
    word_len = len(words[0])
    word_count = len(words)
    res = []
    if word_len==0 or word_count==0:
        return res

    word_fre = {}
    for word in words:
        word_fre[word] = word_fre.get(word,0)+1



    for i in range(len(str1)-word_len*word_count+1):
        word_seen = {}
        for j in range(word_count):
            word_start = i+j*word_len
            word = str1[word_start:word_start+word_len]

            if word not in word_fre:
                break

            word_seen[word] = word_seen.get(word,0)+1

            if word_seen[word] > word_fre[word]:
                break

            if j+1==word_count:
                res.append(i)
    return res


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()
