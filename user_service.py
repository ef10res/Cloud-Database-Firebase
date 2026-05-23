from firebase import db

# add user function
def add_user():
    user_id = input("User ID: ")
    name = input("Name: ")

    db.collection("users").document(user_id).set({
        "name" : name
    })

    print("User added!")

# view users function
def view_users():
    users = db.collection("users").stream()
    
    print("\n=== USERS ===")
    for u in users:
        print(u.id, u.to_dict())

# delete user function
def delete_user():
    user_id = input("User ID to delete: ")

    #delete user document
    db.collection("users").document(user_id).delete()

    print("User deleted")