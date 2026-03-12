class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pointerA = len(a) - 1
        pointerB = len(b) - 1
        res = []
        carry = 0
        while pointerA >= 0 or pointerB >= 0:
            sum = carry 
            if pointerA >= 0:
                sum += int(a[pointerA])
                pointerA -= 1
            if pointerB >= 0:
                sum += int(b[pointerB])
                pointerB -= 1
            carry = sum // 2
            bitRes = sum % 2
            res.append(str(bitRes))            
           
        if carry > 0:
            res.append(str(carry % 2))

        return ''.join(res[::-1])