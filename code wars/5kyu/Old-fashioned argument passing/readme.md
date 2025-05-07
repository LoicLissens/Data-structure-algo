You get a function fun that was written some decades ago. Back then, it was considered cool if the functions received their arguments from standard input, and printed their result to standard output instead of returning it.

The function fun was written in this old-fashioned style. Your task is to convert it to modern style, where the arguments are passed explicitly and the result is returned.

Consider the original function as a black box. Write a decorator unfool that converts it to modern style. Take into account:

Multiple functions were used for input and output; some of them were not standard (print, input but also others).
All imports were of the form import foo, and not from foo import bar nor import foo as f.
File handles were referenced by their original name, no aliases involved. This was to make it less likely that the file accidentally remains open.
Each argument comes in a different line.
All arguments and the return value are of type int.
Example

def example_fun():
    n = int(input())
    if n == 0:
        print(42)
    elif n == 1:
        print(2, file=sys.stdout)
    else:
        sys.stdout.write("7")
(This one comes preloaded). The function unfool(example_fun) must take a single argument and return a number according to the input / output of example_fun. So unfool(example_fun)(0) = 42, unfool(example_fun)(1) = 2 and unfool(example_fun)(2) = 7. If there were two (or more) input(), unfool(example_fun) would take two (or more) arguments.

