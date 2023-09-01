# def coroutine1():
#     print('callee 1')
#     x = yield 1
#     print('callee 2: %d' % x)
#     x = yield 2
#     print('callee 3: %d' % x)
    
# task = coroutine1()
# i = next(task)

# i = task.send(10)
# task.send(20)

def test_yield():
    while True:
        y = yield 1
        if y == 10:
            break
        
task = test_yield()
i = next(task)
