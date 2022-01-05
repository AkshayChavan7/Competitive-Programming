// Leetcode
// https://leetcode.com/problems/roman-to-integer/
class Solution
{
public:
    int romanToInt(string s)
    {

        // 1st solution - without hashmap
        int sum = 0;
        string order = "IVXLCDM";
        int val[7] = {1, 5, 10, 50, 100, 500, 1000};

        sum += val[order.find(s[s.length() - 1])];
        int curr_index = 0, prev_index = 0;
        for (int i = s.length() - 2; i >= 0; i--)
        {
            curr_index = order.find(s[i]);
            prev_index = order.find(s[i + 1]);
            if (prev_index > curr_index)
            {
                sum -= val[curr_index];
            }
            else
            {
                sum += val[curr_index];
            }
        }
        return sum;

        // 2nd solution - with hashmap
        // int sum = 0;
        // unordered_map<char, int> T = {
        //     {'I',1},
        //     {'V',5},
        //     {'X',10},
        //     {'L',50},
        //     {'C',100},
        //     {'D',500},
        //     {'M',1000},
        // };
        // sum+=T[s[s.length()-1]];
        // for(int i = s.length()-2; i>=0;i--) {
        //     if(T[s[i]]<T[s[i+1]]) {
        //         sum -= T[s[i]];
        //     } else {
        //         sum+=T[s[i]];
        //     }
        // }
        // return sum;
    }
};