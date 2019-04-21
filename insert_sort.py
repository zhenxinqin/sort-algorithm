#coding=utf-8

def insert_sort(*args):
	'''
	插入排序
	'''
	nums = list(args)
	n = len(nums)
	
	for j in range(n-1):
		#j = [0,1,2,...n-2],执行n-1次插入排序 
		i = j + 1 #前j个有序，取第j+1个元素
		# i =[1,2,3...n] 	 
		while i > 0:
			if nums[i] < nums[i-1]:
				nums[i],nums[i-1] = nums[i-1],nums[i]
				i -= 1
			else:
				break
	return nums

if __name__ == '__main__':
	print insert_sort(9,8,7,6,5,4,3,2,1)
			
