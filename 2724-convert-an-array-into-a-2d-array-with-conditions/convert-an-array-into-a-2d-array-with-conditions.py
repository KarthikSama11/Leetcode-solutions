class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
      res = []
      dic = {}
      for num in nums:
        if num not in dic: dic[num] = 0
        dic[num] += 1
      temp = []
      while len(dic):
        temp = []
        for num, count in list(dic.items()):
          temp.append(num)
          dic[num] -= 1
          if dic[num] == 0:
            del dic[num]
        res.append(temp.copy())
        temp.clear()  
      return res
        