class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x) # integer타입이라서 거꾸로 읽을려면 str으로 변환시키기, 슬라이싱은 시퀀스 타입에만 적용가능
        if string_x == string_x[::-1]:
            return True
        else:
            return False
       

        
        