nums = [int(i) for i in open('17-d3.txt')]

cnt = 0
max_sum = -10**11

razmah = max(nums)-min(nums)

for i in range(len(nums)-2):
    num_1 = nums[i]
    num_2 = nums[i+1]
    num_3 = nums[i+2]
    if num_1 < razmah and num_2 < razmah and num_3 < razmah:
        if int('2' in num_1) + int('2' in num_2) + int('2' in num_3) >= 2:
            cnt += 1
            max_sum = max(max_sum, num_1+num_2+num_3)