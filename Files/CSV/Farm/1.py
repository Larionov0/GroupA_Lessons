import datetime
import plotly.graph_objs as go


def search_last_tomato_supply():
    """
    Вывести на экран последнюю дату поставки помидоров
    """
    with open('farm_data.csv', 'rt', encoding='utf-8') as csv_file:
        headers = csv_file.readline()
        last_date = datetime.datetime(year=2000, month=1, day=1)
        for line in csv_file:
            line_list = line.rstrip().split(', ')
            veg_type = line_list[1]
            if veg_type == 'помидор':
                date_string = line_list[0]  # '10.01.2021'
                date = datetime.datetime.strptime(date_string, '%d.%m.%Y')
                if date > last_date:
                    last_date = date
    print('Последняя дата поставки помидоров: ', last_date.date())


def vegetables_amounts_pie():
    """
    Визуализировать в виде круговой диаграммы соотношение
    общего количества поставок разных видов овощей
    """
    vegetables_quantities = {}
    with open('farm_data.csv', 'rt', encoding='utf-8') as file:
        headers = file.readline().rstrip().split(', ')
        type_index = headers.index('type')
        quantity_index = headers.index('quantity')
        for line in file:
            line_list = line.rstrip().split(', ')
            vegetable = line_list[type_index]
            quantity = int(line_list[quantity_index])

            if vegetable not in vegetables_quantities:
                vegetables_quantities[vegetable] = 0
            vegetables_quantities[vegetable] += quantity

    vegetables = list(vegetables_quantities.keys())
    quantities = list(vegetables_quantities.values())

    diag = go.Pie(labels=vegetables, values=quantities)
    go.Figure(data=[diag]).write_html('vegetables.html', auto_open=True)


vegetables_amounts_pie()
