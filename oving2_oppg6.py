"""The rotation matrix from frame {a} to frame {b} is given by
Rab = Rot(ˆx, π/6) Rot(ˆz, π/4)
a) Implement the Python functions rotx, roty and rotz which takes a rotation angle as input
and returns a rotation matrix for the given rotation angle around the ˆx, ˆy and ˆz axis,
respectively.
b) Perform the matrix multiplication of Rab by hand and by using the functions created in
the previous point.
c) Sketch the resulting frames {a} and {b}."""
import numpy as np
import matplotlib.pyplot as plt
def rotx(theta):
    rot = np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]])
    return rot
def roty(theta):
    rot = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]])
    return rot
def rotz(theta):
    rot = np.array([[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]])
    return rot
R_ab = np.dot(rotx(np.pi/6),rotz(np.pi/4))
print("R_ab:")
print(R_ab)
i = np.array([1,0,0])
j = np.array([0,1,0])
k = np.array([0,0,1])
i_, j_, k_ = R_ab@i, R_ab@j, R_ab@k
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
#axis system
ax.quiver(0, 0, 0, i[0], i[1], i[2], color='g', arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, j[0], j[1], j[2], color='r', arrow_length_ratio=0.3)
ax.quiver(0, 0, 0, k[0], k[1], k[2], color='b', arrow_length_ratio=0.3)
#rotated axis system
ax.quiver(0, 0, 0, i_[0], i_[1], i_[2], color='g', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, j_[0], j_[1], j_[2], color='r', arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, k_[0], k_[1], k_[2], color='b', arrow_length_ratio=0.1)
#display limits
ax.set_xlim([-0.5, 1])
ax.set_ylim([-.5, 1])
ax.set_zlim([-.5, 1])
plt.show()