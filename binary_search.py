#coding=utf-8

def binary_search(sorted_list,find_value):
	'''
	二分查找递归版
	sorted_list：从小到大排好序的数组
	find_value：要查找的元素
	'''
	n = len(sorted_list)
	mid = n / 2

	while n > 0:

		
		if sorted_list[mid] == find_value:
			return True
		elif sorted_list[mid] < find_value:
			return binary_search(sorted_list[mid+1:],find_value)
		else:
			return binary_search(sorted_list[:mid],find_value)

	return False


def bin_search(sorted_list,find_value):
	'''
	非递归版本二分查找
	'''

	left = 0
	right = len(sorted_list)-1


	while left <= right:

		middle = (left + right) / 2

		if sorted_list[middle] == find_value:
			return True
		elif sorted_list[middle] > find_value:
			right = middle - 1
		else:
			left = middle + 1

	return False


if __name__ == '__main__':
	print binary_search([1,2],1)
	print bin_search([1,2,3,4,5],3)