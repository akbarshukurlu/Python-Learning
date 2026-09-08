print("**************")

class File():

    def __init__(self):

        with open("Advanced Data Structures/text.txt", "r", encoding="utf-8") as file:

            file_content = file.read()

            words = file_content.split()
            self.simple_words = list()

            for i in words:
                i = i.strip(" ")
                i = i.strip(",")
                i = i.strip(".")

                self.simple_words.append(i)
    def all_words(self):

        set_of_words = set()

        for i in self.simple_words:
            set_of_words.add(i)

        print("All words....")

        for i in set_of_words:
            print(i)

            print("***************************")


    def words_frequency(self):

        word_dictionary = dict()

        for i in self.simple_words:

            if (i in word_dictionary):
                word_dictionary[i] += 1
            else: 
                word_dictionary[i] = 1

        for word,number in word_dictionary.items():
            print("The word {} appears {} times....".format(word,number))


            print("------------------------------------")
file = File()
file.words_frequency()
