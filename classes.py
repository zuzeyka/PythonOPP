# наследование классов
# наследование - переопределение методов и полей из одного класса в другой (от родительскому к дочернему)

class Human:
    def __init__(self, name: str, height: float) -> None:
        self.name = name
        self.height = height
    def run(self):
        print("Run")
    def jump(self):
        print("Jump")