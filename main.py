from colorama import Fore, Style
import os
from time import sleep

def clear():
	os.system("clear")


Options = True
start = True

print("This program is used to identify the\nnumber is pythagrean triplet or not")
while Options:
	try:
		print("(1) Start \n(2) Help \n(0) Exit")
		User_Option = int(input("Enter your option: "))
		if User_Option == 1:
			while start:
				try:
					clear()
					print(f"()")
					a = int(input(Style.RESET_ALL+"Enter the value of a: "))
					clear()
					print(f"({a})")
					b = int(input("Enter the value of b: "))
					clear()
					print(f"({a},{b})")
					c = int(input("Enter the value of c: "))
					clear()
					print(f"({a},{b},{c})")
					confirm = input("Are these the values you want to use? (y/n): ")
					if confirm == "y" or confirm == "Y" or confirm == "":
						start = True
					elif confirm == "n" or confirm == "N":
						start = False
					else:
						print("Invalid option")
						sleep(2)
						clear()

					if a > 0 and b > 0 and c > 0:
						d = a, b, c
						Question = sorted(d, reverse=True)
						if Question[2]**2 + Question[1]**2 == Question[0]**2:
							clear()
							print(f"""
Question: ({a},{b},{c})

Answer:{Fore.GREEN}
	{Question[0]}² = {Question[0]**2} ------- (1)
	{Question[1]}² + {Question[2]}² = {Question[1]**2} = {Question[1]**2 + Question[2]**2} ----- (2)

	∴ {Question[0]}² = {Question[1]}² + {Question[2]}² ----- (from 1 & 2)
	{Fore.YELLOW}
The square of the largest number is equal to the 
sum of the squares of the other two numbers.
{Style.RESET_ALL}
""")
							input("Press Enter to continue...")

						else:
							clear()
							print(f"""
Question: ({a},{b},{c})

Answer:{Fore.YELLOW}
	{Question[0]}² = {Question[0]**2} ------- (1)
	{Question[1]}² + {Question[2]}² = {Question[1]**2} = {Question[1]**2 + Question[2]**2} ----- (2)

	∴ {Question[0]}² ≠ {Question[1]}² + {Question[2]}² ----- (from 1 & 2)
	{Fore.GREEN}
The square of the largest number is not equal to
the sum of the squares of the other two numbers.
{Style.RESET_ALL}
""")
							input("Press Enter to continue...")

				except ValueError:
					print(Fore.RED + "Please enter a valid number")
		elif User_Option == 2:
			clear()
			print("This program is used to identify the number is\npythagrean triplet or not")
			print(f"\nBy using the formula: {Fore.YELLOW}a2 + b2 = c2{Style.RESET_ALL}\n")
			print("The program will ask you to enter the values of\na, b and c")
			print("If the values are correct, the program will\nidentify if the number is\npythagrean triplet or not")
			print("If the values are incorrect, the program will ask you to enter the values again")
			input(f"\n\n\n\n\n\nPress {Fore.GREEN}Enter{Style.RESET_ALL} to continue...")

		elif User_Option == 0:
			clear()
			print("Exiting...")
			sleep(1)
			exit()
	except ValueError:
		print("Please enter a valid option")
		sleep(2)
		clear()
		continue
