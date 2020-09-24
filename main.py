import math
import random
import statistics
import matplotlib.pyplot as plt
import sys

#create different instances of this class using different numbers of K
#then compare using variance and decline in variance for increase in values #of k to show the optimal number for number of centroids
def main():
  file = open(sys.argv[1])
  data = []
  for line in file:
    a = line.split("\t")
    a = [s.rstrip() for s in a]
    a[0] = int(a[0])
    a[1] = int(a[1])
    data.append(a)
  set0 = Kmeans(4)
  set0.create_centroids(4, data)
  set0.compute_data(data, centroids)
  set0.centroid_iteration(data, centroids)
  set0.graph()
  file.close()

class Kmeans:
  def __init__(self, k):
    self.k = k

  #Create k random centroids
  def create_centroids(self, k, data):
    global centroids
    global repeats
    centroids = []
    repeats = []
    #Select a random data point as centroid
    x=0
    while(x<k):
      r = random.randrange(0,len(data),1)
      if r in repeats:
        pass
      elif r not in repeats:
        repeats.append(r)
        centroids.append(data[r])
        x +=1

  def dist(self, centroid, point):
    #Return euclidean distance between centroid and a data point
    return math.sqrt((centroid[0]-point[0])**2 + (centroid[1]-point[1])**2)

  #Find the nearest centroid of a point
  def nearest_centroid(self, centroids, point):
    distances = []
    for i in centroids:
      distances.append(self.dist(i,point))
    new_list = sort[distances.index(min(distances))]
    new_list.append(point)
    sort[distances.index(min(distances))] = new_list

  #Group data points into their respective centroids
  def compute_data(self, data, centroids):
    global sort
    sort = {}
    for i in range(self.k):
      sort[i] = []
    for i in data:
      self.nearest_centroid(centroids, i)

  #Generate new centroids
  def centroid_iteration(self, data, centroids):
    global new_centroids
    new_centroids = []
    for i in range(len(sort)):
      xvalue = []
      yvalue = []
      for j in sort[i]:
        xvalue.append(j[0])
        yvalue.append(j[1])
      newx = statistics.mean(xvalue)
      newy = statistics.mean(yvalue)
      input0 = [newx, newy]
      new_centroids.append(input0)

    for i in range(len(centroids)):
      while centroids[i] != new_centroids[i]:
        centroids = new_centroids
        self.compute_data(data, centroids)
        self.centroid_iteration(data, centroids)

  #Graph data and centroids
  def graph(self):
    for i in sort:
      xarray = []
      yarray = []
      for j in sort[i]:
        xarray.append(j[0])
        yarray.append(j[1])
        plt.scatter(xarray, yarray)
    for i in range(len(centroids)):
      plt.scatter(new_centroids[i][0], new_centroids[i][1],s=100)
    plt.xlabel("F1 (Hz)")
    plt.ylabel("F2 (Hz)")
    plt.savefig("Output.png")
    plt.show()

main()

