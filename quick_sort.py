#coding=utf-8

def quick_sort(nums,first,last):
	'''
	快速排序
	first：排序队列起始地址
	last：排序队列的终止地址
	'''

	#递归退出的条件
	if first >= last:
		return

	mid_value = nums[last]#设置最后一个元素为基准，先移动low游标
	low = first 
	high = last
	# print 'last',last
	

	while low != high:

		#low右移
		while low < high and nums[low] <= mid_value:
		# while nums[low] <= mid_value:出错
			low += 1

		#大于mid_value的值放到mid_value右边
		if low < high:

			nums[high] = nums[low]
			high -= 1

		#high左移
		while  low < high and nums[high] > mid_value:
		# while nums[high] > mid_value:出错
			high -= 1

		#小于mid_value的值放到mid_value左边
		if low < high:

			nums[low] = nums[high]
			low += 1
		
	#退出循环时low==high，此时位置为基准元素的位置
	nums[low] = mid_value
	
	#对基准元素左右边递归
	quick_sort(nums,first,low-1)
	quick_sort(nums,low+1,last)
	return nums


if __name__ == '__main__':
	nums = [4,8,7,6,5,9,3,2,1,0]
	print quick_sort(nums,0,len(nums)-1)
	print nums
	
