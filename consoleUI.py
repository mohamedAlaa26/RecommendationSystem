from recommendation import users, recommend, all_users_stats


def display_recommendation_system():
    while True:
        print("Welcome to the Recommendation System")
        print("1. Get Recommendation")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user = input("Enter your username: ")
            if user not in users:
                print("Invalid username. Please try again.")
                continue

            cart = input("Enter items in your cart separated by commas: ").split(",")
            cart = [item.strip() for item in cart]

            recommendation = recommend(user, cart, all_users_stats)
            print(f"Recommended item for {user}: {recommendation}")

        elif choice == '2':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    display_recommendation_system()
