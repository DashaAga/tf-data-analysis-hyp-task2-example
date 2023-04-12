import pandas as pd
import numpy as np
from scipy.stats import shapiro

chat_id = 588908837 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha=0.03
    statistic1, pvalue1 = shapiro(x)
    statistic2, pvalue2 = shapiro(y)
    
    if pvalue1 < alpha or pvalue2 < alpha:
        return True
    else:
        return False
