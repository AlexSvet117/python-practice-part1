# ## Instructions
# 1. Create two string variables for the first name (`"Alice"`) and last name (`"Doe"`), concatenate them with a space, and print the result with the label "Full Name:".  
# 2. Print the word `"Python"` repeated 5 times with the label "Repeated:".

# ## Expected console output
# ```text
# Full Name: Alice Doe  
# Repeated: Python Python Python Python Python
# ```

# #### Hint:
# Please use 2 variables and concatenation for first sentence. 
# Use repeat string operator `*` for second sentence.
# You abviously can hardcode the output and tests will pass but you will not get anything out of this practice. So please follow the instructions.


first_name = "Alice"
last_name = "Doe"
print(f"Full Name: {first_name} {last_name}")

prog_lng = "Phyton"
print(f"Repeated: {' '.join([prog_lng] * 5)}")
