class Bmw:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max = max_speed
        self.color = color

    def start_engine(self):
        print(f"{self.title} {self.model}")

    def stop_engine(self):
        print(f"{self.title} {self.model}")

    def info(self):
        print(f"""
Title:{self.title}
Model:{self.model}
Weight:{self.weight}
Hp:{self.hp}
Nm:{self.nm}
Max speed:{self.max}
Color:{self.color}""")


X6 = Bmw('output CarTitle ', 'Car Model engine stoped! X6', 2000, 400, 600, 1000, "white")
X6.info()
X6.start_engine()
X6.stop_engine()


class Mercedec:
    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max = max_speed
        self.color = color

    def start_engine(self):
        print(f"{self.title} {self.model}")

    def stop_engine(self):
        print(f"{self.title} {self.model}")

    def info(self):
        print(f"""
Title:{self.title}
Model:{self.model}
Weight:{self.weight}
Hp:{self.hp}
Nm:{self.nm}
Max speed:{self.max}
Color:{self.color}""")


merc = Mercedec('output carTitle ', 'car Model engine stoped! AMG', 1800, 600, 600, 1750, "black")
merc.info()
merc.start_engine()
merc.stop_engine()
