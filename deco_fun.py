def main(func):
    def inner(data):
        if isinstance(data,str):
            res=data.upper()
        else:
            res='hello'
        return func(res)
    return inner

@main
def abc(data):
    print(data)

abc('hello')
