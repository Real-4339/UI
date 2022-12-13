#!/usr/bin/python3
"""
This is a simple implementation of the k-means algorithm.
"""
import random
import numpy as np
import matplotlib.pyplot as plt


def generation(n: int, points_x, points_y):
    for i in range(n):
        if len(points_x) < n:
            new_x = random.choice(list(points_x))
            if abs(new_x) >= x_:
                sign_x = 1 if new_x > 0 else -sign_x
                x_offset = np.random.randint(0, 100, 1)[0] * sign_x
            else:
                x_offset = np.random.randint(0, 100, 1)[0]
                points_x.add(new_x + x_offset)
        if len(points_y) < n:
            new_y = random.choice(list(points_y))
            if abs(new_y) > y_:
                sign_y = 1 if new_y > 0 else -1
                y_offset = np.random.randint(0, 25, 1)[0] * sign_y
            else:
                y_offset = np.random.randint(0, 100, 1)[0]
            points_y.add(new_y + y_offset)

def main(k:int, n:int):
    """
    First generating 20 random data
    Second generating n points
    Third generating k clusters
    Choose k random points as the initial centroids
    Assign each data point to the closest centroid
    Update the centroid of each cluster
    Repeat the above steps until the centroids do not change
    Plot the data points and the final centroids
    """
    # Size of the plot: from -5000 to 5000
    x_ = 5000
    y_ = 5000
    # Generating 20 random data
    cube = np.random.randint(0, 20, 1)[0]
    rng = np.random.default_rng()
    x = rng.choice(x_, 20, replace=False)
    y = rng.choice(y_, 20, replace=False)
    # choose from x random points and give them minus sign
    x = np.where(np.random.choice([True, False], 20, p=[cube/20, 1-cube/20]), -x, x)
    y = np.where(np.random.choice([True, False], 20, p=[cube/20, 1-cube/20]), -y, y)
    plt.scatter(x, y, c='black', s=7)
    x = np.array(list(x))
    y = np.array(list(y))
    # Generating n points
    points_x:set = set(x)
    points_y:set = set(y)
    generation(n, points_x, points_y)
    #if len(points_x) < n:
    # add the points to 20 points
    x = np.concatenate((x, np.array(list(points_x))))
    y = np.concatenate((y, np.array(list(points_y))))
    
    plt.scatter(x, y, c='red', s=7)
    return
    # Generating k clusters
    centroids_x = np.random.randint(0, 100, k)
    centroids_y = np.random.randint(0, 100, k)
    centroids = np.array(list(zip(centroids_x, centroids_y))).reshape(len(centroids_x), 2)
    plt.scatter(centroids_x, centroids_y, c='blue', s=7)
    # Choose k random points as the initial centroids
    old_centroids = np.zeros(centroids.shape)
    clusters = np.zeros(len(points))
    error = np.linalg.norm(centroids - old_centroids)
    # Assign each data point to the closest centroid
    while error != 0:
        for i in range(len(points)):
            distances = np.linalg.norm(points[i] - centroids, axis=1)
            cluster = np.argmin(distances)
            clusters[i] = cluster
        # Update the centroid of each cluster
        old_centroids = centroids
        for i in range(k):
            points = [points[j] for j in range(len(points)) if clusters[j] == i]
            centroids[i] = np.mean(points, axis=0)
        error = np.linalg.norm(centroids - old_centroids)
    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    fig, ax = plt.subplots()
    for i in range(k):
        points = np.array([points[j] for j in range(len(points)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
    ax.scatter(centroids[:, 0], centroids[:, 1], marker='*', s=200, c='#050505')
        


if __name__ == "__main__":
    k, n = input("Enter the number of clusters and number of data points: ").split()
    k, n = int(k), int(n)
    main(k, n)
