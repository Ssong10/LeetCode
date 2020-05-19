# 100ms, 14.1MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        numslen = len(nums1) + len(nums2)
        for _ in range(round((numslen-1.5)/2)):
            if not nums1:
                nums2.pop()
            elif not nums2:
                nums1.pop()
            else:
                a,b = nums1.pop(), nums2.pop()
                if a>b:
                    nums2.append(b)
                else:
                    nums1.append(a)
        if numslen % 2:
            if not nums2:
                return nums1[-1]
            if not nums1:
                return nums2[-1]
            return max(nums2.pop(),nums1.pop())
        else:
            total = 0
            for _ in range(2):
                if nums1:
                    a = nums1.pop()
                else:
                    a = 0
                if nums2:
                    b = nums2.pop()
                else:
                    b = 0
                if a>b :
                    total += a
                    nums2.append(b)
                else:
                    total += b
                    nums1.append(a)
            return total/2

# 84 ms	13.9 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = sorted(nums1 + nums2)
        numlen = round((len(nums3)-1.5)/2)
        if numlen:
            mid = nums3[numlen:-numlen]
        else:
            mid = nums3
        if mid:
            return sum(mid)/len(mid)