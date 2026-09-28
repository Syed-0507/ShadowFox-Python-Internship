# Beginner Task - For Loop

import random


# -----------------------------------
# 1. Six-Sided Dice Simulation
# -----------------------------------

print("----- Dice Rolling Simulation -----")

rolls = 20
count_six = 0
count_one = 0
consecutive_sixes = 0
previous_roll = None

for i in range(rolls):
    current_roll = random.randint(1, 6)

    print("Roll", i + 1, ":", current_roll)

    if current_roll == 6:
        count_six += 1

    if current_roll == 1:
        count_one += 1

    # Check whether the current and previous rolls are both 6
    if current_roll == 6 and previous_roll == 6:
        consecutive_sixes += 1

    previous_roll = current_roll

print("\nDice Statistics:")
print("Number of times 6 was rolled:", count_six)
print("Number of times 1 was rolled:", count_one)
print("Number of times two 6s occurred in a row:", consecutive_sixes)


# -----------------------------------
# 2. Jumping Jacks Workout
# -----------------------------------

print("\n----- Jumping Jacks Workout -----")

total_jumping_jacks = 100
completed = 0

for i in range(10):

    completed += 10

    print("\nYou completed", completed, "jumping jacks.")

    # If all 100 are completed
    if completed == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").strip().lower()

    if tired == "yes" or tired == "y":

        skip = input(
            "Do you want to skip the remaining sets? (yes/no): "
        ).strip().lower()

        if skip == "yes" or skip == "y":
            print(
                "You completed a total of",
                completed,
                "jumping jacks."
            )
            break

        else:
            remaining = total_jumping_jacks - completed
            print(remaining, "jumping jacks remaining.")

    else:
        remaining = total_jumping_jacks - completed
        print(remaining, "jumping jacks remaining.")