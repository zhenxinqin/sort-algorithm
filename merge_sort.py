#coding=utf-8

def merge_sort(alist):

	'''
	归并排序
	'''
	
	#分解到只剩一个元素时
	if len(alist) <= 1:
		return alist

	mid = len(alist) / 2 #将列表分为左右两份的中间值
	#递归
	left_list = merge_sort(alist[:mid]) #left_list是排好序的片段
	right_list = merge_sort(alist[mid:])

	#合并
	left_cur,right_cur = 0,0#左右游标
	result = [] #用来储存排好序的数字 
	while left_cur < len(left_list) and right_cur < len(right_list):

		if left_list[left_cur] <= right_list[right_cur]:
			result.append(left_list[left_cur])
			left_cur += 1
		else:
			result.append(right_list[right_cur])
			right_cur += 1
	#退出while时，可能left_list有剩余，可能right_list有剩余,添加到结果队列
	result += left_list[left_cur:]
	result += right_list[right_cur:]

	return result


if __name__ == '__main__':
	alist = [9,8,7,6,5,4,3,2,1,0]
	sorted_alist = merge_sort(alist)
	print alist
	print sorted_alist
