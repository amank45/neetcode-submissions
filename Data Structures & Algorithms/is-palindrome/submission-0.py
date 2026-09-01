class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = []
        
        for it in s:
            if it.isalnum():
                news.append(it.lower())

        i = 0
        r = len(news) - 1
        
        while i < r:
            if news[i] != news[r]:
                return False
            i += 1
            r -= 1
            
        return True