# Beginner Task - Classes and Objects


class Avenger:

    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    # Method to display superhero information
    def get_information(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)

    # Method to check whether the superhero is a leader
    def is_leader(self):
        if self.leader:
            print(self.name, "is the leader of the Avengers.")
        else:
            print(self.name, "is not the leader of the Avengers.")


# Creating Avengers objects

captain_america = Avenger(
    "Captain America",
    105,
    "Male",
    "Super Strength",
    "Shield",
    True
)

iron_man = Avenger(
    "Iron Man",
    53,
    "Male",
    "Technology",
    "Armor"
)

black_widow = Avenger(
    "Black Widow",
    39,
    "Female",
    "Superhuman",
    "Batons"
)

hulk = Avenger(
    "Hulk",
    54,
    "Male",
    "Unlimited Strength",
    "No Weapon"
)

thor = Avenger(
    "Thor",
    1500,
    "Male",
    "Super Energy",
    "Mjolnir"
)

hawkeye = Avenger(
    "Hawkeye",
    52,
    "Male",
    "Fighting Skills",
    "Bow and Arrows"
)


# Store all Avengers in a list

avengers = [
    captain_america,
    iron_man,
    black_widow,
    hulk,
    thor,
    hawkeye
]


# Display information about each Avenger

print("----- AVENGERS TEAM -----")

for avenger in avengers:
    avenger.get_information()
    avenger.is_leader()