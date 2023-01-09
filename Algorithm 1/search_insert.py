#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

# https://leetcode.com/problems/search-insert-position/?envType=study-plan&id=algorithm-i

def searchInsert(nums, target):
        start,end=0,len(nums)-1
        while start<=end:
            mid = (end+start)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start=mid+1
            else:
                end=mid-1 
        if (target<nums[mid] and mid==0) or (target>nums[mid-1] and target<nums[mid]):
            return mid
        elif target<nums[mid]:
            return mid-1
        else:
            return mid+1  
        
print(searchInsert([1,3,5,6],0))     
print(searchInsert([1,3],2))    