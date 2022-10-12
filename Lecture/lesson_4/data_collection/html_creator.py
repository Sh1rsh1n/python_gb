from user_interface import temperature_view
from user_interface import wind_speed_view
from user_interface import preassure_view


def create(device = 1):
    style = 'style="font-size:30px;"'
    html = '<html>\n    <head></head>\n     <body>\n'
    html += '   <p {}> Temperature: {} c</p>\n'\
        .format(style, temperature_view(device))
    html += '   <p {}> wind_speed: {} m/s</p>\n' \
        .format(style, wind_speed_view(device))
    html += '   <p {}> Preassure: {} mmHg</p>\n' \
        .format(style, preassure_view(device))

    with open('index.html', 'w') as page:
        page.write(html)

    return html


def n_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    style = 'style="font-size:30px;"'
    html = '<html>\n    <head></head>\n     <body>\n'
    html += '   <p {}> Temperature: {} F</p>\n'\
        .format(style, t)
    html += '   <p {}> wind_speed: {} "m/s"</p>\n' \
        .format(style, w)
    html += '   <p {}> Preassure: {} mmHg</p>\n' \
        .format(style, p)
    html += '   </body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data
