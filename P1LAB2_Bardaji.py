# CTI-11
# P1LAB2 -  A program that demonstrates Input, Processing, and Output by calculating product sales. 
# John
# 9/3/26

# fictional store -- pick three things
# product_name, product_count, product_price

# hardcoding sets values directly
# product_name = "lemon"            # strings use "quotes" and are made of text
# product_count = 1000              # integers are whole numbers, no decimal
# product_price = 1.50              # double's are decimal numbers

# Instead, we ask he user with input()
# input
print("STORE STARTUP")
print("_" * 10)
product_name = input ("enter product name: ")
product_count = input("enter product count: ")
product_price = input("enter unit price: ")


# processing 
product_count = int(product_count) # convert string to integer: "100" -> 100
product_price = float(product_price) # convert string to float: float "3.25" -> 3.25
total = product_count * product_price # requires two numbers, returns a third number

# output
print("CUSTOMER INTERFACE")
print("_" * 10)
print("welcome to the", product_name, "store")

print(f"we have {product_count}, {product_name}(s) at  {product_price:.2f} each." )
print(f"total is: ${total:.2f}.")


