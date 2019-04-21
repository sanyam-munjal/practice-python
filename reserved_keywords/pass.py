#pass is a null statement. The difference between a comment and pass statement in Python is that, while the interpreter ignores a comment entirely, pass is not ignored.
#However, nothing happens when pass is executed. It results into no operation (NOP).
#Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. They cannot have an empty body. The interpreter would complain. So, we use the pass statement to construct a body that does nothing. We can do the same thing in an empty function or class as well.

# pass is just a placeholder for
# functionality to be added later.

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
