class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def find(self, word):
        places = {}
        for value, key in self.get_all_words().items():
            if word.lower() in key:
                places[value] = key.index(word.lower()) + 1

        return places

    def count(self, word):
        counters = {}
        for value, key in self.get_all_words().items():
            words_count = key.count(word.lower())
            counters[value] = words_count

        return counters

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                info = file.read().lower()
                for sym in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    info = info.replace(sym, '')
                all_words[name] = info.split()

        return all_words

finder1 = WordsFinder('test_file.txt')

print(finder1.get_all_words())
print(finder1.find('teXT'))
print(finder1.count('teXT'))