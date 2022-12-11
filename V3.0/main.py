import classes
import timeit

"""
Centroid Method: each iteration merges the clusters with the most similar centroid. A centroid is the average of all points in the system.
Medoid Method: each iteration merges the clusters with the most similar medoid. A medoid is the point in the cluster that is closest to all other points in the cluster.
"""


def main(control: int):
    """
    Main function
    :param control: 0 - center is a centroid, 1 - center is a medoid
    """
    map = classes.Map()
    #print("starting picturing")
    #map.picture_before()

    k = input("Enter the number of clusters: ") # number of clusters
    k = int(k)

    if control == 0:
        print("Centroid")     
        total_time = timeit.timeit(lambda: map.centroid(k), number=1)
        print("Total time: ", total_time)
    elif control == 1:
        print("Medoid")
        total_time = timeit.timeit(lambda: map.medoid(k), number=1)
        print("Total time: ", total_time)
    else:
        print("Error")
        return


if __name__ == "__main__":
    main(int(input("Enter 0 or 1: ")))

