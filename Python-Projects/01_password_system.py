"""
User-Friendly Password System

A website is programming an authentication system that will accept a password either if it's the correct password or if it's the correct password with a single character appended to it. Your task is to implement such a system using a hashing function. Given a list of events in which either a password is set or authorization is attempted, determine if each authorization attempt will be successful or not.

Hashing Function:
Let f(x) be a function that takes a character and returns its decimal character code in the ASCII table.
For instance: f('a') = 97, f('B') = 66, f('9') = 57

Let h(s) be the hashing function where p = 131 and M = 10^9 + 7:
h(s) = (s[0]*p^(n-1) + s[1]*p^(n-2) + s[2]*p^(n-3) + ... + s[n-2]*p + s[n-1]) mod M

Example: 
For s = "cAr1":
h(s) = (99*131^3 + 65*131^2 + 114*131 + 49) mod 10^9+7 = 223691457

Event Types:
1. setPassword(s): Sets the password to s
2. authorize(x): Returns 1 if x is either the hash of the current password OR the hash of the current password with a single character appended to it. Otherwise returns 0.

Example:
Events:
1. setPassword("cAr1")
2. authorize(223691457) → returns 1 (matches hash of "cAr1")
3. authorize(303580761) → returns 1 (matches hash of "cAr1a")
4. authorize(100) → returns 0 (no match)
5. setPassword("d")
6. authorize(100) → returns 1 (matches hash of "d")

Output: [1, 1, 0, 1]

Function:
authEvents(events) where events is a 2D array of strings
Returns: array of integers (1 or 0) for each authorization attempt

Constraints:
- 2 ≤ q ≤ 10^5
- 1 ≤ length of s ≤ 9
- 0 ≤ x < 10^9+7
- First event is always setPassword
- At least one authorize event
- s contains only lowercase/uppercase letters and digits
"""

def authEvents(events):

    p= 131
    M = 10**9+7
    current_password = ""
    result = ''

    def compute_hash(s):
        if not s:
            return 0
        
        hash_value = 0
        n=len(s)

        for i in range(n):
            char_code = ord(s[i])
            power = n-1-i
            hash_value = (hash_value+char_code*pow(p,power,M))%M
        return hash_value
    
    def is_authorized(x):
        if compute_hash(current_password) ==x:
            return True
        
        for c in range(ord('a'),ord('z')+1):
            extended = current_password + chr(c)
            if compute_hash(extended) ==x:
                return True
            
        for c in range(ord('0'),ord('9')+1):
            extended = current_password +chr(c)

            if compute_hash(extended) ==x:
                return True
            
        for event in events: 
            event_type = event[0]
            if event_type == 'setPassword':
                current_password = event[1]
            elif event_type=="authorized":
                x=int(event[1])
                if is_authorized(x):
                    result.append(0)
    return result


# Test with the example from the problem
# Create a 2D list where each inner list represents an event
events = [
    ["setPassword", "cAr1"],      # Set password to "cAr1"
    ["authorize", "223691457"],    # Check if 223691457 is valid
    ["authorize", "303580761"],    # Check if 303580761 is valid
    ["authorize", "100"],          # Check if 100 is valid
    ["setPassword", "d"],          # Change password to "d"
    ["authorize", "100"]           # Check if 100 is valid again
]

# Call the function with the test events
result = authEvents(events)

# Print the result
print(f"Result: {result}")

# Print what we expected based on the problem description
print(f"Expected: [1, 1, 0, 1]")

# Verify the hash calculations from the example
# Re-define constants for the verification section
p = 131
M = 10**9 + 7

# Define the hash function again for standalone verification
def compute_hash(s):
    # Return 0 for empty string
    if not s:
        return 0
    
    # Initialize hash accumulator
    hash_value = 0
    
    # Get string length
    n = len(s)
    
    # Calculate hash using the formula
    for i in range(n):
        char_code = ord(s[i])  # Get ASCII code
        power = n - 1 - i       # Calculate power
        hash_value = (hash_value + char_code * pow(p, power, M)) % M
    
    # Return final hash
    return hash_value

# Print header for verification section
print(f"\nHash verification:")

# Verify hash of "cAr1"
# Expected: h('cAr1') = (99*131^3 + 65*131^2 + 114*131 + 49) mod (10^9+7)
print(f"h('cAr1') = {compute_hash('cAr1')} (expected: 223691457)")

# Verify hash of "cAr1a" (password with 'a' appended)
print(f"h('cAr1a') = {compute_hash('cAr1a')} (expected: 303580761)")

# Verify hash of "d"
# h('d') = 100 because ord('d') = 100 and there's no power term (just the character itself)
print(f"h('d') = {compute_hash('d')} (expected: 100)")