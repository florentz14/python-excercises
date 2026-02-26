python_class = {"Python", "HTML", "CSS", "JavaScript", "SQL"}
web_class = {"HTML", "CSS", "JavaScript", "PHP", "SQL"}

# intersection of the two sets
common_subjects = python_class & web_class
print("Common subjects:", common_subjects)

# union of the two sets
all_subjects = python_class | web_class
print("All subjects:", all_subjects)

# difference of the two sets
python_only = python_class - web_class
print("Python only subjects:", python_only)

# symmetric difference of the two sets
web_only = web_class - python_class
print("Web only subjects:", web_only)

# display the sets
print("Python class:", python_class)