# Movie Ticket Booking System

try:
    # User input
    user_name = input("Enter your name: ").strip()
    mobile_number = input("Enter your mobile number: ")
    ticket_type = input("Enter ticket type (Regular/VIP): ").strip().lower()
    number_of_tickets = int(input("Enter number of tickets: "))

    # Price selection
    if ticket_type == "regular":
        ticket_price = 500
    elif ticket_type == "vip":
        ticket_price = 1000
    else:
        print("Invalid ticket type entered!")
        exit()

    # Total calculation
    total_cost = ticket_price * number_of_tickets

    # Discount logic
    discount = 0
    if total_cost > 3000:
        discount = total_cost * 0.10

    final_amount = total_cost - discount

    # Output display
    print("\n--- Movie Ticket Bill ---")
    print("Customer Name:", user_name)
    print("Ticket Type:", ticket_type.capitalize())
    print("Number of Tickets:", number_of_tickets)
    print("Total Cost: Rs.", total_cost)
    print("Discount: Rs.", discount)
    print("Final Amount to Pay: Rs.", final_amount)

except ValueError:
    print("Please enter valid numeric input for number of tickets.")
