class Solution:
    def compress(self, arr: List[str]) -> int:
      i, j, size = 0, 0, len(arr)
      while i < size:
        count = 0
        cur = arr[i]
        while i < size and arr[i] == cur:
          count += 1
          i += 1
        arr[j] = cur
        j += 1
        if count > 1:
          count = str(count)
          for ch in count:
            arr[j] = ch
            j += 1

      return j


        


      
        
