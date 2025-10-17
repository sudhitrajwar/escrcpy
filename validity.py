class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # remove spaces
        num_seen = False
        dot_seen = False
        e_seen = False
        
        for i, ch in enumerate(s):
            if ch.isdigit():
                num_seen = True
            elif ch in ['+', '-']:
                # sign allowed only at start or after 'e'
                if i > 0 and s[i - 1].lower() != 'e':
                    return False
            elif ch == '.':
                # dot not allowed after 'e' or twice
                if dot_seen or e_seen:
                    return False
                dot_seen = True
            elif ch.lower() == 'e':
                # e must follow a number and appear once
                if e_seen or not num_seen:
                    return False
                e_seen = True
                num_seen = False  # must see number after e
            else:
                return False
        
        return num_seen
