import os
import random
import sys
import colorama
import argparse
import datetime

char_text = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
script_ver = "1.0.0"
name_ascii = f'''{colorama.Fore.LIGHTRED_EX}
  _____               _____            
 |  __ \             / ____|                  ------------------------
 | |__) |_ _ ___ ___| |  __  ___ _ __  ----> | Author |   Cyber_Hill  |        {colorama.Fore.BLUE}
 |  ___/ _` / __/ __| | |_ |/ _ \ '_ \        ------------------------{colorama.Fore.YELLOW} 
 | |  | (_| \__ \__ \ |__| |  __/ | | | ---> | Script Version | {script_ver} |
 |_|   \__,_|___/___/\_____|\___|_| |_|       ------------------------  
{colorama.Fore.RESET}'''


def gen_pass(password_lenght, password_count):
    """

    :param password_lenght:
    :param password_count:
    :return List of generated password:

    """
    password_list = []
    for n in range(password_count):
        password = ''
        for i in range(password_lenght):
            password += random.choice(char_text)
        password_list.append(password)

    return password_list



parser = argparse.ArgumentParser()

parser.add_argument('-L', type=int, help="Length of generated passwords")
parser.add_argument('-C', type=int, help="Generated password count")
parser.add_argument('-P', type=str, help="Path to save result")


args = parser.parse_args()

if args.L or args.C or args.P:
    print(name_ascii)
    if not args.L or not args.C:
        print(colorama.Fore.LIGHTRED_EX + "Password length or Password count are missing!")
    else:
        if args.L < 1:
            print(colorama.Fore.LIGHTRED_EX + "Password length must be bigger than 0")
        elif args.C < 1:
            print(colorama.Fore.LIGHTRED_EX + "Password count must be bigger than 0")
        else:
            if not args.P:
                print(
                    colorama.Fore.LIGHTRED_EX + "\nPath to save is not promted:Result will not be saved!" + colorama.Fore.RESET)
                generated_passwords = gen_pass(args.L, args.C)
                print("\n==========================================")
                for password in generated_passwords:
                    print(colorama.Fore.LIGHTGREEN_EX + password + colorama.Fore.RESET)
                    print("==========================================")
            elif args.P:
                generated_passwords = gen_pass(args.L, args.C)
                print("\n==========================================")
                for password in generated_passwords:
                    print(colorama.Fore.LIGHTGREEN_EX + password + colorama.Fore.RESET)
                    print("==========================================")
                if os.path.exists(args.P):
                    date = f"{datetime.datetime.now().year}_{datetime.datetime.now().month}_{datetime.datetime.now().day}_{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}"
                    try:
                        with open(f"{args.P}result_{date}.txt", "w", encoding="utf-8") as file:
                            file.write("==========================================")
                            for passwords in generated_passwords:
                                file.write("\n"+passwords + "\n")
                                file.write("==========================================")
                            else:
                                print(f"Result has been successfully saved in {args.P}result_{date}.txt")
                    except:
                        if PermissionError:
                            print(colorama.Fore.LIGHTRED_EX + "Unable create file in directory:Permission denied")
                        else:
                            print("Unknown Error")

                elif not os.path.exists(args.P):
                    print(colorama.Fore.LIGHTRED_EX + "\nPath does not exists!")


else:
    print(name_ascii)

    password_lenght = input("Please write length of passwords: ")
    password_count = input("Please write count of passwords: ")
    if not password_count or not password_lenght:
        print(colorama.Fore.LIGHTRED_EX + "Password length or Password count are missing!")
    else:
        try:
            password_lenght = int(password_lenght)
            password_count = int(password_count)


        except:
            print(colorama.Fore.LIGHTRED_EX + "Error promt only number")
            sys.exit()

        generated_passwords = gen_pass(password_lenght, password_count)
        print("\n==========================================")
        for password in generated_passwords:
            print(colorama.Fore.LIGHTGREEN_EX + password + colorama.Fore.RESET)
            print("==========================================")

        save = input("\nDo you want save result? (y/n)")
        if save.lower() in ["y", "yes"]:
            path = input("\nWrite path? ")
            if os.path.exists(path):
                date = f"{datetime.datetime.now().year}_{datetime.datetime.now().month}_{datetime.datetime.now().day}_{datetime.datetime.now().hour}_{datetime.datetime.now().minute}_{datetime.datetime.now().second}"
                try:
                    with open(f"{path}result_{date}.txt", "w", encoding="utf-8") as file:
                        file.write("==========================================")
                        for passwords in generated_passwords:
                            file.write("\n"+passwords + "\n")
                            file.write("==========================================")
                        else:
                            print(f"Result has been successfully saved in {path}result_{date}.txt")
                except:
                    if PermissionError:
                        print(colorama.Fore.LIGHTRED_EX + "Unable create file in directory:Permission denied")
                    else:
                        print("Unknown Error")

            elif not os.path.exists(path):
                print(colorama.Fore.LIGHTRED_EX + "Path does not exists!")
        elif save.lower() in ["n", "no"]:
            pass

