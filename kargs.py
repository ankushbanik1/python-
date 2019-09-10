def marks(**kwargs):
    print(type( kwargs))

    for key,value in kwargs.items():
        print(key ,value)


marklist={"ankush banik":91,"arian basak":68}

marks(**marklist)