# Receipt generator 
sum = 0 
number_added = {}
print("For knowing the sum of your purchase press q")
while True:
    try:
        products = input(" Enter the products you shopped \n")
        if products == "q":
            quit()
        
        num = input(" Enter the cost of the product: \n")
        
        number_added[f"{products}"] = num
        print(number_added)
        if products != "q":
            sum = sum + int(num)
            print(f" You have done shopping for a total amount of {sum}Rs")
            
    except Exception as e:
        print(e)
    finally:
        print("########## Thank You for Shopping here ##########")








