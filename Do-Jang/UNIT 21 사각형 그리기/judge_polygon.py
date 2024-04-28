import turtle as t

point, line = map(int, input().split())
t.shape('turtle')
t.speed('fastest')
for i in range(point):
    t.forward(line)
    t.right((360/point) * 2)
    t.forward(line)
    t.left(360/point)
