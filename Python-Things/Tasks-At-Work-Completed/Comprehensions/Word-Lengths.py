def word_lengths():
   return (', '.join([(f'{x} -> {len(x)}') for x in input().split(', ')]))

print(
    word_lengths()
)