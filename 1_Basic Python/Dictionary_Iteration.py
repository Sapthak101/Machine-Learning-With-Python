prices={
    "box_of_spagetti": 90,
    "birani":56,
}
quantity={
    "box_of_spagetti":6,
    "birani":10
}

money_spent=0

for i in prices: #iterating though dictionaries by default gives the index
    money_spent=money_spent+prices[i]*quantity[i]
print(money_spent)

