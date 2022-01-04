// Leetcode 
// https://leetcode.com/problems/palindrome-number/
class Solution
{
public:
    bool isPalindrome(int x)
    {

        // Method 1 - converting number to string and then checking for palindrome
        // string s = to_string(x);
        // for(int i = 0, j=s.length()-1; i<s.length(); i++, j--) {
        //     if(s[i]!=s[j]) {
        //         return false;
        //     }
        //     if(i>=j) {
        //         break;
        //     }
        // }
        // return true;

        // Method 2 - by reversing int
        if (x < 0)
            return false;
        unsigned int sum = 0, n = x;
        while (n != 0)
        {
            sum = (sum * 10) + (n % 10);
            n = n / 10;
        }
        return sum == x;
    }
};