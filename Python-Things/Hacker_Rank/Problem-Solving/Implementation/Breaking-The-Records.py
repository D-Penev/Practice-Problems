def breaking_the_records():
    n = int(input())
    scores = list(map(int, input().split()))


    curr_max_score = scores[0]
    curr_min_score = scores[0]
    max_records_beaten = 0
    min_records_beaten = 0

    for i in range(0, len(scores)):
        if scores[i] > curr_max_score:
            curr_max_score = scores[i]
            max_records_beaten += 1

        if scores[i] < curr_min_score:
            curr_min_score = scores[i]
            min_records_beaten += 1

    print(max_records_beaten, min_records_beaten)


breaking_the_records()
