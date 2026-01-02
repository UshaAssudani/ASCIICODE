import os
import msvcrt
from colorama import init, Fore

init()  


SMALL_PATTERNS = [
    "      *               *        * *          *            *   *       *                      *                       *                                       ", 
    "  *** *      ****     *  ****  *  * ****    *     *          ****    *                ***   **** ****  *            *                           *  *        ",
    " **** ****  *      ****  *  * ****  **** *  ****         *   *   *   *   ** ** ***** *   *  *  * *  *  ****  ****  ***  *  *  *   * *   *  * *  *  *  ****  ",
    "*   * *   * *      *  *  * *   *     * *    *  *  *   *  *   ****    *   * * * *   * *   *  **** ****  *     *****  *   *  *   * *  * * *   *    *     *    ",
    " *** *****   ****  ****  ***   *    ****    *  *  *   ****   *   *   *   *   * *   *  ***   *       *  *     ****   **  ****    *   *   *  * *  *     ****  "
]


BIG_DATA = [
    " ***  ****   ***  ****  ***** *****  ***  *   * ***** ***** *   * *     *   * *   *  ***  ****   ***  ****   **** ***** *   * *   * *   * *   * *   * ***** ",
    "*   * *   * *   * *   * *     *     *     *   *   *      *  *  *  *     ** ** **  * *   * *   * *   * *   * *       *   *   * *   * *   *  * *   * *     *",
    "*   * ****  *     *   * ***   ****  *  ** *****   *      *  ***   *     * * * * * * *   * ****  *   * ****  *****   *   *   * *   * * * *   *     *     *",
    "***** *   * *   * *   * *     *     *   * *   *   *   *  *  *  *  *     *   * *  ** *   * *     *   * *  *      *   *   *   *  * *  ** **  * *    *    *",
    "*   * ****   ***  ****  ***** *      ***  *   * *****  ***  *   * ***** *   * *   *  ***  *      ***  *   * ****    *   *****   *   *   * *   *   *   *****"
]


COLORS = {
    "1 RED": Fore.RED, "2 GREEN": Fore.GREEN, "3 Yellow": Fore.YELLOW,
    "4 BLUE": Fore.BLUE, "5 MAGENTA": Fore.MAGENTA, "6 CYAN": Fore.CYAN,
    "7 WHITE": Fore.WHITE 
}


def choose_color():
    os.system("cls")
    print("Choose Color:")
    print("1.Red  2.Green  3.Yellow  4.Blue  5.Magenta  6.Cyan  7.White")
    return COLORS.get(msvcrt.getch().decode(), Fore.CYAN)


def print_small(text, color):
    os.system("cls")
    for row in range(5):
        for ch in text:
            if 'a' <= ch <= 'z':
                n = ((ord(ch) - 96) - 1) * 6
                print(color + SMALL_PATTERNS[row][n:n+6], end=" ")
            else:
                print(" " * 6, end=" ")
        print()
    print(Fore.WHITE)   # color normal


def print_big(text, color):
    os.system("cls")
    for row in BIG_DATA:
        for ch in text:
            start = (ord(ch) - 17) * 6 if ch.isdigit() else (ord(ch.upper()) - 65) * 6
            print(color + row[start:start+6], end="")
        print()
    print(Fore.WHITE)   # color normal


def main_ui():
    while True:
        os.system("cls")
        print("\nASCII ART PROJECT")
        print("1. Small Letter")
        print("2. Capital Letter")
        print("3. Small Word")
        print("4. Capital Word")
        print("5. Numbers")
        print("6. Exit")

        choice = msvcrt.getch().decode()
        color = choose_color()

        if choice == "1":
            c = input("Enter small letter: ").lower()
            print_small(c, color)

        elif choice == "2":
            c = input("Enter capital letter: ").upper()
            print_big(c, color)

        elif choice == "3":
            w = input("Enter small word: ").lower()
            print_small(w, color)

        elif choice == "4":
            w = input("Enter capital word: ").upper()
            print_big(w, color)

        elif choice == "5":
            n = input("Enter numbers: ")
            if n.isdigit():
                print_big(n, color)

        elif choice == "6":
            break

        input("\nPress Enter to continue...")


main_ui()
