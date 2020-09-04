def required_literature():
    numberOfPages = int(input())
    pagesInOneHour = int(input())
    numberOfDays = int(input())

    totalReadingTime = numberOfPages / pagesInOneHour
    print(totalReadingTime / numberOfDays)



required_literature()