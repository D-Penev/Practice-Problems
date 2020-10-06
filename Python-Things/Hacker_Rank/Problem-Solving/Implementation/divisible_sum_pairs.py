def divisible_sum_pairs():
    nums = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    pair_counter = 0
    all_pairs = {x: x for x in range(0, nums[0])}
    curr_arr_index = 0
    all_values = list(all_pairs.values())
    for i in range(nums[0]):
       for j in range(len(all_values)):
           if i < all_values[j] and (numbers[i] + numbers[all_values[j]]) % nums[1] == 0:
               pair_counter += 1
    return pair_counter


print(
    divisible_sum_pairs()
)
