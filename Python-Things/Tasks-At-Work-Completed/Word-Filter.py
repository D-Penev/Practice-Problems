def word_filter():
    print("\n".join([x for x in input().split() if len(x) % 2 == 0]))

word_filter()