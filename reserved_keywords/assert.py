#assert
#assert is used for debugging purposes.
#While programming, sometimes we wish to know the internal state or check if our assumptions are true. assert helps us do this and find bugs more conveniently. assert is followed by a condition.
#If the condition is true, nothing happens. But if the condition is false, AssertionError is raised. 
#For our better understanding, we can also provide a message to be printed with the AssertionError.


def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark2 = [55,88,78,90,79]
print("Average of mark2:",avg(mark2))

mark1 = []
print("Average of mark1:",avg(mark1))
