def array_front_9(nums):

    if len(nums) == 0:
        return  False

    if len(nums) <= 3:
        if nums.count(9) > 0:
            return  True
        else:
            return  False

    if len(nums) >= 4:
        validNumbers = nums[0:3]
        if validNumbers.count(9) > 0:
            return True
        else:
            return  False