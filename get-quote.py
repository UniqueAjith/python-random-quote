import random 

def primary(): 
    f = open("quotes.txt") 
    quotes = f.readlines() 
    f.close() 
    #last=18
    res = random.sample(quotes,2)
    for i in res:
        print(i,end="")

if __name__== "__main__": 
    primary()
