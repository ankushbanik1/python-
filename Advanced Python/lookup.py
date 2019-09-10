import re
import argparse

def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument("wo",help="i am the wo")
    parser.add_argument("hello",help="hello world its ankush")
    args=parser.parse_args()
    searchFile=open(args.hello)
    line=0

    for linesearch in searchFile:
        linesearch=linesearch.strip('n\r')
        line+=1
        searchResult=re.search(args.hello,linesearch,re.M|re.I)
        if searchResult:
            print(str(line)+":"+linesearch)

if __name__ == "__main__":
    Main()            