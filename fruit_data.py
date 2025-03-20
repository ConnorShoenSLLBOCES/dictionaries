def main():
    fruits = {}

    # Get number of fruits
    num_fruits = int(input("How many fruits would you like to enter? "))

    # Collect data
    for x in range(num_fruits):
        name = input("Enter the fruit name: ").strip()
        color = input(f"Enter the color of {name}: ").strip()
        weight = float(input(f"Enter the average weight of {name}(in lbs.): "))
        price = float(input(f"Enter the price per pound of {name}($): "))

        # Store Data
        fruits[name] = {
            'Color':color,
            'Average Weight':weight,
            'Price per Pound':price
            }
    
    # Output data
    print("\nFruit Data Overview:\n")
    
    for fruit, details in fruits.items():
        print(f"Fruit: {fruit}")
        print(f"Color: {details['Color']}")
        print(f"Average Weight: {details['Average Weight']:.1f}")
        print(f"Price per Pound: ${details['Price per Pound']:.2f}")
        print("-" * 20)

if __name__ == "__main__":
    main()