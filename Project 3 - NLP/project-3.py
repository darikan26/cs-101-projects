# Credits:
# - get_tokens_from_file() function adapted from read_words_from_file() (lab 05)
# - I learned the FreqDist() method from reading the nltk documentation
# - The-Time-Machine.txt obtained from https://www.gutenberg.org/files/35/35-0.txt
# - Beyond-Lies-The-Wub.txt obtained from https://www.gutenberg.org/cache/epub/28554/pg28554.txt

from nltk import *
import unidecode
import matplotlib.pyplot as plt

filename = "The-Time-Machine.txt"

# adapted from read_words_from_file() from lab05.
def get_tokens_from_file(filename):
    with open(filename, encoding = "utf-8") as file:
        text_utf8 = file.read()
        text = unidecode.unidecode(text_utf8)
        text = text.lower()
    tokens = word_tokenize(text)
    return tokens

def remove_punctuation(tokens):
    punctuation = ["_", ".", ",", "'", ";", ":", "?", "(", ")",
                   "\"", "*", "-", "!", "#", "``", "''", "--",
                   "[", "]", "&", "`", "<", ">"]
    
    words = []
    for token in tokens:
        if token not in punctuation:
            words.append(token)
    return(words)
    
def plot_frequency_distribution(words):
    words_freq = FreqDist(words)
    words_freq.plot(30,cumulative=False, color = "mediumorchid")
    plt.show()

def main():
    tokens = get_tokens_from_file(filename)
    words = remove_punctuation(tokens)
    plot_frequency_distribution(words)
    
main()

