# Create a function named calculate_discount(price, discount_percent) that calculates the final price after 
# applying a discount. The function should take the original price 
# (price) and the discount percentage (discount_percent) as parameters.
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.
def calculate_discount(original_price, discount_percent):

    if discount_percent >= 20:
        
        discount_amount = original_price * (discount_percent / 100)
        
        final_price = original_price- discount_amount
        return final_price
    else:
       
        return original_price
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price using the calculate_discount function
    final_price = calculate_discount(original_price, discount_percent)
    
    # Print the final price
    print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numerical values.")