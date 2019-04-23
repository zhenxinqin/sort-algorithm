#coding=utf-8

class BinaryTreeNode(object):
	"""docstring for BinaryTreeNode"""
	def __init__(self, data, left=None, right=None):
		'''
		'''
		self.data = data
		self.left = None
		self.right = None


class BinaryTree(object):
	"""docstring for BinaryTree"""
	def __init__(self):
		'''
		初始化
		'''
		self._root = None
		
	def is_empty(self):
		'''
		判断二叉搜索树是否为空
		'''
		return self._root is None

	def inorder_travel(self, node):
		'''
		二叉树的中序遍历，node：遍历的起始节点
		'''
		if node is None:
			return
		self.inorder_travel(node.left)
		print node.data,
		self.inorder_travel(node.right)

	def insert(self, value):
		'''
		向二叉搜索树中插入值为value的节点
		'''
		node = BinaryTreeNode(value) # 生成节点对象

		if self.is_empty():
			#二叉树为空
			self._root = node
			return

		cur = self._root #游标指向根节点
		while 1:
			#判断要插入的值与当前游标所指节点的值大小
			if node.data > cur.data:
				# 大于，如果无右子树，则插入，否则继续向右
				if cur.right is None:
					cur.right = node
					return
				cur = cur.right
			elif node.data < cur.data:
				if cur.left is None:
					cur.left = node
					return
				cur = cur.left
			else:
				#如果要插入的值已经存在，直接return
				return

	def search(self, item):
		'''
		搜索值为item的节点是否存在
		'''
		cur = self._root #游标

		while cur is not None:
			if cur.data == item:
				return True
			elif cur.data > item:
				cur = cur.left
			else:
				cur = cur.right

		#退出while时，cur指向None
		return None


	def delete(self, value):
		'''
		删除二叉搜搜树中值为value的节点
		'''
		p, q = None, self._root #维持p为q的父节点
		
		while q is not None and q.data != value:
			p = q #维持p为q的父节点
			if q.data > value:
				q = q.left
			else:
				q = q.right
		#退出while循环时q为none或者q指向要删除的节点
		if q is None:
			print 'dont exist'
			return
		if q.left is None and q.right is None:
			#q为叶子节点,或根节点
			if p is None:
				#二叉树只有一个节点，且要删除的节点是二叉树的根节点
				self._root = None
				return
			if q is p.left:
				p.left = None
				return
			else:
				p.right = None
				return
		elif q.left is not None and q.right is None:
			if p is None:
				#要删除的节点是二叉树的根节点
				self._root = q.left
				return
			if q is p.left:
				p.left = q.left
				return
			else:
				p.right = q.left
				return
		elif q.right is not None and q.left is None:
			if p is None:
				#要删除的节点是二叉树的根节点
				self._root = q.right
				return
			if q is p.left:
				p.left = q.right
				return
			else:
				p.right = q.right
				return
		else:
			#q左右非空
			r = q.left #找到左子树的最大节点
			while r.right is not None:
				r = r.right
			#退出while时，r指向左子树最大节点
			q.data = r.data # r的值覆盖q的值
			self.delete(r.data) # 删除节点r
			
			# r.right = q.right
			# if q is p.left:
			# 	p.left = r
			# 	return
			# else:
			# 	p.right = r
			# 	return





if __name__ == '__main__':
	
	bst = BinaryTree()
	bst.insert(1)
	bst.insert(2)
	bst.insert(3)
	bst.insert(4)
	bst.insert(5)
	bst.insert(6)
	bst.insert(7)
	# print bst.insert(7)
	bst.insert(8)
	bst.insert(9)
	bst.insert(10)
	bst.insert(11)
	bst.insert(12)
	bst.inorder_travel(bst._root)
	print ''
	bst.delete(12)
	bst.delete(3)
	bst.delete(6)
	bst.delete(4)
	bst.delete(5)
	bst.delete(2)
	bst.delete(1)
	bst.insert(3)
	bst.insert(6)
	bst.insert(4)
	bst.insert(5)
	bst.insert(2)
	bst.insert(1)
	bst.insert(12)
	bst.inorder_travel(bst._root)
