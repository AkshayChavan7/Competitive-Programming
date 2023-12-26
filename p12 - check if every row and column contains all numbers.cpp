// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/
class Solution {
public:
    
    int getNSum(int n) {
        int sum = 0;
        for(int i =1; i<=n; i++) {
            sum+=i;
        }
        return sum;
    }
    
    bool checkValid(vector<vector<int>>& matrix) {
        int n=  matrix.at(0).size(), tC=0, tR=0, prev = -1;
        int t = getNSum(n);
        cout<<t;
        for(int i=0;i<n;i++) {
            tC = t, tR=t, prev=-1;
            for(int j=0; j<n;j++) {
                tC-=matrix.at(i).at(j);
                tR-=matrix.at(j).at(i);
                if(prev== matrix.at(i).at(j))
                    return false;
                else
                    prev = matrix.at(i).at(j);
            }
            if(tC!=0 || tR!=0)
                return false;
                
        }
        return true;
    }
};