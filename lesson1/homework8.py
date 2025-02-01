import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, result
import unittest
import time

def measure_time(func, *args, **kwargs):

    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, result
def fast_function():
    return "fast"

def slow_function():
    time.sleep(1)
    return "slow"

class TestMeasureTime(unittest.TestCase):
    def test_fast_function(self):
        exec_time, result = measure_time(fast_function)
        self.assertEqual(result, "fast")
        self.assertLess(exec_time, 0.1)

    def test_slow_function(self):
        exec_time, result = measure_time(slow_function)
        self.assertEqual(result, "slow")
        self.assertGreater(exec_time, 0.9)

if __name__ == '__main__':
    unittest.main()