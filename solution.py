import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha=0.03
    stat, p_val = ks_2samp(x, y)

    if p_val < alpha:
        return True
    else:
        return False
