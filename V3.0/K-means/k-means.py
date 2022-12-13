#!/usr/bin/python3
"""
This is a simple implementation of the k-means algorithm.
"""
import random
import numpy as np
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Point):
            return NotImplemented
        return self.x == o.x and self.y == o.y
    
    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"

def distance(p1: Point, x1, y1) -> float:
    """
    Calculate the distance between two points
    """
    return np.sqrt((p1.x - x1)**2 + (p1.y - y1)**2)

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
    # Generating n points
    points: set = set(Point(x, y) for x, y in zip(x, y))
    for i in range(n):
        new_x = random.choice(list(points))
        if abs(new_x.x) >= x_:
            sign_x = 1 if new_x.x > 0 else -sign_x
            x_offset = np.random.randint(0, 100, 1)[0] * sign_x
        else:
            x_offset = np.random.randint(0, 100, 1)[0]
        new_y = random.choice(list(points))
        if abs(new_y.y) > y_:
            sign_y = 1 if new_y.y > 0 else -1
            y_offset = np.random.randint(0, 25, 1)[0] * sign_y
        else:
            y_offset = np.random.randint(0, 100, 1)[0]
        points.add(Point(new_x.x + x_offset, new_y.y + y_offset))
    if len(points) < n:
        for i in range(n - len(points)):
            new_x = random.choice(list(points))
            if abs(new_x.x) >= x_:
                sign_x = 1 if new_x > 0 else -1
                x_offset = np.random.randint(0, 100, 1)[0] * sign_x
            else:
                x_offset = np.random.randint(0, 100, 1)[0]
            new_y = random.choice(list(points))
            if abs(new_y.y) > y_:
                sign_y = 1 if new_y > 0 else -1
                y_offset = np.random.randint(0, 25, 1)[0] * sign_y
            else:
                y_offset = np.random.randint(0, 100, 1)[0]
            points.add(Point(new_x.x + x_offset, new_y.y + y_offset))

    points = np.array(list(points))
    # Choose k random points as the initial centroids
    clusters = np.random.choice(points, k, replace=False)
    # Make centroid array
    centroids = np.array([np.array([c.x, c.y]) for c in clusters])
    # Assign each data point to the closest centroid
    clusters = np.array([np.argmin([distance(p, c[0], c[1]) for c in centroids]) for p in points])
    # Update the centroid of each cluster
    centroids = [np.mean(points[clusters == i], axis=0) for i in range(k)]
    # Repeat the above steps until the centroids do not change
    while True:
        clusters = np.array([np.argmin([distance(p, c[0], c[1]) for c in centroids]) for p in points])
        new_centroids = [np.mean(points[clusters == i], axis=0) for i in range(k)]
        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids
    # Plot the data points and the final centroids
    plt.scatter(points[:, 0], points[:, 1], c=clusters, s=7, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.5)
    plt.show()
        

if __name__ == "__main__":
    k, n = input("Enter the number of clusters and number of data points: ").split()
    k, n = int(k), int(n)
    main(k, n)
