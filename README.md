#### [Ls_ApexLol_v01.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_ApexLol_v01.hipnc)
APEX node graphs are stored as geometry so you can do silly things like move the nodes themselves around with attribnoise:

https://github.com/user-attachments/assets/598374e9-640f-4ea8-b978-7f94de4b3d33

 
#### [Ls_ColourBooper_v01.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_ColourBooper_v01.hipnc)
Semi-serious try at 3D colour correction with 5 from/to pickers using radial basis functions to stay smooth, kinda similar to the mesh-like colour warping in Baselight/Flame/Resolve:

https://github.com/user-attachments/assets/ead2cc2e-e160-45a9-83da-68dfa6ef0727


#### [Ls_Cop3AtomicAdd.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_Cop3AtomicAdd.hipnc)
Using OpenCL global atomic add tricks to render a buffer of point positions as single pixel particles super fast, a bit like Krakatoa or higx point render:

https://github.com/user-attachments/assets/30609454-98d0-46a3-883d-81831ba6363e


#### [Ls_Cop3PrefixsumGlow.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_Cop3PrefixsumGlow.hipnc)
The Prefix Sum COP makes summed area tables that let you do box filters of any size pretty much instantly, so you can add up tons of them to approximate the non-separable kernels of exponential or fibonacci glows (which look uncomfortably like having smudged glasses if you get the shape just right):

<img width="2560" height="1600" alt="Ls_Cop3PrefixsumGlow" src="https://github.com/user-attachments/assets/495ac1de-7cc3-4653-bac4-3b99bbbf24ef" />


#### [Ls_KarmaMandelbulb](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_KarmaMandelbulb)
The HDK comes with a Karma procedural that renders a mandelbulb in VEX without having to create any geometry (sadly it crashes as soon as you change any of the parameters in 20.5.361 unless you switch the renderer from Karma CPU to something else and then back again):

<img width="2560" height="1462" alt="Ls_KarmaMandelbulb" src="https://github.com/user-attachments/assets/8ee538ab-d207-4d4f-9962-f442dbbd91ff" />


#### [Ls_KarmaPNGslapcompACES_v01.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_KarmaPNGslapcompACES_v01.hipnc)
Probably the best we can do in 21.0 to render PNGs from Karma with an OCIO view transform baked in, by applying it with a slapcomp block and passing `--ocio 0` to husk so it doesn't do another transform... it matches rendering an EXR and applying the view transform afterwards in COPs:

<img width="2559" height="1320" alt="Ls_KarmaPNGslapcompACES_v01" src="https://github.com/user-attachments/assets/c23c8a5b-a734-488d-ae2d-15baaaa40658" />


#### [Ls_KarmaSunset_v01](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_KarmaSunset_v01)
You can sorta render a sunset using a uniform volume on a sphere as big as the entire earth with a geo-referenced DEM terrain, letting the atmosphere both scatter and absorb the same colour so the sky gradient from the low-angle sun appears naturally:

<img width="1985" height="857" alt="Ls_KarmaSunset_v01" src="https://github.com/user-attachments/assets/34b49392-95c7-40c3-aed7-08908b59b9fe" />


#### [Ls_MatrixFromChart_v01b.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_MatrixFromChart_v01b.hipnc)
Extracts a best-fit 3x3 matrix from two Macbeth chart images similarly to mmColorTarget using everyone's favourite, the Linear Solver SOP:

<img width="2560" height="1487" alt="Ls_MatrixFromChart_v01" src="https://github.com/user-attachments/assets/1a30e0f6-d35c-478f-86aa-d5a005937645" />


#### [Ls_Ramprefine_v01.hiplc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_Ramprefine_v01.hiplc)
Simplifying colour ramps that have way too many points by treating them as 3D paths in RGB space:

https://github.com/user-attachments/assets/9da0f16f-a628-4aed-a6d0-662202ece5c5


#### [Ls_RotationWalksHome_v03.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_RotationWalksHome_v03.hipnc)
Visualizing the main result of https://arxiv.org/abs/2502.14367v3 by showing rotation vectors in SO(3) for 50 walks as their angle scales increase over time, both on the left walking once (which never returns to the origin) and on the right the same walk repeated twice (which returns to the origin many times):

https://github.com/user-attachments/assets/3f226109-32f6-4381-84f9-b048bd06978c


#### [Ls_Semicompressible_Ink2d_v01.hiplc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_Semicompressible_Ink2d_v01.hiplc)
2D ink simulation from scratch using only microsolvers, blending back the effect of divergence-free projection to avoid excessive mushroom shapes:

https://github.com/user-attachments/assets/f1af625d-02dd-4921-adcc-a04b86c6db06


#### [Ls_Squish_v01.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_Squish_v01.hipnc)
Cheap trick to make meshes squish away from each other when in contact without any simulation:

https://github.com/user-attachments/assets/084022c2-775c-4e59-994a-e58003d28d1f


#### [Ls_TerrainFromContours_v02.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_TerrainFromContours_v02.hipnc)
Creates a smooth terrain from contour lines using thin plate spline interpolation, adapted from the RBF blendshape example in the Linear Solver SOP help page:

<img width="2560" height="1600" alt="Ls_TerrainFromContours_v01" src="https://github.com/user-attachments/assets/765c99a6-6ef5-4f7a-ac75-bfa5d35cffa6" />


#### [Ls_TurbulenceQ_v01.hipnc](https://github.com/lcrs/_.hips/raw/refs/heads/main/Ls_TurbulenceQ_v01.hipnc)
Extracts the Q-criterion isosurface beloved by aerospace CFD people from a smoke or pyro sim (it's the difference between the squared frobenius norms of the symmetric and anti-symmetric parts of the velocity gradient tensor, see https://www.m4-engineering.com/q-criterion-for-vortex-visualization):

https://github.com/user-attachments/assets/445e0c6c-a4eb-4907-9ef0-1cb60870c3ee






Everything else in here I have zero memory of don't @ me 🤍 lewis.saunders@gmail.com

(Older stuff might be on https://lewisinthelandofmachines.tumblr.com)
