import plotly.graph_objs as go

x = ['Marina', 'Anna', 'Vasya', 'Kolya', 'Petya']
y = [11, 4, 12, 10, 5]

diag = go.Bar(x=x, y=y)
fig = go.Figure(data=[diag])
fig.write_html('marks.html', auto_open=True)
