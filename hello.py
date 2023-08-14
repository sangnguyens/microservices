def say_hello(name: int = "Sang", x: int = 2, y: int = 3) -> int:
    print(f"Hello {name}")

    return x + y


say_hello("Allen", x=3, y=6)
