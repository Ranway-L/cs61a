new_tree = copy_tree(t)
for tr in new_tree:
	if is_leaf(tr):
		if label(tr) == old:
			tr[0] = new
	elif is_tree(tr):
		tr = replace_leaf(tr,old,new)
return new_tree
yggdrasil = tree('odin',
                  [tree('balder',
						[tree('thor'),
                         tree('loki')]),
                   tree('frigg',
                        [tree('thor')]),
                   tree('thor',
						[tree('sif'),
						tree('thor')]),
			   tree('thor')])