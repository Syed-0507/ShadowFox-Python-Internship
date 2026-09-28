# Beginner Task - List

# Initial Justice League members
justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Original Justice League:")
print(justice_league)


# 1. Calculate the number of members
print("\nNumber of members:", len(justice_league))


# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])

print("\nAfter adding Batgirl and Nightwing:")
print(justice_league)


# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("\nAfter making Wonder Woman the leader:")
print(justice_league)


# 4. Separate Aquaman and Flash by placing Superman between them
justice_league.remove("Superman")

flash_index = justice_league.index("Flash")
aquaman_index = justice_league.index("Aquaman")

# Insert Superman between Flash and Aquaman
if flash_index < aquaman_index:
    justice_league.insert(aquaman_index, "Superman")
else:
    justice_league.insert(flash_index, "Superman")

print("\nAfter separating Aquaman and Flash:")
print(justice_league)


# 5. Replace the existing team with the new Justice League
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("\nNew Justice League team:")
print(justice_league)


# 6. Sort the Justice League alphabetically
justice_league.sort()

print("\nJustice League after alphabetical sorting:")
print(justice_league)


# New leader
new_leader = justice_league[0]

print("\nNew Leader:", new_leader)