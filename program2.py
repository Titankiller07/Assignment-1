print("I Love Star Wars")

def my_decorator(func):
    def wrapper(*args):
        print("I Love the movies and the series")
        result = func(*args)
        print("I have watched it about 20 times all the way through")
        return result
    return wrapper

@my_decorator
def favorite(name):
    print("My favorite is " + name + "!")

favorite("The Clone Wars Animated Series")
