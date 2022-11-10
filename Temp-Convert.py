'''---------------------------------------------------

 Gabriela Muriel

----------------------------------------------------------'''


class color:
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m' 

def convertFromCelsius():

    num_1 = int(input('\n\t\t\tEnter your' + color.BOLD + ' first ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Celsius' + color.END + ':    \n\n\t\t\t\t'))
    num_2 = int(input('\n\t\t\tEnter your' + color.BOLD + ' second ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Celsius' + color.END + ':    \n\n\t\t\t\t'))
    num_3 = int(input('\n\t\t\tEnter your' + color.BOLD + ' third ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Celsius' + color.END + ':    \n\n\t\t\t\t'))

    celsuis_f_1 = num_1 * (9.0/5.0) + 32
    celsuis_f_2 = num_2 * (9.0/5.0) + 32
    celsuis_f_3 = num_3 * (9.0/5.0) + 32
    celsuis_k_1 = num_1 + 273.15
    celsuis_k_2 = num_2 + 273.15
    celsuis_k_3 = num_3 + 273.15

    print(color.BOLD + color.UNDERLINE + '\n\t\t\tCelsius\t\t\t\tFahrenheit\t\t\tKelvin\n' + color.END)
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_1, celsuis_f_1, celsuis_k_1))
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_2, celsuis_f_2, celsuis_k_2))
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_3, celsuis_f_3, celsuis_k_3))

    print("\n_______________________________________________________________________________________________________________________\n\n")
    print("༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶")
    print("\n_______________________________________________________________________________________________________________________\n\n")

def convertFromFahrenheit():

    num_1 = int(input('\n\t\t\tEnter your' + color.BOLD + ' first ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Fahrenheit' + color.END + ':    \n\n\t\t\t\t'))
    num_2 = int(input('\n\t\t\tEnter your' + color.BOLD + ' second ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Fahrenheit' + color.END + ':     \n\n\t\t\t\t'))
    num_3 = int(input('\n\t\t\tEnter your' + color.BOLD + ' third ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Fahrenheit' + color.END + ':    \n\n\t\t\t\t'))

    fahrenheit_c_1 = (num_1 - 32) * (5.0/9.0)
    fahrenheit_c_2 = (num_2 - 32) * (5.0/9.0)
    fahrenheit_c_3 = (num_3 - 32) * (5.0/9.0)
    fahrenheit_k_1 = (num_1 + 459.67) * (5.0/9.0)
    fahrenheit_k_2 = (num_2 + 459.67) * (5.0/9.0)
    fahrenheit_k_3 = (num_3 + 459.67) * (5.0/9.0)

    print(color.BOLD + color.UNDERLINE + '\n\t\t\tFahrenheit\t\t\tCelsius\t\t\t\tKelvin\n' + color.END)
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_1, fahrenheit_c_1, fahrenheit_k_1))
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_2, fahrenheit_c_2, fahrenheit_k_2))
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_3, fahrenheit_c_3, fahrenheit_k_3))

    print("\n_______________________________________________________________________________________________________________________\n\n")
    print("༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶")
    print("\n_______________________________________________________________________________________________________________________\n\n")

def convertFromKelvin():

    num_1 = int(input('\n\t\t\tEnter your' + color.BOLD + ' first ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Kelvin' + color.END + ':    \n\n\t\t\t\t'))
    num_2 = int(input('\n\t\t\tEnter your' + color.BOLD + ' second ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Kelvin' + color.END + ':    \n\n\t\t\t\t'))
    num_3 = int(input('\n\t\t\tEnter your' + color.BOLD + ' third ' + color.END + 'temperature expressed in degree' + color.BOLD + ' Kelvin' + color.END + ':    \n\n\t\t\t\t'))

    kelvin_f_1 = num_1 * (9.0/5.0) - 459.67
    kelvin_f_2 = num_2 * (9.0/5.0) - 459.67
    kelvin_f_3 = num_3 * (9.0/5.0) - 459.67
    kelvin_c_1 = num_1 - 273.15
    kelvin_c_2 = num_2 - 273.15
    kelvin_c_3 = num_3 - 273.15

    print(color.BOLD + color.UNDERLINE + '\n\t\t\tKelvin\t\t\t\tFahrenheit\t\t\tCelsius\n' + color.END)
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_1, kelvin_f_1, kelvin_c_1))
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_2, kelvin_f_2, kelvin_c_2))
    print('\t\t\t{:.2f}\t\t\t\t{:.2f}\t\t\t\t{:.2f}\n'.format(num_3, kelvin_f_3, kelvin_c_3))

    print("\n_______________________________________________________________________________________________________________________\n\n")
    print("༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶")
    print("\n_______________________________________________________________________________________________________________________\n\n")

def getMenuSelection():
    print("\n_______________________________________________________________________________________________________________________\n\n")
    print("༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶")
    print("\n_______________________________________________________________________________________________________________________\n\n")

    print("\t\t\t\t" + color.BOLD + "1)" + color.END + "\tConvert from Celsius\n")
    print("\t\t\t\t" + color.BOLD + "2)" + color.END + "\tConvert from Fahrenheit\n")
    print("\t\t\t\t" + color.BOLD + "3)" + color.END + "\tConvert from Kelvin\n")
    print("\t\t\t\t" + color.BOLD + "4)" + color.END + "\tQuit Program\n\n")

    user_input = int(input("Enter " + color.UNDERLINE + "Number" + color.END + ":\t\t\t"))

    print("\n_______________________________________________________________________________________________________________________\n\n")
    print("༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶༶•┈┈⛧┈♛ ♛┈⛧┈┈•༶")
    print("\n_______________________________________________________________________________________________________________________\n\n")

    return user_input

def main():
    menuSelection = 0

    while True:
        menuSelection = getMenuSelection()
        
        if menuSelection == 1:
            convertFromCelsius()

        elif menuSelection == 2:
            convertFromFahrenheit() 

        elif menuSelection == 3:
            convertFromKelvin()

        elif menuSelection == 4:
            break #Exit Condition

        else: 
            print("Please enter a number between 1 and 4")

if __name__ == "__main__":
    main()
