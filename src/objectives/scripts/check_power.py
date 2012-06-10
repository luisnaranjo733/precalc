points = (
    (1.0, 32.0),
    (2.0, 8.0),
    (6.0, 8.0/9.0),
    (8.0, 0.5),
    (10.0, 0.32),
)

def f(x):
    return 32.0*x**-2

for x,y in points:
    assert y == f(x)
