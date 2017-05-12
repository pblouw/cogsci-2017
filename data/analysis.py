import numpy as np

from bootstrap import sample, mean, bootstrapci

# counts for each Likert option from .csv files
human_true_1 = 6
human_true_2 = 55
human_true_3 = 64
human_true_4 = 158
human_true_5 = 217

human_false_1 = 205
human_false_2 = 93
human_false_3 = 51
human_false_4 = 70
human_false_5 = 13

model_true_1 = 64
model_true_2 = 60
model_true_3 = 66
model_true_4 = 137
model_true_5 = 153

# create arrays of recorded Likert values from all conditions
human_true_data = np.concatenate((5 * np.ones(human_true_5),
                                 4 * np.ones(human_true_4),
                                 3 * np.ones(human_true_3),
                                 2 * np.ones(human_true_2),
                                 1 * np.ones(human_true_1)))

model_true_data = np.concatenate((5 * np.ones(model_true_5),
                                 4 * np.ones(model_true_4),
                                 3 * np.ones(model_true_3),
                                 2 * np.ones(model_true_2),
                                 1 * np.ones(model_true_1)))

human_false_data = np.concatenate((5 * np.ones(human_false_5),
                                  4 * np.ones(human_false_4),
                                  3 * np.ones(human_false_3),
                                  2 * np.ones(human_false_2),
                                  1 * np.ones(human_false_1)))

human_true_mean = mean(human_true_data)
human_true_ci = bootstrapci(human_true_data, mean)

print('Human Data - True')
print('Mean Rating: ', human_true_mean)
print('95% CIs: ', human_true_ci[1],  human_true_ci[0])

human_false_mean = mean(human_false_data)
human_false_ci = bootstrapci(human_false_data, mean)

print('Human Data - False')
print('Mean Rating: ', human_false_mean)
print('95% CIs: ', human_false_ci[1], human_false_ci[0])


model_true_mean = mean(model_true_data)
model_true_ci = bootstrapci(model_true_data, mean)

print('Model Data - True')
print('Mean Rating: ', model_true_mean)
print('95% CIs: ', model_true_ci[1], model_true_ci[0])



