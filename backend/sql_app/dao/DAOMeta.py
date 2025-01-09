class DAOMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}，bases: {bases}, dct: {dct}")
        if 'model' not in dct:
            raise AttributeError(f"Class {name} must define a 'model' attribute")
        return super().__new__(cls, name, bases, dct)