total = input('What is the total amount for your online shopping? ')
country = input('Shipping within the US or Canada? ')

if country == "US":
    if float(total) <= 50:
        print("Shipping Costs $6.00")
    elif float(total) <= 100:
        print ("Shipping Costs $9.00")
    elif float(total) <= 150:
        print ("Shipping Costs $12.00")
    else:
        print ("FREE")
if country == "Canada":
    if float(total) <= 50:
        print ("Shipping Costs $8.00")
    elif float(total) <= 100:
        print ("Shipping Costs $12.00")
    elif float(total) <= 150:
        print ("Shipping Costs $15.00")
    else:
        print ("FREE")

        
        
