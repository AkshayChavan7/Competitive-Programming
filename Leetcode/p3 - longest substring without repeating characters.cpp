// https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution {
public:
    int mLen = 0;
    
    // recursion function
    void maxSubStringLength(string s, int prevMaxLen) {
        
        int maxLen = 0;
        string substr = "";
        int recursionFlag = 0;
        for(int i=0; i<s.length(); i++) {
            if(substr.find(s[i])<=substr.length()) {        // substr contains char
                recursionFlag = 0;
                for(int j = i-1; j>=0; j--) {
                    if(s[j] == s[i]) {
                        // cout<<"maxSubStringLength("<<s.substr(j+1)<<","<<substr.length()<<")"<<endl;
                        maxSubStringLength(s.substr(j+1),substr.length());     
                        recursionFlag = 1;
                        break;
                    }
                }
                if(recursionFlag) {
                    break;
                }
            } else {
                substr +=s[i];
            }
        }
        
        if(substr.length()>prevMaxLen) {
            if(substr.length()>mLen) {
                mLen = substr.length();
            }
        } 
        // else {
        //     // return prevMaxLen;
        //     // mLen = prevMaxLen;
        // }
    }
    
    int lengthOfLongestSubstring(string s) {
        
        maxSubStringLength(s,0);
        return mLen;
    }
};