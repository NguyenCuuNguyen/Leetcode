import java.util.*;
import java.io.*;
import java.lang.*;


//SOLUTION 1: Dynamic Node Representation (Linked Representation).
public static class Node{
    int value;
    Node left;
    Node right;

    // Constructor Declaration of Class
    public Node(int value){
        this.value = value;
        private left = null;
        private right = null;      
    }
    public void printVal() {System.out.print(value + " ")}
    public int getVal(){ return value;}
}
public class BinaryTree{
    public Node root;
    //Constructors:
    BinaryTree(int key){
        root = new Node(key);
    }
    BinaryTree(){ root = null;}

    // Inserting an element.
    // Removing an element.
    // Searching for an element.
    // Deletion for an element.
    // Traversing an element. There are four (mainly three) types of traversals 
}


//SOLUTION 2: Arrau implementation (Sequential Representation).
public class TreeArray{
    
}

public static void main(String[] args){
    BinaryTree tree = new BinaryTree();
    tree.root = new Node(1)
    tree.root.left = new Node(2)
    tree.root.right = new Node(3);
    tree.root.left.left = new Node(4)
}

