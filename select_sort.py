#coding=utf-8

def select_sort(*args):
	'''
	选择排序
	'''
	nums = list(args)
	n = len(nums)

	for j in range(n-1):
		#j = [0,1,2,3,...,n-2]
		min_index = j#假定未处理的第一个数字为最小
		for i in range(j+1,n):
			#i = [j+1,j+2,...,n-1]
			if nums[min_index] > nums[i]:
				min_index = i
		#退出时，min_index是未处理数字中最小值的下标
		nums[min_index],nums[j] = nums[j],nums[min_index]#交换
	return nums

if __name__ == '__main__':
	print select_sort(9,8,7,6,5,4,3,2,1)

