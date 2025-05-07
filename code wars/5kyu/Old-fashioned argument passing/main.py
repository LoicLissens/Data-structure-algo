import sys
from contextlib import redirect_stdout
from io import StringIO

def unfool(fun):
    def wrapper(*args):
        print(args)
        original_stdin = sys.stdin
        argres = ""
        for arg in args:
            if args:
                argres += str(arg)+"\n"
            else:
                argres += str(0)
        sys.stdin = StringIO(argres)
        f = StringIO()
        with redirect_stdout(f):
            try:
                fun()
                sys.stdin = original_stdin
            except Exception:
                sys.stdin = original_stdin
                raise
        val = f.getvalue().strip()
        return int(val)
    return wrapper

# Best solution seen:
import sys, io

def unfool(fun):
    def wrapper(*args):
        stdin, stdout = sys.stdin, sys.stdout
        sys.stdin = io.StringIO('\n'.join(map(str, args)))
        output = io.StringIO()
        sys.stdout = output
        try: fun()
        finally: sys.stdin, sys.stdout = stdin, stdout
        return int(output.getvalue().strip())
    return wrapper