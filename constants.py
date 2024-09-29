from enum import Enum

class ValueEnum(Enum):
    ''' Enums that return the value you assign them '''
    def __get__(self, instance, owner):
        return self.value

class Color(ValueEnum):
    WHITE       = (255, 255, 255)
    RED         = (255,   0,   0)
    BRIGHT_RED  = (255, 100,   0)
    GREEN       = (  0, 255,   0)
    BLUE        = (  0,   0, 255)
    BRIGHT_BLUE = (  0, 150, 255)
    YELLOW      = (255, 255,   0)
    GREY        = (100, 100, 100)