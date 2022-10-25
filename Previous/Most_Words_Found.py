class MostWordsFound:
    def most_words(self, sentences: [str]) -> int:
        max_words = 0
        for sentence in sentences:
            temp_words = sentence.count(" ")
            max_words = max(max_words, temp_words)
        return max_words