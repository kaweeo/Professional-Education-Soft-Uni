def tags(html_tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = f"<{html_tag}>{func(*args)}</{html_tag}>"
            return result

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
