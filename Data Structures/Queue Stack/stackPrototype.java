import java.util.*;

public class MyStack<T>{
    public static class stackNode<T>{ //Nested class (means static inner) => can be instantiated without outer instantiation, can access only outer's static 
        private T data;
        private stackNode next;

        public stackNode(T data){
            this.data = data;
        }
    }

    public stackNode<T> top;

    public T pop(){
        if (top == null) throw new EmptyStackException();
        T item = top.data;
        top = top.next;
        return item;
    }

    public void push(T item){
        stackNode<T> t = new stackNode<T>(item);
        t.next = top;
        top = t;
    }

    public T peek(){
        if (top == null) throw new EmptyStackException();
        return top.data;
    }

    public boolean isEmpty(){
        return top == null;
    }
}