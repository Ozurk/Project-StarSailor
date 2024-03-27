import sys
import time
import re
import pyautogui
import os
import shutil
import pandas

print("\n" * 3)
input("maximize window\n")
terminal_width = shutil.get_terminal_size().columns
intro_screen_character = input("type a single character then press enter".center(terminal_width) + "\n")


def typing_effect(string, wait_time):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(wait_time)  # this controls the speed of the game


intro_speed = .001
os.system("cls")


def full_screen():
    # todo work on this
    counter = 0
    while counter != 3:
        try:
            pyautogui.screenshot(r"..\pictures\screenshot_for_maximize.png")
            cmd_maximize = pyautogui.locateCenterOnScreen(r"..\pictures\cmd_maximize_png.png", grayscale=False)
            print(cmd_maximize)
            pyautogui.moveTo(cmd_maximize[0], cmd_maximize[1], 3)
            time.sleep(.25)
            pyautogui.click()
        except pyautogui.ImageNotFoundException:
            print("Attempting Operation")
            counter += 1
    os.system('cls')
    input("If it was not done automatically, please maximize the terminal window\n")


def intro_striper(number_of_rows):
    for stripes in range(number_of_rows):
        typing_effect(intro_screen_character * terminal_width, intro_speed)
        print()
        typing_effect("+" * terminal_width, intro_speed)
        print()
        typing_effect(intro_screen_character * terminal_width, intro_speed)
        print()


def intro_screen():
    starsailor_sign = ['-----------------------------------------------------------------------------',
                       '  #####  #######    #    ######   #####     #    ### #       ####### ######  ',
                       ' #     #    #      # #   #     # #     #   # #    #  #       #     # #     # ',
                       ' #          #     #   #  #     # #        #   #   #  #       #     # #     # ',
                       '  #####     #    #     # ######   #####  #     #  #  #       #     # ######  ',
                       '       #    #    ####### #   #         # #######  #  #       #     # #   #   ',
                       ' #     #    #    #     # #    #  #     # #     #  #  #       #     # #    #  ',
                       '  #####     #    #     # #     #  #####  #     # ### ####### ####### #     # ',
                       '-----------------------------------------------------------------------------']
    # this is the fancy little intro screen
    intro_striper(6)
    round_number = 0
    print("\n")
    for iterations in starsailor_sign:
        typing_effect(starsailor_sign[round_number].center(terminal_width, ":") + "\n", intro_speed)
        round_number += 1

    print("\n")
    intro_striper(6)
    time.sleep(.75)
    print('\n\n')
    input("Press Enter to Continue...".center(terminal_width, " ") + "\n")
    print("\n")


def get_file(file_path):
    try:
        file = open(file_path, "r")
        text = file.read()
        text = text.strip()
        file.close()
        return text
    except UnicodeDecodeError:
        file = open(file_path, "r", encoding="utf-8")
        text = file.read()
        text = text.strip()
        file.close()
        return text


def text_regex(text):
    alphabet_regex = re.compile("[a-zA-Z]+")
    mo = alphabet_regex.findall(text)
    return mo
    # will return a list of strings


def one_or_two():
    user_input = input("\n Enter [1] or [2]\n")
    if user_input.strip() == "1":
        return int(user_input)
    elif user_input.strip() == "2":
        return int(user_input)
    else:
        print("You must enter 1 or 2")
        one_or_two()


def yes_or_no(yes_or_no_input):
    options = ['yes', 'no']
    while yes_or_no_input.lower().strip() not in options:
        yes_or_no_input = input("Please enter [yes] or [no]\n")
    if yes_or_no_input == "yes":
        return yes_or_no_input
    if yes_or_no_input == "no":
        return yes_or_no_input


def number_regex(number):
    numberregex = re.compile(r"\d+")
    mo = numberregex.findall(number)
    return int(mo[0])


def spinner(load_time):
    for iteration in range(load_time * 5):
        sys.stdout.write('\rwaiting |')
        time.sleep(.1)
        sys.stdout.write('\rwaiting /')
        time.sleep(.1)
        sys.stdout.write('\rwaiting -')
        time.sleep(.1)
        sys.stdout.write('\rwaiting \\')
        time.sleep(.1)
    sys.stdout.write('\r')


def one_through_4():
    options = ["1", '2', '3', '4']
    user_input = ''
    while user_input not in options:
        user_input = input("\n \n")
        if user_input.strip() == "1":
            return int(user_input)
        elif user_input.strip() == "2":
            return int(user_input)
        elif user_input.strip() == "3":
            return int(user_input)
        elif user_input.strip() == "4":
            return int(user_input)
        else:
            input("")


def table_printer(file_path):
    table = pandas.read_csv(file_path)
    print(table)


def number_validation(set_range):
    user_input = input("\n")
    if user_input == "":
        print("please enter a number\n")
        number_validation(set_range)
    try:
        int(user_input)
    except TypeError:
        print("please enter a number\n")

        number_validation(set_range)
    if int(user_input) not in range(set_range):
        print("The number you entered is not an available option\n")
        number_validation(set_range)
    elif int(user_input) == 0:
        print("you can not enter 0 as a choice\n")
        number_validation(set_range)
    return int(user_input)
