# Function to calculate the final price after a discount.
def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, the discount is applied.
    Otherwise, the original price is returned.
    
    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage (e.g., 20 for 20%).

    Returns:
        float: The final price after the discount, or the original price.
    """
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate and return the final price
        return price - discount_amount
    else:
        # If the discount is less than 20%, return the original price
        return price

# --- Main part of the script ---

if __name__ == "__main__":
    try:
        # Prompt the user to enter the original price and convert it to a float.
        original_price = float(input("Enter the original price of the item: "))
        # Prompt the user for the discount percentage and convert it to a float.
        discount_percentage = float(input("Enter the discount percentage (e.g., 25 for 25%): "))

        # Call the function to get the final price.
        final_price = calculate_discount(original_price, discount_percentage)

        # Print the final price based on whether a discount was applied.
        if final_price == original_price:
            print(f"The original price is: ${original_price:.2f}")
        else:
            print(f"The final price is: ${final_price:.2f}")

    except ValueError:
        # Handle cases where the user enters non-numeric input.
        print("Invalid input. Please enter a valid number for price and discount.")
        #enjoy running the programme
