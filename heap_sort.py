#coding=utf-8
#优先队列的最小堆实现
#基于优先队列的哈夫曼树

class PrioQueue(object):
	'''
	优先队列,最小堆基于list实现
	'''
	def  __init__(self, elist=[]):
		'''
		初始化
		'''
		self.elems = elist
		if elist:
			self.buildheap()

	def buildheap(self):
		'''
		从已有列表中建立一个堆
		时间复杂度O(n)
		'''
		end = len(self.elems)
		for i in range(end/2, -1, -1):
			# i = [end/2, end/2-1,...,1,0]
			#从end节点的父节点开始调整 
			self.siftdown(self.elems[i], i, end)
		

	def is_empty(self):
		'''
		判断是否为空
		'''
		return  not self.elems

	def enqueue(self, value):
		'''
		把值为value的元素插入最小堆
		'''
		self.elems.append(None)
		self.siftup(value, len(self.elems)-1)
	
	def siftup(self, value, last):
		'''
		向上筛选
		'''
		elems_copy = self.elems
		i = last
		j = (last-1)/2

		while i > 0 and value < elems_copy[j]:
			elems_copy[i] = elems_copy[j]
			i = j
			j = (j-1)/2
		#退出循环时，i==0，或者找到要插入的位置
		elems_copy[i] = value

	def dequeque(self):
		'''
		把根节点的元素弹出
		'''
		if self.is_empty():
			print 'it is  empty'
			return

		min_value = self.elems[0]
		#最后的节点添加到头结点，生成堆
		elems_copy = self.elems
		last_value = elems_copy.pop()
		if len(elems_copy) > 0: # 判断是否还有剩余元素
			self.siftdown(last_value, 0, len(elems_copy)-1)
		return min_value

	def siftdown(self, value, start, end):
		'''
		向下筛选
		value:要调整的值
		'''
		elems_copy = self.elems
		i = start
		j = i * 2 + 1 #左子节点
		while j < end:
			#j 指向左右节点中的最小值
			if j+1 < end and elems_copy[j+1] < elems_copy[j]:
				j += 1
			if value < elems_copy[j]:
				break #如果value是三者中最小，找到value的位置
			else: # j指向的值最小，j指向的值上移
				elems_copy[i] = elems_copy[j]
				i = j
				j = 2 * j + 1
		#退出循环时，i指向value要插入的位置
		elems_copy[i] = value


class HTNode(object):
	"""
	哈夫曼树的节点类
	"""
	def __init__(self, data, left=None, right=None):
		
		self.data = data
		self.left =	left
		self.right = right

	def __lt__(self, other_node):
		'''
		重写 < 运算符
		'''
		return self.data < other_node.data




class HuffmanPrioQ(PrioQueue):
	"""
	哈夫曼优先队列,最小堆
	"""
	def numbers(self):
		'''
		返回哈夫曼优先队列中元素的个数
		'''
		return len(self.elems)


def huffman_tree(weights=[]):
	'''
	哈夫曼树
	'''
	trees = HuffmanPrioQ() #生成一个最小堆来存放哈夫曼树
	for w in weights:
		#生每个值生成一棵哈夫曼树节点
		trees.enqueue(HTNode(w))
	while trees.numbers() > 1:
		t1 = trees.dequeque()
		t2 = trees.dequeque()
		new_tree = HTNode(t1.data+t2.data, t1, t2)
		trees.enqueue(new_tree)
	#退出while时，trees 只剩一个元素
	return trees.dequeque()

def travel(node):
	'''
	层次遍历
	'''
	que = []
	que.append(node)
	while len(que) > 0:
		root = que.pop(0)
		print root.data,
		if root.left is not None:
			que.append(root.left)
		if root.right is not None:
			que.append(root.right)

		


if __name__ == '__main__':
	list1 = [0,1,2,3,4,5,6,7,8,9]
	pl = PrioQueue(list1)
	pl.enqueue(-1)
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.dequeque()
	print pl.elems
	pl.enqueue(0)
	pl.enqueue(1)
	pl.enqueue(2)
	pl.enqueue(3)
	pl.enqueue(4)
	pl.enqueue(5)
	pl.enqueue(6)
	pl.enqueue(7)
	pl.enqueue(100)
	pl.enqueue(-10)
	pl.enqueue(5)
	print pl.dequeque()
	print pl.elems
	weights = [1,2,3,4,5,6,7,8,9]
	hfm_tree = huffman_tree(weights)
	travel(hfm_tree)



