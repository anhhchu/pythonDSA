
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = [int(char) for char in version1.split('.')]
        for num in reversed(version1):
            if num == 0: version1.pop()
            else: break
        #version2.replace('.','')
        version2 = [int(char) for char in version2.split('.')]
        for num in reversed(version2):
            if num == 0: version2.pop()
            else: break
        
        if version1 == version2:
            return 0

        elif version1 > version2:
            return 1

        elif version1 < version2:
            return -1

     

sol = Solution()
print(sol.compareVersion("7.5.2.4","7.5.3"))
print(sol.compareVersion("1.001","1.01"))
print(sol.compareVersion("1.0.1","1.1"))
print(sol.compareVersion("1.0.1","1"))
