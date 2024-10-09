#include <bits/stdc++.h> // Includes all standard C++ libraries
using namespace std;

// Definition of the TreeNode class
class TreeNode {
    public:
    int val; // Value of the node
    TreeNode* left; // Pointer to the left child
    TreeNode* right; // Pointer to the right child

    // Default constructor
    TreeNode() {
        val = 0;
        left = right = NULL;
    }

    // Parameterized constructor
    TreeNode(int val) {
        this->val = val;
        left = right = NULL;
    }
};

// Function to build a binary tree from a given array
TreeNode* buildTree(vector<int>& arr) {
    queue<TreeNode*> queue; // Queue to facilitate level order insertion
    TreeNode* root = new TreeNode(arr[0]); // Create the root node
    queue.push(root); // Push the root node to the queue
    int i = 1; // Index to track the current position in the array

    // Loop until the queue is empty or all elements are processed
    while (!queue.empty() && i < arr.size()) {
        TreeNode* curr = queue.front(); // Get the front node from the queue
        queue.pop(); // Remove the front node from the queue

        // Check and insert the left child
        if (i < arr.size() && arr[i] != -1) {
            curr->left = new TreeNode(arr[i]);
            queue.push(curr->left);
        }
        i++;

        // Check and insert the right child
        if (i < arr.size() && arr[i] != -1) {
            curr->right = new TreeNode(arr[i]);
            queue.push(curr->right);
        }
        i++;
    }
    return root; // Return the root of the constructed tree
}

// Function to perform preorder traversal of the tree
void preorder(TreeNode* root) {
    if (!root) return; // Base case: if the node is null, return
    cout << root->val << " "; // Print the value of the node
    preorder(root->left); // Recursively traverse the left subtree
    preorder(root->right); // Recursively traverse the right subtree
}

int main() {
    int h; // Variable to store the height of the tree
    cout << "Enter height: ";
    cin >> h; // Input the height of the tree
    int size = pow(2, h) - 1; // Calculate the size of the array based on the height
    vector<int> arr(size); // Create an array to store the tree elements
    cout << "Enter array elements: ";
    for (int i = 0; i < size; i++) cin >> arr[i]; // Input the elements of the array
    TreeNode* root = buildTree(arr); // Build the tree from the array
    preorder(root); // Perform preorder traversal of the tree
}