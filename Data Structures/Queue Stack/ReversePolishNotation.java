class ReversePolishNotation {
    //Stack = LIFO 
    //EX: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    public int evalRPN(String[] tokens) {
        int a, b;
        Stack<Integer> st = new Stack<>();
        for(String S: tokens){ //each item in list
            if(S.equals("+")){
                st.add(st.pop()+st.pop()); //stack now has 3+9=12=> ["10","6", 12,"-11"] 
            }else if (S.equals("*")){
                st.add(st.pop()*st.pop());
            }else if(S.equals("-")){
                a = st.pop();
                b = st.pop();
                st.add(b-a);
                
            }else if(S.equals("/")){
                a = st.pop();
                b = st.pop();
                st.add(b/a); //THE ORDER MATTTERS
            }else{
                st.add(Integer.parseInt(S));
            }
    }
     return st.pop();   
}
}