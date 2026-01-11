def reversePairs(nums):

    def merge_sort(arr, left, right):
        
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = 0
        count += merge_sort(arr, left, mid)
        count += merge_sort(arr, mid + 1, right)

        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += j - (mid + 1)

        arr[left:right + 1] = sorted(arr[left:right + 1])
        return count

    return merge_sort(nums, 0, len(nums) - 1)

# nums = [1, 3, 2, 3, 1]
# print(reversePairs(nums))

nums = [2, 4, 3, 5, 1]
print(reversePairs(nums))
