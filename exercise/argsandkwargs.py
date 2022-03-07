

def print_kwargs(**kwargs):
    print(f'Kwargs data type: {type(kwargs).__name__}')
    for (key, value) in kwargs.items():
        print(f'{key} = {value}')


def print_args(*args):
    i = 0
    print(f"Args data type: {type(args).__name__}")
    for arg in args:
        print(f"Arg at {i} = {arg}")
        i=i+1


if __name__ == "__main__":
    dicts = {
        "name": "felix",
        "class": "S1B",
        "date": "843"
    }
    print_kwargs(**dicts)

    print_args("wazekwa")
