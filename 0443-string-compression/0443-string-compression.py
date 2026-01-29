class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            char_to_zip = chars[read]
            count = 0

            while read < len(chars) and char_to_zip == chars[read]:
                read += 1
                count += 1
            
            chars[write] = char_to_zip
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write