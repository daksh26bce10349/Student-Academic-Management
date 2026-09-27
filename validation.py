def valid_marks(marks):
    if 0 <= marks <= 100:
        return True
    return False

def valid_choice(choice,minimum,maximum):
    if minimum <= choice <= maximum:
        return True
    return False