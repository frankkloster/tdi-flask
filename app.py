import numpy as np

from bokeh.embed import components

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class StockForm(FlaskForm):
    closing = BooleanField('Closing Price')
    adjusted_closing = BooleanField('Adjusted Closing Price')
    opening = BooleanField('Opening Price')
    adjusted_opening = BooleanField('Adjusted Opening Price')
    submit = SubmitField('Submit')

from stocks import stocks

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)

@app.route("/", methods=['GET', 'POST'])
def index():
    closing, adjusted_closing, opening = None, None, None
    form = StockForm()
    if form.validate_on_submit():
        closing = form.closing.data
        adjusted_closing = form.adjusted_closing.data
        opening = form.opening.data
    plot = stocks(closing=closing, adjusted_closing=adjusted_closing, opening=opening)
    
    script, div = components(plot)

    return render_template("index.html", 
                            div=div, 
                            script=script,
                            form=form)

if __name__ == '__main__':
  app.run()