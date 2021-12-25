# Guess the number game
lucky_num = 26
close_num_g = lucky_num + 5
close_num_s = lucky_num - 5
max_num_of_guesses = 5
print("Welcome in 'GUESS THE NUMBER' game created by 'AKSHAT JAIN'")
print("You have" , max_num_of_guesses, "chances to guess the lucky number")
num_of_guesses = 1
left_guesses = 4
while(num_of_guesses<(max_num_of_guesses+1)):
    user_input = int(input("\nGuess any number : "))
    if user_input==lucky_num:
        print("yuppy ! You guess the lucky number\n You took ",num_of_guesses," guesses")
        break
    elif close_num_s<user_input<lucky_num:
        print("OOPPPSS ! Your so close , enter some greater number")
        print("left number of guesses", left_guesses)
    elif user_input<close_num_s:
        print("Enter greater number")
        print("left number of guesses", left_guesses)
    elif close_num_g>user_input>lucky_num:
        print("OOPPPSS ! Your so close , enter some smaller number")
        print("left number of guesses", left_guesses)
    elif user_input>close_num_g:
        print("Enter smaller number")
        print("left number of guesses", left_guesses)
    num_of_guesses = num_of_guesses + 1
    left_guesses = max_num_of_guesses - num_of_guesses

if (num_of_guesses>max_num_of_guesses):
    print("OPPSSS ! 'GAME OVER' ! you rach maximum number of guesses")

# not my code but i learn something from this code
# n=18
# number_of_guesses=1
# print("Number of guesses is limited to only 9 times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the number :\n"))
#     if guess_number<18:
#         print("you enter less number please input greater number.\n")
#     elif guess_number>18:
#         print("you enter greater number please input smaller number.\n ")
#     else:
#         print("you won\n")
#         print(number_of_guesses,"no.of guesses he took to finish.")
#         break
#     print(9-number_of_guesses,"no. of guesses left")
#     number_of_guesses = number_of_guesses + 1
#
# if(number_of_guesses>9):
#     print("Game Over")