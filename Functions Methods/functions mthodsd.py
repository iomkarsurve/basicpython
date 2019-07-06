def Add(a,b,c):
    print(a+b+c)
Add(4,5,1)

def food():
    print("Chicken Biryani is love")
food()
food() #reuse function any number of times
food()
food()

#default argument
def price(qty=1):
    print("Price is :",qty*40,"$")
price()  #if no value for qty 1 will be used



def Order(item):
    if(item=="chicken biryani"):
        return 1
itemname=input("enter item name")
result=Order(itemname)
print("Result id ",result)
if(result==1):
    print("200Rs , Thank you for shopping")

