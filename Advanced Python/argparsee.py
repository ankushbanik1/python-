import argparse
def fib():

    a,b=0,1
    for i in range(6):


        a,b=b,a+b
    print(a)

def Main():
    parser=argparse.ArgumentParser()
    parser.add_argument('num',help="Enter a input",type=int)
    args=parser.parse_args()

    result=fib(args.num)
    print("The"+str(args.num)+"Fibonassi Term is "+str(result))



if __name__ == "__main__":
    Main()   