import re


def Main():
    line="Hii i am ankush , self-tought programmer"
    inn=input("Enter a string: ")

    matchResult=re.match(inn,line, re.M|re.I)
    if matchResult:
        print("Found",matchResult.group())

    else:
        print("Not found")
        SearchResult=re.search(inn,line, re.M|re.I)
    if SearchResult:
        print("Found in search",SearchResult.group())

    else:
        print("Not found")

if __name__ == "__main__":
    Main()