import types
import math

# -----------------------------------------------
# 1. User-Defined Function Checker
# Write a Python program to check if a function is a user-defined function or not.
# Use types.FunctionType, types.LambdaType()
# -----------------------------------------------
print("🔹 1. User-Defined Function Checker")

def my_function():
    return "Hello!"

lambda_func = lambda x: x * 2

print("Is 'my_function' a user-defined function?", isinstance(my_function, types.FunctionType))
print("Is 'lambda_func' a lambda function?", isinstance(lambda_func, types.LambdaType))
print("Is 'print' a user-defined function?", isinstance(print, types.FunctionType))  # False

print()

# -----------------------------------------------
# 2. User-Defined Method Checker
# Write a Python program to check if a given value is a method of a user-defined class.
# Use types.MethodType()
# -----------------------------------------------
print("🔹 2. User-Defined Method Checker")

class MyClass:
    def method(self):
        pass

obj = MyClass()

print("Is 'obj.method' a method?", isinstance(obj.method, types.MethodType))
print("Is 'math.sqrt' a method?", isinstance(math.sqrt, types.MethodType))  # False

print()

# -----------------------------------------------
# 3. Generator Function Checker
# Write a Python program to check if a given function is a generator or not.
# Use types.GeneratorType()
# -----------------------------------------------
print("🔹 3. Generator Function Checker")

def my_gen():
    yield 1
    yield 2

gen_instance = my_gen()
normal_func = lambda: 10

print("Is 'gen_instance' a generator?", isinstance(gen_instance, types.GeneratorType))
print("Is 'normal_func()' a generator?", isinstance(normal_func(), types.GeneratorType))  # False

print()

# -----------------------------------------------
# 4. Compiled Code and Module Checker
# Write a Python program to check if a given value is compiled code or not.
# Also check if a given value is a module or not.
# Use types.CodeType, types.ModuleType()
# -----------------------------------------------
print("🔹 4. Compiled Code and Module Checker")

code_obj = compile("x = 5", "<string>", "exec")

print("Is 'code_obj' a compiled code object?", isinstance(code_obj, types.CodeType))
print("Is 'math' a module?", isinstance(math, types.ModuleType))
print("Is 'my_function' a compiled code object?", isinstance(my_function, types.CodeType))  # False

print()

"""
🔹 1. User-Defined Function Checker
Is 'my_function' a user-defined function? True
Is 'lambda_func' a lambda function? True
Is 'print' a user-defined function? False

🔹 2. User-Defined Method Checker
Is 'obj.method' a method? True
Is 'math.sqrt' a method? False

🔹 3. Generator Function Checker
Is 'gen_instance' a generator? True
Is 'normal_func()' a generator? False

🔹 4. Compiled Code and Module Checker
Is 'code_obj' a compiled code object? True
Is 'math' a module? True
Is 'my_function' a compiled code object? False
"""