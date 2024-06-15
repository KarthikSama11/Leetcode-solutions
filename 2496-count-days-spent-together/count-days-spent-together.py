class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
      alice = [int(arriveAlice[0:2]),int(arriveAlice[3:]),int(leaveAlice[0:2]),int(leaveAlice[3:])]
      bob = [int(arriveBob[0:2]),int(arriveBob[3:]),int(leaveBob[0:2]),int(leaveBob[3:])]
      days =[0,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
      a1 = [0,0]
      b1= [0,0]
      for i in range(alice[0]):
        a1[0]+= days[i]
      a1[0] += alice[1]
      for i in range(alice[2]):
        a1[1] += days[i]
      a1[1] += alice[3]
      for i in range(bob[0]):
        b1[0]+= days[i]
      b1[0]+= bob[1]
      for i in range(bob[2]):
        b1[1] += days[i]
      b1[1] += bob[3]
      ans = min(b1[1],a1[1]) - max(a1[0],b1[0])+1
      if ans >0: 
        return ans
      return 0
