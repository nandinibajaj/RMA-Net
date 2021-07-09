import numpy as np

#translate points
def transferXYZ(npCloud, matrixMoveToCentroid):
    return np.dot(npCloud,matrixMoveToCentroid) 

def zeroMeanCloud(pt_cloud):
    npCloud = np.asarray(pt_cloud)
    centroid=np.average(npCloud,axis=0)
    matrixMoveToCentroid=np.identity(4)
    matrixMoveToCentroid[0:3,3]=-centroid[0:3] #create transform matrix
    matrixMoveToCentroid=np.transpose(matrixMoveToCentroid) #transposing transform matrix
    npCloud=transferXYZ(npCloud,matrixMoveToCentroid)  #translation
    return npCloud[:,0:3]

# Normalize the input pt_cloud with respect to the input max_val, max mean of X Y Z to be zero  
def norm_data(pt_cloud,zeroMean=True, normalizeFactor=None):
    if(zeroMean):
        pt_cloud  =zeroMeanCloud(pt_cloud)
       
    if(normalizeFactor==None):    
        max_coord = np.max(np.absolute(pt_cloud))
        normalizeFactor=max_coord
    return pt_cloud / normalizeFactor

def main():
    file_data_path="/home/nandini/Downloads/RMA-Net-main/lander/sourceCAD_2055_vertices.obj"
    file_save_path="/home/nandini/Downloads/RMA-Net-main/lander/centered_sourceCAD_2055_vertices.obj"
    point_cloud= np.loadtxt(file_data_path, skiprows=0, max_rows=1000000)
    point_cloud=point_cloud[:,:3]
    print(point_cloud)
    st=np.ones(point_cloud.shape[0])
    point_cloud=np.insert(point_cloud,3,st,axis=1)#inserting a unit vector to match transform matrix order of 4
    out = norm_data(point_cloud)#centered matrix of vertices
    np.savetxt(file_save_path, out, delimiter=' ')


if __name__=="__main__":
    main()
