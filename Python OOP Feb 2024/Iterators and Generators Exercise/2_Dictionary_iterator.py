class dictionary_iter():
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.checker = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.checker == len(self.dictionary) - 1:
            raise StopIteration

        self.checker += 1
        dict_list = list(self.dictionary.items())
        return list(dict_list)[self.checker]


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
