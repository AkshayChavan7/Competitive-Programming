// Leetcode
// https://leetcode.com/problems/zigzag-conversion/

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows==1)
            return s;
        string arr[numRows];
        bool flag = true;
        int cnt = 0;
        for(int i=0; i<s.length(); i++) {
            arr[cnt]+=s[i];
            
            if(flag)
                cnt++;
            else 
                cnt--;
            if(cnt==0)
                flag = true;
            else if(cnt==numRows-1)
                flag = false;
        }
        string output = "";
        for(int i = 0; i<numRows; i++) {
            output+=arr[i];
        }
        return output;
    }
};