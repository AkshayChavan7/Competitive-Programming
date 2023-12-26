// https://leetcode.com/problems/palindrome-linked-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public: 
    bool isPalindrome(ListNode* head) {
        vector<int> a;
        while(head != NULL) {
            a.push_back(head->val);
            head = head->next;   
        }
        for(int i=0, j=a.size()-1; i<a.size()/2; i++, j--) {
            if(a.at(i)!=a.at(j))
                return false;
        }
        return true;
    }
};