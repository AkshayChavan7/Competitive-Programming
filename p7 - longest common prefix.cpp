// https://leetcode.com/problems/longest-common-prefix/

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==1) {
            return strs.at(0);
        }
        string output = "";
        string s = strs.at(0);
        for(int i=0; i<s.length(); i++) {
           for(int j = 1; j<strs.size(); j++) {
               if(s[i]!=strs.at(j)[i]) { 
                    return output;
               } 
           }
            output+=s[i];
       }
        return output;
    }
};