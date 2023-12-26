// https://leetcode.com/problems/string-to-integer-atoi/

class Solution {
public:
    
    bool isInt(char ch) {
        if(int(ch) >=48 && int(ch)<=57)
            return true;
        return false;
    }
    
    // 2^31-1 = 2147483647              -2^31 = -2147483648
    int myAtoi(string s) {
        
        bool numTriggeredFlag = false, negFlag = false, signOccuredFlag = false;
        long int num = 0;
        for(int i =0; i<s.length(); i++) {
            if(!isInt(s[i]) && signOccuredFlag && !numTriggeredFlag) 
                return 0;
            if(s[i]=='-' || s[i]=='+') {
                signOccuredFlag = true;
                
                if(s[i]=='-' && !numTriggeredFlag) 
                    negFlag = true;
            }
            
            if(isInt(s[i])) {
                numTriggeredFlag = true;
                
                if((num*10)>2147483647 || (negFlag && (num * 10)>2147483648))
                {
                    if(negFlag)
                        return -2147483648;
                    else
                        return 2147483647;
                } 
                else
                    num = (num * 10) + (int(s[i])-48);   
            }
            
            if((s[i]!=' ' && s[i]!='-' && s[i]!='+') && !numTriggeredFlag)
                return 0;
            
            
            if(numTriggeredFlag && !isInt(s[i]))
                break;
        }
        
        
        if(negFlag){
            if(num>2147483648)
                return -2147483648;
            return (-1) * num;
        }
        else {
            if(num>2147483647)
                return 2147483647;
            return num;
        }
        
        return 0;
    }
};