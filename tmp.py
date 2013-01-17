def test(*args, **kwargs):
    a = 'a'
    b = 'b'
    return locals()
a,b = test()