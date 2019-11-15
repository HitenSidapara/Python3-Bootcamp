# __init__ method call it self when we are create the object of the class


class DemoClass:
    def __init__(self):
        print("DemoClass Is called");


demo1 = DemoClass();
demo2 = DemoClass();