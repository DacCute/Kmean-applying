import numpy as np
import matplotlib as plt
import pandas as pd
from scipy.spatial.distance import cdist

#import necessary function
from preprocess import *
from process import *

data_locate = "../Data/e-shop clothing 2008.csv"

data = pd.read_csv(data_locate)

#make df to work on
choose_feature()

#Count number of type / custumer
type_df()

