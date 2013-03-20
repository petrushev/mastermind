from mastermind import evaluate, valid

def test_evaluate():
    assert evaluate((1,2,3,4), (2,1,3,6))==(1,2)
    assert evaluate((1,2,3,4), (1,2,3,4))==(4,0)
    assert evaluate((1,2,3,4), (5,6,7,8))==(0,0)
    assert evaluate((1,2,3,4), (2,3,5,6))==(0,2)

def test_valid():
    assert valid((1,2,3,4))
    assert not valid((1,1,2,3))
    assert not valid((1,2,3))
    assert not valid((0,2,3,4))
    assert not valid((1,3,4,5,6))
    assert not valid((1,2,2,3,4))

def suite():
    total, failed = 0, 0
    for test_name, test in globals().iteritems():
        if not test_name.startswith('test'): continue
        total = total + 1
        try:
            test()
        except AssertionError:
            print test_name, 'failed.'
            failed = failed  + 1
    if failed:
        print '%d of %d tests failed.' % (failed, total)
    else:
        print 'all %d tests passed.' % total

if __name__=='__main__':
    suite()
