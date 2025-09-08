class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        for i in range(1, n):
            a = i
            b = n - a
            x = i
            y = n - x

            # check if a and b have zeros
            is_a_have_zero = False
            is_b_have_zero = False

            print(f"a:{a} b:{b}")

            while a > 0:
                print(f"a:{a}")
                if a % 10 == 0:
                    is_a_have_zero = True
                    break

                a = a//10

            while b > 0:
                print(f"b:{b}")
                if b % 10 == 0:
                    is_b_have_zero = True
                    break

                b = b//10

            if not is_a_have_zero and not is_b_have_zero:
                return [x , y]

        return None