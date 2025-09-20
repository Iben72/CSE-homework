# loan eligibility estimation

loan = int(input("how large is the loan? "))
print(f"the loan size is rated as {loan}")

credit_history = int(input("how good is your credit history? "))
print(f"my credit history is rated as {credit_history}")

income = int(input("how high is your income? "))
print(f"my income is as high as {income}")

down_payment = int(input(" how high is your down payment? "))
print(f"my down payment is as high as {down_payment}")




     
if credit_history >= 7 and income >= 7 and loan >=5:
    print("yes")

elif (credit_history >= 7 or income >= 7) and down_payment >= 5 and loan >= 5:
     print("yes")

elif (credit_history >= 7 or income >= 7) and down_payment < 5 and loan >= 5:
     print("no")



     
if loan < 5 and credit_history < 4:
     print("no")

elif (income >= 7 or down_payment >= 7) and loan < 5:
     print("yes")

elif income >= 4 and down_payment >= 4 and loan < 5:
     print("yes")

elif income < 4 and down_payment < 4 and loan < 5:
     print("no")

else:
     print("no")



    