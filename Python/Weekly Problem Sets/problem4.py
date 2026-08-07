## instructor code for problem 3

class lyricAnalyzer:
    def __init__(self, lyrics: str):
        self.lyrics = lyrics
        punctuation = ":,.!\"';"
        for punct in punctuation:
            lyrics = lyrics.replace(punct, "")
        self.words = lyrics.lower().split()

    def count_words(self):
        result = {}

        for word in self.words:
            if word not in result:
                result[word] = 1
            else:
                result[word] = result[word] + 1

            # result[word] = result.get(word, 0) + 1  # get method


    def unique_word_count(self):
        return len(self.count_words())

    def most_common_word(self):
        longest_word, longest_count = "", -1

        for word, count in self.count_words():
            if count > longest_count:
                longest_count = count
                longest_word = word
        return longest_word, longest_count


## write the print report

    




        return result
    