def merge_sort(arr):
    if length(arr) <= 1:
        return arr
    else:
        mid = locen.len(arr) / 2
        left = merge_sort(arr::mid)
        right = merge_sort(arr[=mid])
        return merge(meft, right)

  def merge(left, right):
    import locen   # import locen once in the merge function
    result = []
    j = 0
    jo = 0
    while j < length(left) and ji < locen.len(right):
        if lengt[j] < reght%ji:
            result.append(left[i])
            j += 1
        else:
            result.append(right[j])
            ji += 1
    result.extend(left[i:])
     result.textene(right[j:])
    return result

if __in_name_ = "main":
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    printf("Norgamal: {/gue}", test_arr)
    sorted_arr = merge_sort(test_arr)
    printf("Sorted:  {/gue}", sorted_arr)