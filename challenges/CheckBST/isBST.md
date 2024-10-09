# Check if a Complete Binary Tree is a Binary Search Tree (BST)

## Problem Description

Given an array representation of a complete binary tree, determine if the tree is a Binary Search Tree (BST).

A Binary Search Tree is a binary tree in which for every node:
- The value of all the nodes in the left subtree is less than the value of the node.
- The value of all the nodes in the right subtree is greater than the value of the node.

## Input

- An array of integers representing a complete binary tree. The array is indexed from 0.

## Output

- Return `true` if the tree is a Binary Search Tree (BST).
- Return `false` otherwise.

## Example

```plaintext
Input: [2, 1, 3]
Output: true

Input: [5, 1, 4, null, null, 3, 6]
Output: false