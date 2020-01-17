def find_first_missing_positive(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1

    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      print("\t>> swapping number {} and {}".format(nums[i], nums[j]))
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  print(nums)
  for i in range(n):
    print('num: {}, i+1:{}'.format(nums[i],i+1))
    if nums[i] != i + 1:
      return i + 1

  return nums.length + 1


def main():
    print(find_first_missing_positive([-8, 1, 5, 40, 2]))
    # print("="*10)
    # print(find_first_missing_positive([3, -2, 0, 1, 2]))
    # print("="*10)
    # print(find_first_missing_positive([3, 2, 5, 1]))


main()



