import urllib

def read_text():
    quotes=open("C:\Users\AshwaMegh\Documents\GitHub\python_programs\movie_quotes.txt")
    contents_of_the_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_the_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output= connection.read()
    if "true" in output:
        print("Profanity Alert !")
    elif "false" in output:
        print("The document is secure.")
    else:
        print("Can not scan the Document Properly")
    connection.close()
    
read_text()
