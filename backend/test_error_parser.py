from error_parser import extract_error_file


sample_traceback = """
Traceback (most recent call last):
  File "sample_project/app.py", line 1, in <module>
    print(username)
NameError: name 'username' is not defined
"""


result = extract_error_file(
    sample_traceback
)

print(result)