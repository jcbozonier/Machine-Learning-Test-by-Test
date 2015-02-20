import pandas
import statsmodels.formula.api as sm

def vanilla_model_test():
  df = pandas.read_csv('./generated_data.csv')
  model_fit = sm.ols('dependent_var ~ ind_var_a + ind_var_b + ind_var_c + ind_var_e + ind_var_b * ind_var_c', data=df).fit()
  print model_fit.summary()
  assert model_fit.f_pvalue <= 0.05, "Prob(F-statistic) should be small enough to reject the null hypothesis."
  assert model_fit.rsquared_adj >= 0.95, "Model should explain 95% of the variation in the sampled data or more."
  assert False