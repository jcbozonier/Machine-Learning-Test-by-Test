import csv

def load_all_data():
  independent_vars = []
  dependent_vars = []
  with open('generated_data.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    csv_reader.next()
    for row in csv_reader:
      independent_vars.append(map(float, row[:8]))
      dependent_vars.append(float(row[8]))
  return independent_vars, dependent_vars

import statsmodels.api as sm

def vanilla_model_test():
  independent_vars, dependent_vars = load_all_data()
  ols_model = sm.OLS(dependent_vars, independent_vars)
  model_fit = ols_model.fit()
  print model_fit.summary()
  assert False
