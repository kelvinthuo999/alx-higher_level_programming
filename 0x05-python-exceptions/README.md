# NOTES

- An error refers to issues that prevent the code from being executed or result in unexpected behaviour 
  due to violations of language syntax or runtime conditions.
- An exception is a disruptive event that is mitigated using try-except for graceful handling.
- Exceptions are used to make the code more robust and resilient.
- A basic structure of handling exceptions:
<pre>
try:
    # Code that might raise an exception
    # ...
except SomeExceptionType:
    # Code to handle the specific exception
    # ...
except AnotherExceptionType:
    # Code to handle another specific exception
    # ...
else:
    # Code to run if no exceptions were raised
    # ...
finally:
    # Code that runs regardless of whether an exception occurred or not
    # ...
</pre>
- 
