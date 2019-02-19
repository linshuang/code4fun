def mergeSort(nums):
    if len(nums) == 1:
        return nums

    nums_len = len(nums)
    mid = nums_len // 2
    sorted_half1 = mergeSort(nums[0:mid])
    sorted_half2 = mergeSort(nums[mid:])

    # merge
    sorted_nums = []
    i = j = 0
    while True:
        if sorted_half1[i] <= sorted_half2[j]:
            sorted_nums.append(sorted_half1[i])
            i+=1
        else:
            sorted_nums.append(sorted_half2[j])
            j+=1
        if i == len(sorted_half1):
            sorted_nums.extend(sorted_half2[j:])
            break
        if j == len(sorted_half2):
            sorted_nums.extend(sorted_half1[i:])
            break

    return sorted_nums

print(mergeSort([1,2,3,4,5,6,7]))
print(mergeSort([11,2,31,14,53,56,77,77,11,2]))
print(mergeSort([11,2,31,14,53,56,77,77,11,2,0]))
print(mergeSort([11,2,31,14,53,56,77,77,11,2,1110]))