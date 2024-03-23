"""
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.
 

Example:
Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
"""
"""
    Ideas:
    - in the BrowserHistory, store the current node (index)
    - when we visit a node, delete all history past the current page index
"""
import unittest

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page_index = 0

    def visit(self, url: str) -> None:
        self.history.insert(self.current_page_index + 1, url)
        self.current_page_index += 1
        del self.history[self.current_page_index+1:]
        assert self.history[self.current_page_index] == url

    def back(self, steps: int) -> str:
        for step in range(steps):
            self.current_page_index -= 1
        
        self.current_page_index = max(self.current_page_index, 0)
        return self.history[self.current_page_index]

    def forward(self, steps: int) -> str:
        for step in range(steps):
            self.current_page_index += 1
        
        self.current_page_index = min(self.current_page_index, len(self.history) - 1)
        return self.history[self.current_page_index]
        

class BrowserHistoryTest(unittest.TestCase):
    def setUp(self):
        self.browser_history = BrowserHistory('leetcode.com')

    def test_moving_forward(self):
        self.browser_history.visit('google.com')
        self.browser_history.visit('facebook.com')
        self.browser_history.visit('youtube.com')
        assert self.browser_history.back(1) == 'facebook.com'
        assert self.browser_history.back(1) == 'google.com'
        assert self.browser_history.forward(1) == 'facebook.com'
        self.browser_history.visit('linkedin.com')
        assert self.browser_history.forward(2) == 'linkedin.com'
        assert self.browser_history.back(2) == 'google.com'
        assert self.browser_history.back(7) == 'leetcode.com'

if __name__ == '__main__':
    unittest.main()


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)