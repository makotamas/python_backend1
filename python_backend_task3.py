# Task 3

import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


from flask import Flask
from flask import send_file
app = Flask(__name__)

# prevent matplotlib from opening a gui
plt.ioff()
mpl.use('Agg')


@app.route('/')
def hello_world():
  with open('income.txt', 'r') as file:
        lines = file.readlines()[1:]  
        
        data_source = []
        for line in lines:
            stripped_line = line.strip() 
            split_line = stripped_line.split(',')
            processed_line = [int(element.replace(' ', '')) for element in split_line] 
            data_source.append(processed_line)
  df = pd.DataFrame(data_source)
  df.columns = ['web dev', 'desktop app dev', 'ios/android dev', 'networking']
  sns_plot = sns.barplot(palette="ch:.25", data=df, ci=None)
  sns_plot.figure.savefig("output.png")
  plt.close()
  return send_file('output.png', mimetype='image/png')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000) 