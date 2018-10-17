class Solution():
    def isPowerOfFour(self, num):

        # To find if there is only one 1 bit.
        if num & (num-1) == 0:
            print("Only one 1 bit in the entire num.")

            # Now that you found out there is only one 1 in the binary conversion of the num.
            # For a number to be pow of 4 it should have one 1 bit followed by even number of 0s.
            # Our task is to now count the number of 0s after we encounter 1.
            count = 0
            while num!=1:
                count+=1
                num = num>>1
            if count % 2 == 0:
                return True
            else:
                return False
        return False            



def main():
    obj = Solution()
    num = 16
    if obj.isPowerOfFour(num):
        print("Its a Pow of 4")
    else:
        print("No its not a Pow of 4")
    pass

if __name__ == '__main__':
    main()