// https://leetcode.com/problems/reverse-integer/
class Solution {
public:
    int reverse(int x) {
        if(x>2147483647 || x<-2147483648)     // 2^31-1 =  2147483647    -2^31 = -2147483648
            return 0;
        string s = to_string(x);
        string rs = "";
        for(int i=s.length()-1;i>=0; i--) {
            rs+=s[i];
        }
        try {
            if(rs[rs.length()-1]=='-')
                return stoi("-"+rs.substr(0,rs.length()-1));
            return stoi(rs);
        } catch(exception e) {
            return 0;
        }   
    }
};