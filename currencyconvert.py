def get_exchange_rate(currency_from, currency_to):
    """Return the exchange rate between two currencies."""
    exchange_rates = {
        'USD': {'EUR': 0.85, 'GBP': 0.76, 'INR': 73.50},
        'EUR': {'USD': 1.18, 'GBP': 0.89, 'INR': 86.50},
        'GBP': {'USD': 1.31, 'EUR': 1.12, 'INR': 97.75},
        'INR': {'USD': 0.014, 'EUR': 0.012, 'GBP': 0.010},
    }

    if currency_from in exchange_rates and currency_to in exchange_rates[currency_from]:
        return exchange_rates[currency_from][currency_to]
    else:
        return None

def convert_currency(amount, currency_from, currency_to):
    """Convert the amount from one currency to another based on exchange rate."""
    rate = get_exchange_rate(currency_from, currency_to)
    if rate:
        return amount * rate
    else:
        return None

def currency_converter():
    print("Welcome to the Currency Converter!")
    
    while True:
        print("\nAvailable currencies: USD, EUR, GBP, INR")
        
        currency_from = input("Enter the currency you want to convert from: ").upper()
        currency_to = input("Enter the currency you want to convert to: ").upper()
        
        try:
            amount = float(input(f"Enter the amount in {currency_from}: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        
        converted_amount = convert_currency(amount, currency_from, currency_to)
        
        if converted_amount is not None:
            print(f"{amount} {currency_from} = {converted_amount:.2f} {currency_to}")
        else:
            print("Conversion not available for the given currencies.")
        
        convert_again = input("Do you want to perform another conversion? (yes/no): ").lower()
        if convert_again != 'yes':
            print("Thank you for using the Currency Converter!")
            break

if __name__ == "__main__":
    currency_converter()
