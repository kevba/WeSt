import pygal

def get_graph():
	""" Creates a graph for the top 10 of least cloud coverage in Asia.
		This graph can be used as a parameter in a jinja2 template.

	:return: A top 10 graph.
	"""
	bar_chart = pygal.Bar()                                       
	bar_chart.add('test', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
	return bar_chart.render(is_unicode=True)