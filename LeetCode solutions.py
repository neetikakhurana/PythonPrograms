#412 FUZZBIZZ
class Solution(object):
    def fizzBuzz(self,n):
            #:type n: int
            string=""
            rtype=[]
            for i in range(1,n+1):
                if i%3==0:
                    if i%5==0:
                        rtype.append("FizzBuzz")
                    else:
                        rtype.append("Fizz")
                elif i%5==0:
                    rtype.append("Buzz")
                else:
                    rtype.append(str(i))
            return rtype
s=Solution()
print s.fizzBuzz(15)

#104 MAXDEPTH
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            s=Solution()
            lheight=s.maxDepth(root.left)
            rheight=s.maxDepth(root.right)
            if lheight>rheight:
                return lheight+1
            else:
                return rheight+1
            
#344 REVERSE STRING
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

#389. Find the Difference
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list1=list(s)
        list2=list(t)
        list1.sort()
        list2.sort()
        for i in range(0,len(t)):
            if i<len(s):
                if list1[i]!=list2[i]:
                    return list2[i]
            else:
                return list2[i]

