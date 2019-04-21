#coding=utf-8

def bubble_sort(*args):
	'''
	冒泡排序
	'''
	nums = list(args)
	n = len(nums)
	for j in range(n-1):#每次把最大的数传到尾部，一共需要n-1次循环
		count = 0
		for i in range(n-1-j):#n个数，已确定大小的有j个，需要n-1-j次循环

			if nums[i] > nums[i+1]:
				nums[i],nums[i+1] = nums[i+1],nums[i]
				count += 1
		if count == 0:#count为零表示没有数据已经排好，退出排序
			return nums
	return nums

if __name__ == '__main__':
		print bubble_sort(9,8,7,6,5,4,3,2,1)


