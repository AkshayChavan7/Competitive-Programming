// Leetcode
// https://leetcode.com/problems/add-two-numbers/

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

class SLL
{
public:
    ListNode *head;

    SLL()
    {
        head = NULL;
    }

    SLL(ListNode *n)
    {
        head = n;
    }

    void appendNode(ListNode *new_node)
    {
        ListNode *ptr;
        ptr = head;

        if (head == NULL)
        {
            head = new_node;
            head->next = NULL;
        }
        else
        {
            while (ptr->next != NULL)
            {
                ptr = ptr->next;
            }
            new_node->next = NULL;
            ptr->next = new_node;
        }
    }
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        SLL l3;
        ListNode *ptr1, *ptr2;
        ptr1 = l1;
        ptr2 = l2;
        int sum, carry = 0;
        bool isCarryLeft = 0;
        while (ptr1 != NULL || ptr2 != NULL)
        {
            isCarryLeft = 0;
            if (ptr1 != NULL && ptr2 != NULL)
            {
                sum = ptr1->val + ptr2->val + carry;
                l3.appendNode(new ListNode(sum % 10));
                carry = sum / 10;

                ptr1 = ptr1->next;
                ptr2 = ptr2->next;
            }
            else
            {
                if (ptr2 == NULL && ptr1 != NULL)
                {
                    sum = ptr1->val + carry;
                    l3.appendNode(new ListNode(sum % 10));
                    carry = sum / 10;

                    ptr1 = ptr1->next;
                }
                if (ptr1 == NULL && ptr2 != NULL)
                {
                    sum = ptr2->val + carry;
                    l3.appendNode(new ListNode(sum % 10));
                    carry = sum / 10;
                    ptr2 = ptr2->next;
                }
            }

            if (ptr1 == NULL && ptr2 == NULL && sum > 9)
            { // check if carry is left after final digit addition
                isCarryLeft = 1;
            }
        }

        if (isCarryLeft)
        {
            l3.appendNode(new ListNode(carry));
        }

        return l3.head;
    }
};