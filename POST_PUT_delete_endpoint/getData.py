products = [
    {
        "id" : 1,
        "title":"Mobile Phone",
        "price":12000,
        "quantity":12
    },
    {
        "id" : 2,
        "title":"Mobile Phone",
        "price":12000,
        "quantity":12
    }
]

def getP():
    for i in products:
        if(i.get("id") == 1):
            return i

print(getP())