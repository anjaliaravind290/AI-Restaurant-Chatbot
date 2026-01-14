# Simple AI Restaurant Chatbot

# Step 1: Create the menu
menu = {
    "Pizza": 12,
    "Burger": 8,
    "Pasta": 10,
    "Coke": 2
}

# Step 2: Welcome message
print("Welcome to AI Restaurant Chatbot!")
print("Type 'menu' to see the menu, 'order <item>' to order, 'my order' to view your order, or 'exit' to quit.")

# Step 3: Memory to store user orders
order_memory = []

# Step 4: Chat loop
while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("Chatbot: Thank you! Visit again.")
        break

    elif "menu" in user_input:
        print("Chatbot: Here is our menu:")
        for item, price in menu.items():
            print(f"- {item}: ${price}")
    
    elif "order" in user_input:
        item = user_input.replace("order ", "").title()
        if item in menu:
            order_memory.append(item)
            print(f"Chatbot: {item} added to your order!")
        else:
            print("Chatbot: Sorry, we don't have that item.")
    
    elif "my order" in user_input:
        if order_memory:
            print("Chatbot: Your current order:", ", ".join(order_memory))
        else:
            print("Chatbot: You haven't ordered anything yet.")
    
    else:
        print("Chatbot: I can show the menu, take your order, or show your current order.")


