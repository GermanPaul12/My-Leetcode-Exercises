#Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.

# https://leetcode.com/problems/binary-search/?envType=study-plan&id=algorithm-i

def search(nums, target):
        start,end=0,len(nums)-1
        while start<=end:
            mid = (end+start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start=mid+1
            else:
                end=mid-1 
        return -1        

print(search([-1,0,3,5,9,12],9))        