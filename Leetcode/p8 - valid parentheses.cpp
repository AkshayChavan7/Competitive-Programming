// Letcode
// https://leetcode.com/problems/valid-parentheses/

class Solution {
public:
    bool isValid(string s) {
        stack<char> stck;
        map<char,char> pair = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'}
        };
        for(int i =0; i<s.length(); i++) {
            switch(s[i]) {
                // if opening bracket then we keep pushing it onto the stack
                case '(': stck.push('(');
                    break;
                case '[': stck.push('[');
                    break;
                case '{': stck.push('{');
                    break;
                default: 
                // if closing bracket then we check whether the top element matches it or not
                    if(stck.empty())
                        return false;
                    if(pair[stck.top()] != s[i])
                        return false;
                    stck.pop();
            }
        }
        // finally if stack is empty then we have parsed valid parentheses. otherwise, not.
        if(stck.empty())
            return true;
        else
            return false;
    }
};