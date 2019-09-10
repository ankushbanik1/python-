from string import Template



def Main():

       
    cart=[]
        
    cart.append(dict(item="milk",price=10,qyt=2))      
    cart.append(dict(item="mango",price=40,qyt=12))    
    cart.append(dict(item="rice",price=30,qyt=24)) 


    t=Template("$qyt x $item = $price")
    total=0
    for data in cart:
        print(t.substitute(data))
        total+= data["price"]
    print("total:"+str(total))


if __name__ == "__main__":
    Main()            



