
def listodict(list1, list2):
    return dict(zip(list1, list2))

products = ['apple', 'banana', 'bread', 'milk']
prices = [100, 80, 50, 70]

res1 = listodict(list1=products, list2=prices)
print(res1)


res2 = listodict(products, list2=prices)
print(res2)
