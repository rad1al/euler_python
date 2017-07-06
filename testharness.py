"""A minimalistic testing system for Python.

Written for self-study purposes, includes test harness 
class along with test class.
"""


class Test:
    def __init__(self, name, func, args, output):
        self.name = name
        self.func = func
        self.args = args
        self.output = output
        
    def test(self):
        try:
            assert self.func(*self.args) == self.output
            return True
        except:
            return False
        

class TestHarness:
    def __init__(self):
        self.tests = list()
    
    def add_test(self, tst):
        self.tests.append(tst)
        
    def test(self, tst):
        return tst.test()

    def run_tests(self):
        all_tests_passed = True
        for tst in self.tests:
            print tst.name + " :",
            if self.test(tst):
                print "PASS"
            else:
                print "*** TEST FAILED ***\n"
                all_tests_passed = False
        if all_tests_passed:
            print "***************************"
            print "SUCCESS -- ALL TESTS PASSED"


def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def power(x, n):
    return x**n

th = TestHarness()
th.add_test(Test(*["Test add", add, (1,2), 3]))
th.add_test(Test(*["Test multiply", multiply, (2,5), 10]))
th.add_test(Test(*["Test power", power, (3,4), 81]))
th.run_tests()

