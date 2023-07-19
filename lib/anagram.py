class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, old_list):
        new_list = []
        for word in old_list:
            if sorted(letter for letter in word) == sorted(
                letter for letter in self.word
            ):
                new_list.append(word)

            else:
                continue
        return new_list