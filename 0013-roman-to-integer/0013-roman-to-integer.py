class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        # 마지막 루프 - 1
        # 만약 IV가 올 경우, I가 V 보다 작으니깐, V - I로 값을 구하고
        # 만약 VI가 올 경우, V > I 보다 커서 V + I를 더해준다.
        # 단 마지막 값 VII 경우 마지막 값 까지 더해야 해서 roman_map[s[-1]] 잊지 않고 더해준다.
        for i in range(len(s) - 1):
            current_v = roman_map[s[i]]
            next_v = roman_map[s[i + 1]]
            if current_v < next_v:
                total -= current_v
            else:
                total += current_v
        total += roman_map[s[-1]]
        return total