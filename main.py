def main():
    ReadContents("books/frankenstein.txt")

def ReadContents(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        GetCharacterCountInString(file_contents.lower())

def GetCharacterCountInString(bookText: str):
    characterDict = {
        "p" : bookText.count("p"),
        "c" : bookText.count("c"),
        " " : bookText.count(" ")
    }
    print(characterDict)

main()