def kmeans_init_center(X, k):
    #choose center randomly
    return X[np.random(X.shape[0], k, replace= False)]
