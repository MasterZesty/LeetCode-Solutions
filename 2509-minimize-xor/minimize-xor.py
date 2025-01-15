class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        print(bin(num2))

        count_ones = bin(num2).count('1')
        num1_list = list(bin(num1))[2:]
        n = len(num1_list)
        x = ['0']*n
        # print(f"count_ones: {count_ones} n:{n} x:{x} num2_list:{num1_list}")

        for i,v in enumerate(num1_list):
            if count_ones > 0 and v == '1':
                count_ones -= 1
                x[i] = '1'

        for i in range(n-1, 0, -1):
            if count_ones > 0 and num1_list[i] == '0':
                count_ones -= 1
                x[i] = '1'

        # print(f"count_ones: {count_ones} n:{n} x:{x} num2_list:{num1_list}")

        ans = ''.join(x)

        if count_ones > 0:
            ans = '1'*count_ones + ans


        return int(ans, 2)