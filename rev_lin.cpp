SinglyLinkedListNode* reverse(SinglyLinkedListNode* head) {
    SinglyLinkedListNode* current_node = head;
    SinglyLinkedListNode* prev = nullptr;
    SinglyLinkedListNode* next;
    while (current_node)
    {
        next = current_node->next;
        current_node->next = prev;
        prev = current_node;
        current_node = next;
    }
    head = prev;
    return head;
}
