# simple finite generator
def get123():
    yield 1
    yield 2
    yield 3


# g is an iterator
g = get123()
print(
    next(g),
    next(g),
    next(g)
)

try:
    next(g)
except StopIteration:
    print('well, no more items')


def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def fun_pipeline():
    """
    computation is lazy (hell yeah!) but it makes debugging complex
    to force generating all items call list() constructor on generator function
    """
    items = [3, 6, 9, 2, 1, 1, 3, 9, 2, 5, ]
    # for item in (take(3, distinct(items))):
    # debugging - distinct generator will generate whole list
    for item in (take(3, list(distinct(items)))):
        print(item)


fun_pipeline()

# infinite generator


def pi():
    pi = 3
    yield pi
    counter = 0
    x = 2
    while True:
        fragment = 4 / (x*(x+1)*(x+2))
        if counter % 2 != 0:
            fragment *= -1
        pi += fragment
        x += 2
        yield pi
        counter += 1


pigen = pi()
# lazy calculation - next iteration calculated only once called
for _ in range(20):
    print(next(pigen))

# infinite loop, Ctrl + D to interrupt
for i in pi():
    print(i)
