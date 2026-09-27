from perfromace_analyzer import calculate_grade

def test_grade_A():
    result = calculate_grade(85)

    if result == "A":
        print("Test 1 passed")
    else:
        print("Test 1 failed")

def test_grade_B():
    result = calculate_grade(75)

    if result == "B":
        print("Test 2 passed")
    else:
        print("Test 2 failed")

def test_grade_F():
    result = calculate_grade(35)

    if result == "F":
        print("Test 3 passed")
    else:
        print("Test 3 failed")

test_grade_A()
test_grade_B()
test_grade_F()
