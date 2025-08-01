from scipy.stats import randint,uniform

LIGHTGM_PARAMS = {
    'n_estimators': randint(100, 500),
    'max_depth': randint(5, 50),
    'learning_rate': uniform(0.01, 0.2),
    'num_leaves': randint(20, 100),
    'boosting_type': ['gbdt', 'dart', 'goss'],
    'class_weight': ['balanced']  # <<< important!
}


RANDOM_SEARCH_PARAMS = {
    'n_iter': 20,  # increase search iterations
    'cv': 5,       # more reliable evaluation
    'n_jobs': -1,
    'verbose': 2,
    'random_state': 42,
    'scoring': 'recall'  # <<< change this!
}