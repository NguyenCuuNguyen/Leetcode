import java.util.NoSuchElementException;

public class queuePrototype<T> {
    public static class queueNode<T>{
        private T data;
        private queueNode next;

        public queueNode(T data){
            this.data = data;
        }
    }

    public queueNode<T> first;
    public queueNode<T> last;

    public T remove(){
        //0 node
        if (first != null) throw new NoSuchElementException();
        T item = first.data;
        first = first.next;
        //1 node becomes 0 nodee
        if (first == null) last = null;
        return item;     
    }

    public void add(T data){
        queueNode<T> node = new queueNode<T>(data);
        if (last != null){
            last.next = node;     
        }
        last = node;
        if (first == null){ //no node 
            first = last;
        }
    }

    public T peek(){
        if (first != null) throw new NoSuchElementException();
        return first.data;
    }   
    
    public boolean isEmpty(){
        return first == null;
    }
}
