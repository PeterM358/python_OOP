def make_bold(func):
    def wrapper(*args):
        start_symbol = '<b>'
        end_symbol = '</b>'
        res = combine_maker(start_symbol, f'{func(*args)}', end_symbol)
        return res

    return wrapper


def make_italic(func):
    def wrapper(*args):
        start_symbol = '<i>'
        end_symbol = '</i>'
        res = combine_maker(start_symbol, f'{func(*args)}', end_symbol)
        return res

    return wrapper


def make_underline(func):

    def wrapper(*args):
        start_symbol = '<u>'
        end_symbol = '</u>'
        # res = f'{start_symbol}{func(*args)}{end_symbol}'
        res = combine_maker(start_symbol, f'{func(*args)}', end_symbol)
        return res
    return wrapper


def combine_maker(*args):
    start_symbol = args[0]
    mid_expression = args[1]
    end_symbol = args[-1]
    return f'{start_symbol}{mid_expression}{end_symbol}'


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))