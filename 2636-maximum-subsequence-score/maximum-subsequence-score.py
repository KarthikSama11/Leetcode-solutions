class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
      minheap = []
      nums = []
      for i in range(len(nums1)):
        nums.append((nums2[i],nums1[i]))
      nums.sort(reverse = True)
      ans = 0
      total = 0
      for i in range(k):
        total += nums[i][1]
        heappush(minheap,nums[i][1])
      factor = nums[k-1][0]
      ans = factor * total
      for i in range(k,len(nums)):
        total -= heappop(minheap)
        ele = nums[i][1]
        heappush(minheap,ele)
        total += ele
        ans = max(ans, total*nums[i][0])
      return ans



        
