from string import Template

    
def Main():
        cart=[]
        cart.append(dict(item="milk",qyt=12,price=100))
        cart.append(dict(item="banana",qyt=12,price=10))
        total=0
        
        t=Template("$item  + $qyt= $price")

        for data in cart:
            print(t.substitute(data))
            total+= data["price"]
        print("total:"+str(total))


if __name__ == "__main__":
    Main()            
    
            






