subjects = ["Math", "English", "Computers"] #3 or higher else should run
choice = int(input("Choose one subject:"))

if subjects[choice] == subjects[0]:
    print(f"You've chosen {subjects[choice]}")
    print(subjects[choice] == subjects[0])
else:
    print("That didn't match")
    print(subjects[1])
    print(choice)
    