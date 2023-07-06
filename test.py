
class Test : 
    def __init__(self) :
        pass 


    def say_hello(self) :
        for c in range(5) : 
            print(c)
            if c == 2 :
                c+=1

    


if __name__=='__main__' :
    t = Test()
    t.say_hello()
