from firebase import db
from datetime import datetime

# workout types array
WORKOUT_TYPES = ["run", "lift", "swim", "hike", "bike"]

#select user 
def select_user():
    return input("Enter user ID: ")

# add workout function
def add_workout():
    user_id = select_user()

    print("Workout types: ")
    for i, w in enumerate(WORKOUT_TYPES):
        print(f"{i+1} {w}")

    choice = int(input("Select type: ")) - 1
    workout_type = WORKOUT_TYPES[choice]

    # add details like miles ran, distance swam, or weights lifted and calories
    details = input("Details: ")
    calories = int(input("Calories: "))
    
    # add information to database
    db.collection("users").document(user_id)\
      .collection ("workouts").add({
          "type": workout_type,
          "details": details,
          "calories": calories,
          "date": datetime.now()
      })
    print("Workout added!")

# view workouts function
def view_workouts():
    user_id = select_user()

    workouts = db.collection("users").document(user_id)\
        .collection("workouts").stream()
    
    # iterate through the workouts in database
    print("\n=== WORKOUTS ===")
    for w in workouts:
        print(w.id, w.to_dict())

# delete workout function
def delete_workout():
    user_id = select_user()

    # view workouts and select workout to delete
    view_workouts()
    workout_id = input("Workout ID to delete: ")

    db.collection("users").document(user_id)\
      .collection("workouts").document(workout_id).delete()
    
    print("Workout deleted!")

# upddate workout function
def update_workout():
    user_id = select_user()

    #view workouts and select workout to update
    view_workouts()
    workout_id = input("Workout ID to update: ")

    # new details and calories
    new_details = input("New details: ")
    new_calories = int(input("New calories: "))

    db.collection("users").document(user_id)\
      .collection("workouts").document(workout_id).set({
          "details": new_details,
          "calories": new_calories
      })
    
    print("Workout updated!")