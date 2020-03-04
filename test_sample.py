import sample

def testDiv5And3():
    assert sample.fizzbuzz(15) == "FizzBuzz"

def testDiv5():
    assert sample.fizzbuzz(5) == "Buzz"

def testDiv3():
    assert sample.fizzbuzz(3) == "Fizz"

def testNotDiv3Or5():
    assert sample.fizzbuzz(2) == 2