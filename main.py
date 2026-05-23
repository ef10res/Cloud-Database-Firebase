from menu import show_menu
import user_service as user
import workout as workout

# selection of menu items
while True:
    show_menu()
    choice = input("Select option: ")

    if choice == "1":
        user.add_user()
    
    elif choice == "2":
        user.view_users()
    
    elif choice == "3":
        user.delete_user()
    
    elif choice == "4":
        workout.add_workout()

    elif choice == "5":
        workout.view_workouts()

    elif choice == "6":
        workout.update_workout()

    elif choice == "7":
        workout.delete_workout()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid option")