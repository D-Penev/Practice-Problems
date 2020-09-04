def calculate_deposit():
    depositedSum = float(input())
    depositTerm = int(input())
    fixedYearRate = float(input())

    a = (depositedSum * fixedYearRate) / 100
    b = a / 12
    print(depositedSum + b * depositTerm)

calculate_deposit()