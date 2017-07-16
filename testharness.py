class Test:
    def __init__(self, name, func, args, output):
        self.name = name
        self.func = func
        self.args = args
        self.output = output
        
    def test(self):
        try:
            assert func(*args) = output
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
        for tst in self.tests:
            print tst.name,
            if self.test(tst):
                print "PASS"
            else:
                print "*** TEST FAILED ***\n"

def add(a, b):
    return a + b

th = TestHarness()
th.add_test(Test(["Test 1", add, (1,2), 3]))
th.run_tests()

