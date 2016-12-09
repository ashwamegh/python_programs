import urllib

def reading_text():
    text=open("C:\Users\AshwaMegh\Documents\GitHub\python_programs\movie_quotes.txt")
    contents=text.read()
    print("Check Normal speech: ")
    print("")
    print("")
    print(contents)
    print("")
    print("")
    text.close()
    pirate_speech(contents)

def pirate_speech(text):
    connection= urllib.urlopen("http://isithackday.com/arrpi.php?text="+text)
    contents = connection.read()
    print("Here's the Pirate version: ")
    print("")
    print("")
    print(contents)
    connection.close()

reading_text()
    
    
