from Grasshopper import DataTree
from Grasshopper.Kernel.Data import GH_Path
from Rhino.Geometry import Point3d

def treeBranch(points, itemNum):
    """ list items (points) into DataTree based on itemNum """
    tree = DataTree[Point3d]()
    pathCount = 0
    newPath = GH_Path(pathCount)

    for num in range(len(points)):
        if num % itemNum == 0 and num != 0:
            pathCount += 1
            newPath = GH_Path(pathCount)
        tree.Add(points[num], newPath)
    return tree