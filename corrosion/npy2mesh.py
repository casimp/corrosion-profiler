from stl import mesh
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def verts2trimesh(x, y, z):
    """
    Converts 3 x 2D arrays of vertices (x, y, z co-ordinates) to a simple
    triangular mesh. 
    """
    verts = np.column_stack([x.flatten()[:, None], 
                             y.flatten()[:, None], 
                             z.flatten()[:, None]])

    # Create arry of unique point ids corresponding to each value in matrix
    ids = np.arange(0, z.size).reshape(z.shape[0], z.shape[1])

    # Define the points that make up all the triangle faces
    A = [ids[:-1, :-1].flatten(), ids[:-1, 1:].flatten(), ids[1:, 1:].flatten()]
    A = np.column_stack(A)
    B = [ids[:-1, :-1].flatten(), ids[1:, :-1].flatten(), ids[1:, 1:].flatten()]
    B = np.column_stack(B)

    face_ids = np.empty((A.shape[0] + B.shape[0], 3), dtype=A.dtype)
    face_ids[::2] = A
    face_ids[1::2] = B

    # Create the mesh
    profile = mesh.Mesh(np.zeros(face_ids.shape[0], dtype=mesh.Mesh.dtype))
    
    # Populate the mesh - i.e. select the vertices that make up each triangle
    for i, f in enumerate(face_ids):
        profile.vectors[i] = verts[f,:]

    return profile


def plot_mesh(profile):
    """
    Basic plotting functionality for a loaded or generated mesh.
    Straight from the numpy-stl docs (https://pypi.org/project/numpy-stl/)
    """
    # Create a new plot
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)

    # LAdd the vectors to the plot
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(profile.vectors))

    # Auto scale to the mesh size
    scale = profile.points.flatten(-1)
    axes.auto_scale_xyz(scale, scale, scale)

    # Show the plot to the screen
    plt.show()


def npy2trimesh(f, x=[0, 19], y=[0, 19]):
    """
    Loads a npy file containing 2D height (corrosion) arrays, plus
    associated x and y position limits. Creates and returns triangular 
    mesh from data.
    """
    h = np.load(f)

    x1 = np.linspace(x[0], x[1], h.shape[0])
    y1 = np.linspace(y[0], y[1], h.shape[1])
    X, Y = np.meshgrid(x1, y1)

    return verts2trimesh(X, Y, h)
