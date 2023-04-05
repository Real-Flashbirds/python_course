
# Python polymorphism example
from abcmeta import ABC, abstractmethod


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

    def photo_synthesis(self):
        """ create sugar by combining light, h2o and co2 """
        print("I make sugar to build cellulose for growth, and tempt animals to spread my seeds."
              "I also contribute free oxygen to the atmosphere, you owe me your existence!")

    def eat(self, *args, **kwargs):
        """ get energy for survival, abstract method, must be overridden """
        raise NotImplementedError

    def dispose(self, *args, **kwargs):
        """ dispose of toxic material """
        raise NotImplementedError

    def procreate(self, *args, **kwargs):
        """ create next generation """
        raise NotImplementedError

    def breath(self, *args, **kwargs):
        """ obtain oxygen and emit co2 for metabolism """
        raise NotImplementedError


class Animal(Organism):
    """ An animal is an organism who has a gender and can move around """

    @property
    def sex(self):
        """ male or female property """

    def move(self):
        """ actively change location """

    @abstractmethod
    def eat(self, *args, **kwargs):
        """ get energy for survival, abstract method, must be overridden """
        raise NotImplementedError

    def dispose(self, *args, **kwargs):
        """ dispose of toxic material """
        raise NotImplementedError

    def procreate(self, *args, **kwargs):
        """ create next generation """
        raise NotImplementedError

    def breath(self, *args, **kwargs):
        """ obtain oxygen and emit co2 for metabolism """
        raise NotImplementedError


class Carnivor(Animal):
    """A carnivor is an animal that consumes meat """

    def eat(self, *args, **kwargs):
        print(f"sorry, killing {food}s is necessary for my health.")


class Herbivor(Animal):
    """a herbivor enjoys munching grass"""

    def eat(self, *args, **kwargs):
        print(f"don't have to kill no {food}, but might need to chew my cud")


class Vertebrate(Animal):
    """ a vertebrate is an animal with a spine (except for some people I know)"""

    @property
    def spine(self):
        """I do have a spine"""

    def eat(self, *args, **kwargs):
        """ get energy for survival, abstract method, must be overridden """
        raise NotImplementedError


class Mammal(Vertebrate):
    def pregnancy(self):
        """ carry offspring in females """

    def birth(self):
        """ emit embryo from womb """

    def nurse(self):
        """ feed young using milk """

    def eat(self, food="furry thing"):
        """ get energy for survival, abstract method, must be overridden """
        super(Animal, food)


class Primate(Mammal):
    def __init__(self):
        self._opposing_thumb = None

    @property
    def opposing_thumb(self):
        """ unique to primates """
        return self._opposing_thumb

    def climb(self):
        """ opposing thumbs makes climbing easy """
        print("Luv them green tall things! Everything seems better from my point of view.")


class Human(Primate):
    def __init__(self):
        self._think = None

    @property
    def think(self):
        """ property of humans """
        print("To be or not to be ?")
        return self._think

    def program(self):
        """ write some software """
        print("I'm going to ask chatGPT to do that exercise for me")

    def cook(self):
        """ use fire to soften food """
        print("Contemplating a big mac, or maybe pizza????")