def get_discount_prize(actual_price,discount):
    dicont_amount=(actual_price*discount)/100
    selling_prize=actual_price-dicont_amount
    return selling_prize
actual=int(input("enetr the actual prize : "))
disc=int(input("enter the discount percentage : "))
print("selling price=",get_discount_prize(actual,disc))