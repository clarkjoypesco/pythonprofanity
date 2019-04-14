
def read_text():
    quotes = open('C:\Users\ClarkJoy\Documents\Repository\pythonprofanity\detect_profanity\movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()