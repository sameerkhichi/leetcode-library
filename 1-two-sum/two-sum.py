class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        ans = [] 
        counter_1 = 0
        

        for first_number in nums:

            counter_2 = 0

            for second_number in nums:
                
                if counter_1 != counter_2:

                    if first_number + second_number == target:

                        ans.append(counter_1)
                        ans.append(counter_2)
                        break

                counter_2 += 1

            if ans:
                break
                
            counter_1 += 1

        return ans