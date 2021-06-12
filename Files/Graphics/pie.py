import plotly.graph_objs as go

countries = ['Пироговия', "Тортовия", "Булковия", "Пирожния"]
squares = [1000, 690, 2200, 1300]


diag = go.Pie(labels=countries, values=squares)
fig = go.Figure(data=[diag])
fig.write_html('countries.html', auto_open=True)
