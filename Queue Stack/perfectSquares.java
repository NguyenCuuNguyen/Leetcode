//CIRCLE BACK
//https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/


class perfectSquares {
public int numSquares(int n) {
    Queue<Integer> q = new LinkedList();
    int step = 0;
    Set<Integer> visited = new HashSet();
    q.add(0);
    visited.add(0);
    
    while(!q.isEmpty()){
        int size = q.size();
        ++step;
        for(int i = 0; i < size; ++i){
            int remian = n - q.remove();
            for(int j = 1; j <= Math.sqrt(remian); ++j){
                int v = n - remian + j * j;
                if(v == n) return step;
                if(!visited.add(v)) continue;
                q.add(v);
            }
        }
    }
 
    return n;
}
}

// class Solution {
//     public int numSquares(int n) {
//         // least number of perfect square numbers ==> shortest path = BFS
//         HashSet<Integer> visited = new HashSet();
//         Queue<Integer> toVisit = new LinkedList();
//         int step = 0;
//         visited.add(0);
//         toVisit.add(0);
//         while(!toVisit.isEmpty()){
//             int size = toVisit.size();
//             step++;
//             for(int i = 1; i < size; i++){
//                 //remove node from queue, whose neighbour will be visited now
//                 int remain = n-toVisit.remove(); //12-0=12
//                 for(int j = 1; j <= Math.sqrt(remain); ++j){
//                     int m = n - remain +j*j;
//                     if(m == n) return step;
//                     if(!visited.add(m)) continue;
//                     toVisit.add(m);
//                 }
//             }
//         }
//         return n;
//     }
// }