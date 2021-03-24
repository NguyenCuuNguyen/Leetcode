class openLock {
    public int openLock(String[] deadends, String target) {
        //state and destination --> BFS to find the shortest path/finding a node in a graph--> States as graph and navigate to destination 
        
        //put deadlock nums into a hashset for constant lookup O(1)
        //Add all the deadends num into Hashset with a for loop or with func:
        HashSet<String> deadlock = new HashSet(Arrays.asList(deadends));
        
        //once a number is considered, don't go back to it anymore
        HashSet<String> visited = new HashSet();
        int level = 0;
        visited.add("0000");
        //Add starting point to queue cuz BFS
        Queue<String> toVisit = new LinkedList();
        toVisit.offer("0000");
        
        while(!toVisit.isEmpty()){
            int size = toVisit.size();
            //iterate through all toVisit possibilities 
            //check if it's deadlock first
            while (size > 0){
                String lock = toVisit.poll();
                if (deadlock.contains(lock)){
                    //decrement the num being visited
                    size--;
                    continue; //break out of inner while
                }
                if(lock.equals(target)){
                    return level;
                }
               
                StringBuilder sb = new StringBuilder(lock);
                //Find all possible moves by incrementing or decrementing each of 4 digit in num
                for(int i = 0; i<4; i++){
                    char cur = sb.charAt(i);
                    //For each digit, we can either go up or down.
                    //cur-'0' to get int from char
                    String s1 = sb.substring(0, i) + (cur=='9'? 0 : cur-'0'+1) + sb.substring(i+1);
                    String s2 = sb.substring(0, i) +(cur=='0'? 9: cur-'0'-1) + sb.substring(i+1);
                    //
                    if(!visited.contains(s1) && (!deadlock.contains(s1))){
                        toVisit.offer(s1);
                        //so the same combo found in next iterations won't be repeated 
                        visited.add(s1); 
                    }
                    if(!visited.contains(s2) && (!deadlock.contains(s2))){
                        toVisit.offer(s2);
                        visited.add(s2);
                    }
                }
               size--;
            }
            
            level++;  
        }
        return -1;
    }
}