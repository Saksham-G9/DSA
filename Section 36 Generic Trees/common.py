from tree_node import TreeNode


def get_tree_balanced() -> TreeNode:
	"""Balanced example: root with several subtrees of varying widths."""
	root = TreeNode(1)
	a = TreeNode(2)
	b = TreeNode(3)
	c = TreeNode(4)

	a.children.extend([TreeNode(5), TreeNode(6)])
	b.children.append(TreeNode(7))
	c.children.extend([TreeNode(8), TreeNode(9), TreeNode(10)])

	root.children.extend([a, b, c])
	return root


def get_tree_skewed() -> TreeNode:
	"""Skewed (deep) tree: a long chain of single children."""
	root = TreeNode(11)
	cur = root
	for v in range(12, 18):
		node = TreeNode(v)
		cur.children.append(node)
		cur = node
	return root


def get_tree_wide() -> TreeNode:
	"""Wide tree: root with many leaf children (shallow but wide)."""
	root = TreeNode(21)
	leaves = [TreeNode(v) for v in range(22, 31)]
	root.children.extend(leaves)
	return root


def get_tree_mixed() -> TreeNode:
	"""Mixed structure combining depth and breadth."""
	root = TreeNode(31)
	left = TreeNode(32)
	right = TreeNode(33)

	left.children.extend([TreeNode(34), TreeNode(35)])
	# add grandchildren under left->35
	left.children[1].children.extend([TreeNode(36), TreeNode(37)])

	right_child = TreeNode(38)
	right_child.children.extend([TreeNode(39), TreeNode(40)])
	right.children.append(right_child)

	root.children.extend([left, right])
	return root


# convenience collection
ALL_TREES = [get_tree_balanced, get_tree_skewed, get_tree_wide, get_tree_mixed]


if __name__ == "__main__":
	for builder in ALL_TREES:
		t = builder()
		print(f"\n=== {builder.__name__} ===")
		t.print_tree()

