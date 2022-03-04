
# Amber Kuhn

def main():
    total_cost = 0
    while True:
        try:
            number_app = int(input("How many of your dinners will have an appetizer?  "))
            if number_app < 0:
                raise ValueError
            break
        except ValueError:
            print("The amount must be a positive integer.")

    for total_app in range(number_app):
        cost_app = 0
        while True:
            try:
                cost_app = float(input("What is the cost of appetizer "f"{total_app + 1}?  "))
                if cost_app < 0:
                    raise ValueError
                break
            except ValueError:
                print("The amount must be a positive number.")
        total_cost += cost_app
        return total_cost
    print("The total cost of the appetizers is "f"${total_cost:,.2f}.")


if __name__ == '__main__':
    main()

