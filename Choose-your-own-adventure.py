#https://www.youtube.com/watch?v=_ZqAVck-WeM&t=358s

print("Welcome to my first game!")
name = input("What is your name? ")
print(f"Hi {name}! That's a really cool name!")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print("That's a really cool age! You sound kinda hot...")

    wants_to_play = input("Do you want to play? (yes/no)").lower()
    if wants_to_play == "yes":
        print("You are staring with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")

            else:
                print("Whoops! That's some slippery mud! Now you're in the river! Take 1 damage.")
                health -= 1

                ans = input("Do you swim down the river or try and get out? (swim/get out)")
                if ans == "swim":
                    print("You're not as fit as you thought. You get tired and swallow some water. Take 2 damage.")
                    health -= 5
                else:
                    print("You get sucked off by a fish as you try and get out. Gain 1 health.")
                    health += 1

                print(f"You're health is now {health}. That's pretty good! Keep going!")
        else:
            print("You bump your shin into a piece of furniture and immediately die... sorry pal. Maybe you should try again.")

    else:
        print("Cya...")
else:
    print("You are not old enough to play...")













