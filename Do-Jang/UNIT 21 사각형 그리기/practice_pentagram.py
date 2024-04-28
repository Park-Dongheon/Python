import turtle as t

n = 5
for i in range(5):
    t.forward(100)
    t.right((360/n) * 2)
    t.forward(100)
    t.left(360/n)
