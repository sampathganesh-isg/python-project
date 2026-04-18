# Display Menu

def show_menu():
    print("\n----- ERP Student Course Registration System -----")
    print("1. Add Student")
    print("2. View Available Courses")
    print("3. Register Course")
    print("4. View Registered Courses")
    print("5. Show Analytics")
    print("6. Exit")


# Optional: Display Messages (Extra clean output)

def show_success(message):
    print(f"\n✅ {message}\n")


def show_error(message):
    print(f"\n❌ {message}\n")