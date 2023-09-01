class NumberSystemConverter:
    def __init__(self):
        print('''
Counting in different number systems

This program shows you equivalent numbers in decimal (base 10),
hexadecimal (base 16), and binary (base 2) numeral systems.

(Ctrl-C to quit.)''')

    def get_positive_integer_input(self, prompt, default=None):
        while True:
            response = input(prompt)
            if response == '':
                if default is not None:
                    return default
                else:
                    print('Please enter a number.')
                    continue
            if response.isdecimal():
                return int(response)
            print('Please enter a valid number greater than or equal to 0.')

    def display_numbers_in_systems(self):
        start = self.get_positive_integer_input(
            'Enter the starting number (e.g. 0) > ', 0)
        amount = self.get_positive_integer_input(
            'Enter how many numbers to display (e.g. 1000) > ', 1000)

        for number in range(start, start + amount):
            hex_number = hex(number)[2:].upper()
            bin_number = bin(number)[2:]

            print(f'DEC: {number}   HEX: {hex_number}   BIN: {bin_number}')


if __name__ == '__main__':
    converter = NumberSystemConverter()
    converter.display_numbers_in_systems()
