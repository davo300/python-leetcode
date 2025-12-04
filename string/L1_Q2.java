/*2. Practical application 1: Arithmetic operations.
(a) [3 marks] Design an algorithm that takes a string, which represents an arithmetic
operation, as input and checks whether or not the brackets are correct (balanced) or incorrect
(unbalanced). The input string may contain a combination of the following characters:
{,},[,],(,),0,1,2,3,4,5,6,7,8,9,+,-,*,/. An obvious hint for this algorithm is to use the stack-
based solution discussed in class as a template, and hence you can use the stack implemented
in #1. Your algorithm must not check the correctness of the arithmetic operators/operands,
but only check for balanced brackets. Your algorithm should also show an error message
when the string contains a character that is not one of those listed above. Provide the
pseudocode of the algorithm.
(b) [3 marks] Implement the algorithm of (a) in your favorite programming language. Run
the program in several cases, including the following (more examples to be asked when the
assignment is submitted):
i. (9*[3*{[(3+3)/5]*7}]) iii. ((3*(9-(4*(6-5))))
ii. {3*(2+[3-[4/[6/9]]]}) iv. {2-{3*{6/[[[(((9-0)))]]]}}/7}
(c) [2 marks] Consider an input string of size n: (i) what is the worst-case time that your
algorithm takes to decide whether or not the string is correct (balanced) or incorrect
(unbalanced)? (ii) Why? Give your answers in terms of the O-notation. 

(a) Pseudocode: --------------------

Algorithm BracketMatch(X,n):

Input: An array X of n tokens, each of which is either a grouping symbol, a
variable, an arithmetic operator, or a number

Output: true if and only if all the grouping symbols in X match
Let S be an empty stack

Let S be an empty stack

    for i=0 to n-1 do

    if X[i] is an opening grouping symbol then

        S.push(X[i])

    else if X[i] is a closing grouping symbol then

        if S.isEmpty() then

            return false {nothing to match with}

        if S.pop() and X[i] does not match the allowed types of characters then

            return false {wrong type} { We use input and top variables to compare with top element here }

    else if X[i] is not one of the other characters

            print 'invalid character!'
            return false {if user imput has invalid character}
 
if the stack is empty after processing the expression, it's balanced
        
    return s.isEmpty();

*/




//(b)
import java.util.EmptyStackException;

public class L1_Q2 {

    // Stack interface defining common stack operations
    public interface Stack {
        public int size(); // Returns the number of elements in the stack
        public boolean isEmpty(); // Checks if the stack is empty
        public Object top() throws EmptyStackException; // Returns the top element without removing it
        public void push(Object o) throws FullStackException; // Adds an element to the stack
        public Object pop() throws EmptyStackException; // Removes and returns the top element
    }

    // Custom exception for a full stack
    public static class FullStackException extends Exception {
        public FullStackException() {
            super("Stack is full"); // Error message for full stack
        }
    }

    // Implementation of the Stack interface using an array
    public class ArrStack implements Stack {
        private Object[] myStack; // Array to hold stack elements
        private int topIndex; // Index of the top element in the stack

        // Constructor that accepts a size parameter to initialize the stack
        public ArrStack(int maxSize) {
            myStack = new Object[maxSize]; // Initialize the stack array with custom size
            topIndex = -1; // Stack is initially empty
        }

        // Returns the number of elements in the stack
        public int size() {
            return topIndex + 1; // topIndex starts from -1, so size is topIndex + 1
        }

        // Checks if the stack is empty
        public boolean isEmpty() {
            return topIndex == -1; // Empty if topIndex is -1
        }

        // Returns the top element without removing it
        public Object top() throws EmptyStackException {
            if (isEmpty()) {
                throw new EmptyStackException(); // Throws exception if the stack is empty
            }
            return myStack[topIndex]; // Returns the top element
        }

        // Adds a new element to the stack
        public void push(Object o) throws FullStackException {
            if (topIndex == myStack.length - 1) { // Checks if the stack is full
                throw new FullStackException(); // Throws exception if stack is full
            } else {
                topIndex++; // Moves the index up
                myStack[topIndex] = o; // Adds the new element at the top
            }
        }

        // Removes and returns the top element
        public Object pop() throws EmptyStackException {
            if (isEmpty()) { // Checks if the stack is empty
                throw new EmptyStackException(); // Throws exception if empty
            } else {
                Object popped = myStack[topIndex]; // Get the top element
                topIndex--; // Move the index down
                return popped; // Return the popped element
            }
        }
    }

    // Method to check if brackets in an expression are balanced
    public boolean BracketMatch(String expression) throws FullStackException {
        ArrStack stack = new ArrStack(expression.length()); // Stack size based on the length of the expression

        // Iterate through each character of the expression
        for (int i = 0; i < expression.length(); i++) {
            char input = expression.charAt(i); // Get the current character

            // If it's an opening bracket, push it to the stack
            if (input == '{' || input == '[' || input == '(') {
                stack.push(input);
            } 
            // If it's a closing bracket, check if it matches the top of the stack
            else if (input == '}' || input == ']' || input == ')') {
                if (stack.isEmpty()) {
                    return false; // If the stack is empty, it's an unbalanced expression
                }
                char top = (char) stack.pop(); // Pop the top element and compare
                // Check for matching pairs of brackets
                if (input == ')' && top != '(' || input == ']' && top != '[' || input == '}' && top != '{') {
                    return false; // Return false if they don't match
                }
            } 
            // Check for invalid characters in the expression
            else if (!(input == '+' || Character.isDigit(input) || input == '-' || input == '*' || input == '/')) {
                System.out.println("Error: Incorrect Character");
                return false; // Return false if an invalid character is found
            }
        }
        // If the stack is empty after processing the expression, it's balanced
        return stack.isEmpty();
    }

    // Main method to test the BracketMatch function
    public static void main(String[] args) {
        L1_Q2 BracketMatch = new L1_Q2(); // Create an instance of L1_Q2

        try {
            // Test expressions for balanced brackets
            String expression1 = "(9*[3*{[(3+3)/5]*7}])";
            System.out.println("\n"+expression1 + " is balanced: " + BracketMatch.BracketMatch(expression1)+"\n");

            String expression2 = "{3*(2+[3-[4/[6/9]]]})";
            System.out.println(expression2 + " is balanced: " + BracketMatch.BracketMatch(expression2)+"\n");

            String expression3 = "((3*(9-(4*(6-5))))";
            System.out.println(expression3 + " is balanced: " + BracketMatch.BracketMatch(expression3)+"\n");

            String expression4 = "{2-{3*{6/[[[(((9-0)))]]]}}/7}";
            System.out.println(expression4 + " is balanced: " + BracketMatch.BracketMatch(expression4)+"\n");

            String expression5 = "(";
            System.out.println(expression5 + " is balanced: " + BracketMatch.BracketMatch(expression5)+"\n");

            String expression6 = "4+5";
            System.out.println(expression6 + " is balanced: " + BracketMatch.BracketMatch(expression6)+"\n");

            String expression7 = "}{";
            System.out.println(expression7 + " is balanced: " + BracketMatch.BracketMatch(expression7)+"\n");

        } catch (FullStackException | EmptyStackException e) {
            System.err.println(e.getMessage()); // Catch and print any exceptions
        }
    }
}
