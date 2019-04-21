#coding=utf-8

def shell_sort(*args):
	nums = list(args)
	n = len(nums)

	gap = n / 5 #shell_sort分组的间隔

	while gap >= 1:
		for j in range(gap,n):
			#j = [gap,gap+1,...n-1]
			i = j #i指向gap后面的要处理的第一个数据
			while i > 0:
				if nums[i] < nums[i-gap]:
					nums[i],nums[i-gap] = nums[i-gap],nums[i] #小数与大数交换，往前移
					i -= gap
				else:
					break
		#处理完所有的分组后，重新设置分组间隔
		gap /= 2

	return nums

if __name__ == '__main__':
	print shell_sort(9,8,7,6,5,100,4,3,2,1,0)
