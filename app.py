import os
from bottle import run, template, get, post, request
from plotly import plotly
from numpy import *
from random import randint

py = plotly(username='alan.sendgi', key='qqli2tgsw5')

index_html = '''View your plot results at {{ plot_url }}'''

@get('/plot')
def form():
    return '''<h2>Graph via Plot.ly</h2>
              <form method="POST" action="/plot">
                X1 min: <input name="x1_min" type="text" />
                X1 max: <input name="x1_max" type="text" /><br/>
                X2 min: <input name="x2_min" type="text" />
                X2 max: <input name="x2_max" type="text" /><br/>
                X3 min: <input name="x3_min" type="text" />
                X3 max: <input name="x3_max" type="text" /><br/>
                <input type="submit" />
              </form>'''

@post('/plot')
def submit():
    x1_min  = int(request.forms.get('x1_min'))
    x1_max  = int(request.forms.get('x1_max'))
    x2_min  = int(request.forms.get('x2_min'))
    x2_max  = int(request.forms.get('x2_max'))
    x3_min  = int(request.forms.get('x3_min'))
    x3_max  = int(request.forms.get('x3_max'))

    x1 = range(x1_min, x1_max)
    y1 = [ random.randint(1, 10) for i in x1 ]
    x2 = range(x2_min, x2_max)
    y2 = [ random.randint(1, 10) for i in x2 ]
    x3 = range(x3_min, x3_max)
    y3 = [ random.randint(1, 10) for i in x3 ]

    response = py.plot(x1, y1, x2, y2, x3, y3)
    url = response['url']
    filename = response['filename']
    print "url:", url
    print "filename:", filename
    return template(index_html, plot_url=url)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    run(host='0.0.0.0', port=port, debug=True)
