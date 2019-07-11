
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first child() function")

    def second_child():
        print("Printing from the second child() function")

    first_child()
    second_child()

parent()