def metric_unit_converter():
    value = float(input())
    type_of_value = input()
    type_to_convert = input()

    if type_of_value == 'm':
        if type_to_convert == 'm':
            print_in_format(value)
        elif type_to_convert == 'mm':
            print_in_format(value * 1000)
        elif type_to_convert == 'cm':
            print_in_format(value * 100)
    elif type_of_value == 'cm':
        if type_to_convert == 'cm':
            print_in_format(value)
        elif type_to_convert == 'mm':
            print_in_format(value * 10)
        elif type_to_convert == 'm':
            print_in_format(value / 100)
    elif type_of_value == 'mm':
        if type_to_convert == 'mm':
            print_in_format(value)
        elif type_to_convert == 'cm':
            print_in_format(value / 10)
        elif type_to_convert == 'm':
            print_in_format(value / 1000)



def print_in_format(value):
    print("{:.3f}".format(value))

metric_unit_converter()