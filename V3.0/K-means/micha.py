"""We have a 2D space that has X and Y dimensions, ranging from -5000 to +5000. Fill this 2D space with 20 points, each point having a randomly selected position using X and Y coordinates. Each point has unique coordinates (ie, there should not be more than one point in the exact same location).

After generating 20 random points, generate another 40000 points, but these points will not be generated completely randomly, but in the following way:

Randomly select one of all points created so far in 2D space. (not only from the first 20)
If the point is too close to the edge, reduce the corresponding interval in the next two steps.
Generate a random number X_offset in the interval from -100 to +100
Generate a random number Y_offset in the interval from -100 to +100
Add a new point in 2D space that will have the same coordinates as the randomly selected point in step 1, offset by X_offset and Y_offset
    """

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def generate_points(main_points=20, near_points=40000):
    # Generating 20 random points
    points = np.random.randint(-5000, 5000, (main_points, 2))
    # Generating 40000 points
    for i in range(near_points):
        # Get a random point from the points array
        point = points[np.random.randint(0, len(points))]
        # Generating random offset
        offset = np.random.randint(-100, 100, 2)
        # Adding the offset to the selected point
        points = np.append(points, [point + offset], axis=0)
    return points


"""The way kmeans algorithm works is as follows:

Specify number of clusters K.
Initialize centroids by first shuffling the dataset and then randomly selecting K data points for the centroids without replacement.
Keep iterating until there is no change to the centroids. i.e assignment of data points to clusters isn’t changing.
Compute the sum of the squared distance between data points and all centroids.
Assign each data point to the closest cluster (centroid).
Compute the centroids for the clusters by taking the average of the all data points that belong to each cluster."""


def k_means(points, k):
    # Randomly selecting k points as centroids
    print('Generating centroids')
    centroids = points[np.random.randint(0, len(points), k)]
    # Initializing clusters
    clusters = [[] for i in range(k)]
    # Initializing previous centroids
    prev_centroids = np.zeros(centroids.shape)
    # Initializing error
    error = np.linalg.norm(centroids - prev_centroids)
    # Loop will run till the error becomes zero
    # Print the percentage of
    while error != 0:
        # Log the percentage of completion
        print(f'{(1 - error / np.linalg.norm(centroids)) * 100:.8f}%', end='\r')
        # Assigning each value to its closest cluster
        for i in range(len(points)):
            distances = np.linalg.norm(points[i] - centroids, axis=1)
            cluster = np.argmin(distances)
            clusters[cluster].append(points[i])
        # Storing the old centroid values
        prev_centroids = centroids.copy()
        # Finding the new centroids by taking the average value
        for i in range(k):
            centroids[i] = np.mean(clusters[i], axis=0)
        # Calculating error
        error = np.linalg.norm(centroids - prev_centroids)
    return centroids


def k_means_medoids(points, k):
    # Randomly selecting k points as centroids
    print('Generating centroids')
    centroids = points[np.random.randint(0, len(points), k)]
    # Initializing clusters
    clusters = [[] for i in range(k)]
    # Initializing previous centroids
    prev_centroids = np.zeros(centroids.shape)
    # Initializing error
    error = np.linalg.norm(centroids - prev_centroids)
    # Loop will run till the error becomes zero
    # Print the percentage of
    while error != 0:
        # Log the percentage of completion
        print(f'{(1 - error / np.linalg.norm(centroids)) * 100:.8f}%', end='\r')
        # Assigning each value to its closest cluster
        for i in range(len(points)):
            distances = np.linalg.norm(points[i] - centroids, axis=1)
            cluster = np.argmin(distances)
            clusters[cluster].append(points[i])
        # Storing the old centroid values
        prev_centroids = centroids.copy()
        # Finding the new centroids by taking the average value
        for i in range(k):
            centroid = np.mean(clusters[i], axis=0)
            if np.isnan(centroid).any():
                centroid = np.mean(clusters[i], axis=0)
        # Calculating error
        error = np.linalg.norm(centroids - prev_centroids)
    return centroids


