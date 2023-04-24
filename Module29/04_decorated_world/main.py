from typing import Callable
from functools import wraps


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
