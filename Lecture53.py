totalPrice = int(input("Price: "))
def vatCalculate(totalPrice):
    y = 7/100
    Result = (y*totalPrice)+totalPrice
    print("Vat: ", int(y*totalPrice))
    return Result
print("TotalPrice: ", vatCalculate(totalPrice))