def get_clusters(points, centroids):
    # Generating the clusters
    print('Generating clusters')
    clusters = [[] for i in range(len(centroids))]
    for i in range(len(points)):
        distances = np.linalg.norm(points[i] - centroids, axis=1)
        cluster = np.argmin(distances)
        clusters[cluster].append(points[i])
    return clusters


def run_k_means_medoids(points, k):
    print(f"Running k-means with {k} clusters")
    medoids = k_means_medoids(points, k)
    evaluate(points, medoids)
    clusters = get_clusters(points, medoids)
    # Plotting the clusters
    for i in range(len(clusters)):
        cluster = np.array(clusters[i])
        color = np.random.rand(3,)
        plt.scatter(cluster[:, 0], cluster[:, 1], color=color, s=1)

    plt.scatter(medoids[:, 0], medoids[:, 1], s=10, color='red')
    # Save plot sd png
    plt.savefig('medoids.png')

# Evaluate the success/failure rate of your clusterer. We consider a successful clusterer to be one in which no cluster has an average distance of points from the center of more than 500.


def evaluate(points, centroids):
    clusters = get_clusters(points, centroids)
    for i in range(len(clusters)):
        cluster = np.array(clusters[i])
        distances = np.linalg.norm(cluster - centroids[i], axis=1)
        print(f'Cluster {i} average distance: {np.mean(distances)}')


def main(number_of_points=20, near_points=40000):
    print(
        f"Generating {number_of_points} random points and {near_points} points near them")
    # Generate 20 random points and 40000 points
    points = generate_points(number_of_points, near_points)
    run_k_means_medoids(points, number_of_points)
    # Generate 20 centroids
    centroids = k_means(points, number_of_points)
    evaluate(points, centroids)
    # Get the clusters
    clusters = get_clusters(points, centroids)
    # Plotting the clusters
    for i in range(len(clusters)):
        cluster = np.array(clusters[i])
        color = np.random.rand(3,)
        plt.scatter(cluster[:, 0], cluster[:, 1], color=color, s=1)
    # Plotting the centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], s=10, color='red')

    # Save plot sd png
    plt.savefig('centroids.png')


main(20, 40000)

"""
Cluster 0 average distance: 105.42697905506014
Cluster 1 average distance: 148.44388523586315
Cluster 2 average distance: 195.43006921774347
Cluster 3 average distance: 107.876241022323
Cluster 4 average distance: 380.32456916606446
Cluster 5 average distance: 753.7358218899421
Cluster 6 average distance: 76.90646449739084
Cluster 7 average distance: 186.5082022021464
Cluster 8 average distance: 164.21614441110535
Cluster 9 average distance: 159.6797863959342
Cluster 10 average distance: 519.6364457038164
Cluster 11 average distance: 216.6378722887837
Cluster 12 average distance: 158.27958209148082
Cluster 13 average distance: 161.9657640736289
Cluster 14 average distance: 548.3637276409896
Cluster 15 average distance: 114.68147237979197
Cluster 16 average distance: 164.39523765667846
Cluster 17 average distance: 125.05586694499483
Cluster 18 average distance: 200.6192227918402
Cluster 19 average distance: 152.38972362136974
Generating clusters
Generating centroids
Generating clusters
Cluster 0 average distance: 119.33093263862622
Cluster 1 average distance: 192.07709476877287
Cluster 2 average distance: 132.98999314925817
Cluster 3 average distance: 890.509509312169
Cluster 4 average distance: 155.35796437252893
Cluster 5 average distance: 1565.3653064569219
Cluster 6 average distance: 152.80069223790323
Cluster 7 average distance: 221.27689849514766
Cluster 8 average distance: 48.08590624344299
Cluster 9 average distance: 430.4651638873643
Cluster 10 average distance: 175.50184032866264
Cluster 11 average distance: 211.75802686939238
Cluster 12 average distance: 566.127494478303
Cluster 13 average distance: 238.9395367065937
Cluster 14 average distance: 174.4023607529007
Cluster 15 average distance: 161.13527272789165
Cluster 16 average distance: 193.84905537915714
Cluster 17 average distance: 175.6113594445561
Cluster 18 average distance: 200.90907395711116
Cluster 19 average distance: 911.9962443208176
Generating clusters"""
