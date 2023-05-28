def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    l = []
    i1 = 0
    i2 = 0
    while len(l) < (len(nums1) + len(nums2)):
        if i1 == len(nums1):
            l.extend(nums2[i2:])
            break
        if i2 == len(nums2):
            l.extend(nums1[i1:])
            break
        if nums1[i1] <= nums2[i2]:
            l.append(nums1[i1])
            i1 += 1
        else:
            l.append(nums2[i2])
            i2 += 1
    length = len(l)
    d = length // 2
    m = length % 2
    print(l)
    if m == 1:
        return l[d]
    else:
        return (l[d] + l[d - 1]) / 2


print(findMedianSortedArrays([3, 4], []))
