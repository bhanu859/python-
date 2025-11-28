rent = int(input("enter the house/rate rate : "))
food = int(input("enter the amount for food ordered : "))
electricity_spend = int(input("enter the amount spend on electricity : "))
charge_per_unit = int(input("enter the total members of persons : "))
persons = int(input("enter the charge per unit : "))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill)//persons
print ("each person has to pay : ",output)