class MyDict:
    def __init__(self, dictionary: dict):
        self.__dictionary = dictionary

    def get_value(self, key):
        if key in self.__dictionary:
            return self.__dictionary[key]
        else:
            return 0

    def set_key_value(self, key, value):
        self.__dictionary[key] = value

    def show_dictionary(self):
        for key, value in self.__dictionary.items():
            print('{}: {}'.format(key, value))


my_dict = MyDict(dict())
my_dict.set_key_value('t', 5)
my_dict.set_key_value('t', 6)
my_dict.set_key_value(8, 'r')
print(my_dict.get_value(8))
my_dict.show_dictionary()
