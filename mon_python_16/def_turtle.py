import turtle

t=turtle.Pen()
colors=['#CBC10B', '#0BCB49', '#0B41CB']


def side(i):
	t.pencolor(colors[0])	# меняет цвет
	t.forward(100)			# рисует вперед
	t.left(i)				# поворачивает налево


x = 120
side(x)
side(x)
side(x)


# 
turtle.done()
