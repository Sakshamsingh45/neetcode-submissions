class Solution:
    def isPalindrome(self, s: str) -> bool:
        st,ed=0,len(s)-1
        while st<ed:
            while st<ed and  not s[st].isalnum():
                st+=1
            while ed>st and not s[ed].isalnum():
                ed-=1
            if s[st].lower()==s[ed].lower():
                st+=1
                ed-=1
            else:
                return False
        return True