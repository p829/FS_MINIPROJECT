#! /usr/bin/env python3

import os
import sys

from PIL import Image
import numpy as np


def K_points(X, K):
    """ Choose K points from X at random """
    m = len(X)
    return X[np.random.choice(m, K, replace=False), :]


def closest_centroid(X, centroid_value):
    m = len(X)
    c = np.zeros(m)

    for i in range(m):
        # Find distances
        distances = np.linalg.norm(X[i] - centroid_value, axis=1)

        # Assign closest cluster to c[i]
        c[i] = np.argmin(distances)

    return c


def mean_value(X, index_value, K):
    _, n = X.shape
    centroid_value = np.zeros((K, n))
    for k in range(K):
        examples = X[np.where(index_value == k)]
        mean = [np.mean(column) for column in examples.T]
        centroid_value[k] = mean
    return centroid_value


def K_mean_value(X, K, no_of_iterations):
    centroid_value = K_points(X, K)
    previous_centroid_value = centroid_value
    for a in range(no_of_iterations):
        index_value = closest_centroid(X, centroid_value)
        centroid_value = mean_value(X, index_value, K)
        if (previous_centroid_value == centroid_value).all():
            # The centroid_value aren't moving anymore.
            return centroid_value
        else:
            previous_centroid_value = centroid_value

    return centroid_value, index_value


