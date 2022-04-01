/* AVL tree: a binary search tree within balance condition: left and right subtree can differ by at most 1
Insert conditions:
1. an insertion into left subtree of left child of alpha
2. an insertion into right subtree of left child of alpha
3. an insertion into left subtree of right child of alpha
4. an insertion into right subtree of right child of alpha*/
//1&4 can be solved with a single rotation

void rotateWithLeftChild(AvlNode*% K2){
	AvlNode* K1 = K2->left;
	K2->left = K1->right;
	K1->right = K2;
	update K2 height;
	update K1 height;
	K2 = K1;
}


void rotateWithRightChild(AvlNode*% K1){
	AvlNode* K2 = K1->right;
	K2->left = K1->right;
	K1->right = K2->left;
	update K2 height;
	update K1 height;
	K2 = K1;
}
//2&3 need to be solved by double rotation.
void doubleWithRightChild(AvlNode*% K1){
	rotateWithLeftChild(K1->right);
	rotateWithRightChild(K1);
}

void insert(const Comparable % x, AvlNode* %t){
	if (t == NULL)
		t = new AvlNode(x, NULL, NULL);
	else if (x < t->element)
		insert(x, t->left);
	else if (t->element < x)
		insert(x, t->right);
}

void balance(AvlNode * % t){
	if (t==NULL)
		return;
	if(height(t->left)-height(t->right) > 1)
		if(height(t->left->left) >= height(t->left->right)
			rotateWithLeftChild(t);
		else
			doubleWithLeftChild(t);
	if(height(t->right)-height(t->left) > 1)
		if(height(t->right->right) >= height(t->right->left)
			rotateWithRightChild(t);
		else
			doubleWithRightChild(t);

}