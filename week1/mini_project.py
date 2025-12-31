def action(name):
    print(f"Sonic punches {name}.")

def damage_taken(damagenumber):
    return damagenumber + 3

damage = damage_taken(7)
print(damage)

print ("Enter your name.\n")
name = input()
print(f"I found you faker. What is it again? {name} they call you?")
shittalk = (input(f"{name} huh.. all im seeing is a shadow of myself. You seem like a faker to me.\n"))
if shittalk == "Faker? I think you're the fake hedgehog around here. You're comparing yourself to me? HA! You're not even good enough to be my fake.":
    print("I'll make you eat those words!\n")
    response = int(input())
    if response == 1:
        action(name)
        damage = damage_taken(7)
        print(damage)
elif shittalk == "We can talk about fakes and appearances later. For now, we've gotta get out of this island with the rest of the emeralds before it blows up under our feet.":
    print("Guess this is the perfect time to test out who's the fastest out of the both of us. Better speed up if you wanna live!\n")
    response = input()


    #I revolved this mini project around Sonic and Shadow's first interaction in the 2001 video game 'Sonic Adventure 2'. Based on what responses you put in the terminal determines how the conversation between the two alien hedgehogs go. Basically a multiple choice text adventure game. Best part of week 1 by far.