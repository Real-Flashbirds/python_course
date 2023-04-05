from abc import ABC, abstractmethod


class Organism(ABC):
    @abstractmethod
    def eat(self, *args, **kwargs):
        """ get energy for survival, abstract method, must be overridden """
        raise NotImplementedError

    @abstractmethod
    def dispose(self, *args, **kwargs):
        """ dispose of toxic material """
        raise NotImplementedError

    @abstractmethod
    def procreate(self, *args, **kwargs):
        """ create next generation """
        raise NotImplementedError

    @abstractmethod
    def breath(self, *args, **kwargs):
        """ obtain oxygen and emit co2 for metabolism """
        raise NotImplementedError


class Plant(Organism):
    """ A plant is an organism that performs photosynthesis"""

    def eat(self, *args, **kwargs):
        raise NotImplementedError

    def dispose(self, *args, **kwargs):
        pass

    def procreate(self, *args, **kwargs):
        pass

    def breath(self, *args, **kwargs):
        pass

    def photo_synthesis(self):
        """ create sugar by combining light, h2o and co2 """
        print("I make sugar to build cellulose for growth, and tempt"
              "animals to spread my seeds."
              "I also contribute free oxygen to the atmosphere, you owe me your existence!")


class Animal(Organism):
    """ An animal is an organism who has a gender and can move around """
    def __init__(self, sex):
        self.sex = sex

    def eat(self, *args, **kwargs):
        pass

    def dispose(self, *args, **kwargs):
        pass

    def procreate(self, *args, **kwargs):
        pass

    def breath(self, *args, **kwargs):
        pass

    @property
    def sex(self):
        """ male or female property """
        return self.__sex

    @sex.setter
    def sex(self, val):
        if not (val is "Female" or val is "Male"):
            self.__sex = "Other"
        else:
            self.__sex = val

    def move(self, movement):
        """ actively change location """
        print(f"Move {movement}")


class Carnivor(Animal):
    """A carnivor is an animal that consumes meat """
    def __init__(self, sex):
        super().__init__(sex=sex)

    # Inherited
    def eat(self, food="furry thing"):
        super().eat()
        print(f"sorry, killing {food}s is necessary for my health.")

    def dispose(self, *args, **kwargs):
        super().dispose()
        pass

    def procreate(self, *args, **kwargs):
        super().procreate()
        pass

    def breath(self, *args, **kwargs):
        super().breath()
        pass


class Herbivor(Animal):
    """a herbivor enjoys munching grass"""
    def __init__(self, sex):
        super().__init__(sex=sex)

    # Inherited
    def eat(self, food="green shoots"):
        super().eat()
        print(f"don't have to kill no {food}, but might need to chew my cud")

    def dispose(self, *args, **kwargs):
        super().dispose()
        pass

    def procreate(self, *args, **kwargs):
        super().procreate()
        pass

    def breath(self, *args, **kwargs):
        super().breath()
        pass


class Vertebrate(Animal):
    """ a vertebrate is an animal with a spine (except for some people
I know)"""
    def __init__(self, sex):
        super().__init__(sex=sex)

    # Inherited
    def eat(self, *args, **kwargs):
        super().eat()
        pass

    def dispose(self, *args, **kwargs):
        super().dispose()
        pass

    def procreate(self, *args, **kwargs):
        super().procreate()
        pass

    def breath(self, *args, **kwargs):
        super().breath()
        pass

    # Own
    @property
    def spine(self):
        """I do have a spine"""
        raise NotImplementedError


class Mammal(Vertebrate):
    def __init__(self, sex):
        super().__init__(sex=sex)

    def pregnancy(self, number=1):
        """ carry offspring in females """
        if self.sex == "Male":
            raise TypeError("Males cannot get pregnant")

        print(f"I am carrying {number} offspring")

    def birth(self, name, number=1):
        """ emit embryo from womb """
        if self.sex == "Male":
            raise TypeError("Males cannot give birth")

        if type(name) is list:
            print(f"Giving birth to {number} babies.", end=" ")
            print(f"Their names are {name}.")
        else:
            print(f"Giving birth to 1 baby.", end=" ")
            print(f"It's name is {name}.")

    def nurse(self):
        """ feed young using milk """
        if self.sex == "Male":
            raise TypeError("Males cannot nurse")

        print("Feeding my babies")


class Primate(Mammal):
    def __init__(self, sex, opposing_thumb=None):
        self.opposing_thumb = opposing_thumb
        super().__init__(sex=sex)

    @property
    def opposing_thumb(self):
        """ unique to primates """
        return self.__opposing_thumb

    @opposing_thumb.setter
    def opposing_thumb(self, opposing_thumb):
        self.__opposing_thumb = opposing_thumb

    def climb(self):
        """ opposing thumbs makes climbing easy """
        print("Luv them green tall things! Everything seems better "
              "from my point of view.")


class Human(Primate):
    def __init__(self, sex):
        super().__init__(sex=sex, opposing_thumb=True)

    @property
    def think(self):
        """ property of humans """
        raise NotImplementedError

    def program(self):
        """ write some software """
        print("Turn that coffee into code")

    def cook(self):
        """ use fire to soften food """
        print("Contemplating a big mac, or maybe pizza????")