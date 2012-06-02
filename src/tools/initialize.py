import os

src_path = os.path.join(
    os.path.dirname(__file__),
    '..'
)

objectives_path = os.path.join(
    src_path,
    'objectives'
)

assert os.path.isdir(objectives_path)
