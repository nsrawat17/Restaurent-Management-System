def generate_bill(orders):
    total =0
    print("\n Your Bill is :")
    print("-------------------------")
    for item , price, qty in orders:
        print(f"{item} -- {price}")
        amt = price*qty
        total += amt

    print("------------------")
    print(f"Total amount is {total}")