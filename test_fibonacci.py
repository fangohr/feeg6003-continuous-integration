def test_fibonacci():
    """
    In this function, we test the fibonacce number computation.
    """

    import fib
    assert fib.fib(2) == 1
    assert fib.fib(3) == 2
    assert fib.fib(10) == 55
    assert fib.fib(11) == 89
