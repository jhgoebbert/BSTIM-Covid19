import itertools as it

""" setup for model selection experiment """

# diseases = ["covid19"]
# prediction_regions = ["germany"]

opt_ia = [True, False]
opt_report_delay = [True, False]
opt_demographics = [True,False]
opt_trend_order = [1,2,3,4]
opt_periodic_order = [1,2,3,4]

combinations = list(it.product(opt_ia,
                               opt_report_delay,
                               opt_demographics,
                               opt_trend_order,
                               opt_periodic_order))
