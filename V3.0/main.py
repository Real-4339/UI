import classes

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
    print("starting picturing")
    map.picture_before()

    print("asking for number of clusters")
    k = input("Enter the number of clusters: ") # number of clusters
    k = int(k)

    if control == 0:
        print("Centroid")     
        #map.centroid(k)
        #map.picture_after()
    elif control == 1:
        print("Medoid")
    else:
        print("Error")
        return

    



if __name__ == "__main__":
    main(int(input("Enter 0 or 1: ")))

