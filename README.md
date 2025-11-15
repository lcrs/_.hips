# Houdini Hips

#### [Ls_ApexLol_v01.hipnc](./Ls_ApexLol_v01.hipnc)
APEX node graphs are stored as geometry so you can do silly things like move the nodes themselves around with attribnoise:

https://github.com/user-attachments/assets/598374e9-640f-4ea8-b978-7f94de4b3d33

#### [Ls_BlendshapeAlongSurface.hipnc](./Ls_BlendshapeAlongSurface.hipnc)
Using the vague concept of a "volumetric tangent space" for blendshaping so it doesn't move linearly, but follows the surface of the sphere to get to its final point (left is normal linear blendshape with obvious intersection and volume problems):

https://github.com/user-attachments/assets/3daf9345-0d87-436f-a49a-33efca1fd062

#### [Ls_Caustics_v01.hiplc](./Ls_Caustics_v01.hiplc)
Caustics are fun to play with in mantra, just set photon target on a caustic light to the transparent object and add a zero to the default photon count. Then constantly hit render in the IPR to update the map:

<img width="1293" height="717" alt="Ls_Caustics_v01" src="https://github.com/user-attachments/assets/9d99f77c-3bf9-4ee0-831d-fdb37678a0c5" />

#### [Ls_ColourBooper_v01.hipnc](./Ls_ColourBooper_v01.hipnc)
Semi-serious try at 3D colour correction with 5 from/to pickers using radial basis functions to stay smooth, kinda similar to the mesh-like colour warping in Baselight/Flame/Resolve:

https://github.com/user-attachments/assets/ead2cc2e-e160-45a9-83da-68dfa6ef0727

#### [Ls_Cop3AtomicAdd.hipnc](./Ls_Cop3AtomicAdd.hipnc)
Using OpenCL global atomic add tricks to render a buffer of point positions as single pixel particles super fast, a bit like Krakatoa or higx point render:

https://github.com/user-attachments/assets/30609454-98d0-46a3-883d-81831ba6363e

#### [Ls_Cop3Cooking.hipnc](./Ls_Cop3Cooking.hipnc)
Demo of slow apex graph cooking behaviour in COPs, maybe due to preview image generation. How can 3 blurs which must be hundreds of instructions run faster than what should be 3 mults and 3 adds plus some copying? Using invoke to run the same block is faster, even with enable compiling turned off:

<img width="1738" height="834" alt="Ls_Cop3Cooking" src="https://github.com/user-attachments/assets/471d372e-1840-4941-a638-1f5b0ffaff25" />

#### [Ls_Cop3LUTfromImage_v02](./Ls_Cop3LUTfromImage_v02)
There's no way to apply a 3D LUT in new-style COPs apart from the OCIO node (which is CPU-only) but if you encode one in an image you can do a reasonable job with OpenCL:

<img width="1920" height="1080" alt="Ls_Cop3LUTfromImage_v01" src="https://github.com/user-attachments/assets/5df6ecc2-5160-4cb2-946d-09308966cc55" />

#### [Ls_Cop3MatrixBinding_v01.hipnc](./Ls_Cop3MatrixBinding_v01.hipnc)
Demo of binding a 3@matrix attribute into OpenCL using float9. Admittedly confusing that you can't access the mat3 as an array of 9 floats since it's actually an array of fpreal3s (each of which is 4 floats wide even more confusingly):

<img width="1490" height="640" alt="copmatrix" src="https://github.com/user-attachments/assets/131eeec3-e7bf-4490-ac45-73cc366732a4" />

#### [Ls_Cop3PrefixsumGlow.hipnc](./Ls_Cop3PrefixsumGlow.hipnc)
The Prefix Sum COP makes summed area tables that let you do box filters of any size pretty much instantly, so you can add up tons of them to approximate the non-separable kernels of exponential or fibonacci glows (which look uncomfortably like having smudged glasses if you get the shape just right):

<img width="2560" height="1600" alt="Ls_Cop3PrefixsumGlow" src="https://github.com/user-attachments/assets/495ac1de-7cc3-4653-bac4-3b99bbbf24ef" />

#### [Ls_Cop3Tile_v01.hipnc](./Ls_Cop3Tile_v01.hipnc)
The Smooth Fill COP can be used for seamless edge blending, useful for tiled textures:

<img width="1918" height="916" alt="Ls_Cop3Tile_v01" src="https://github.com/user-attachments/assets/c5c2381f-b26a-464f-abcb-70ab86c89f56" />

#### [Ls_Cop3UVProject.hipnc](./Ls_Cop3UVProject.hipnc)
Camera projection in COPs. Recreating the projection itself in COPs is complicated, it's easier to project UVs from camera as a uv2 attrib in SOPs, then bake from uv2 to uv:

<img width="2672" height="1629" alt="Ls_Cop3UVProject" src="https://github.com/user-attachments/assets/f69d6bc8-82cb-40cb-9154-f8550dec79d8" />

#### [Ls_CurveExtrapolate.hipnc](./Ls_CurveExtrapolate.hipnc)
Extrapolating a curve using taylor polynomials. You can enable gradient3 and gradient4 as well but it gets a bit spicy:

https://github.com/user-attachments/assets/d58d709d-7c4b-41ca-9edc-0990bd77d081

#### [Ls_KarmaMandelbulb](./Ls_KarmaMandelbulb)
The HDK comes with a Karma procedural that renders a mandelbulb in VEX without having to create any geometry (sadly it crashes as soon as you change any of the parameters in 20.5.361 unless you switch the renderer from Karma CPU to something else and then back again):

<img width="2560" height="1462" alt="Ls_KarmaMandelbulb" src="https://github.com/user-attachments/assets/8ee538ab-d207-4d4f-9962-f442dbbd91ff" />

#### [Ls_KarmaPNGslapcompACES_v01.hipnc](./Ls_KarmaPNGslapcompACES_v01.hipnc)
Probably the best we can do in 21.0 to render PNGs from Karma with an OCIO view transform baked in, by applying it with a slapcomp block and passing `--ocio 0` to husk so it doesn't do another transform... it matches rendering an EXR and applying the view transform afterwards in COPs:

<img width="2559" height="1320" alt="Ls_KarmaPNGslapcompACES_v01" src="https://github.com/user-attachments/assets/c23c8a5b-a734-488d-ae2d-15baaaa40658" />

#### [Ls_KarmaSunset_v01](./Ls_KarmaSunset_v01)
You can sorta render a sunset using a uniform volume on a sphere as big as the entire earth with a geo-referenced DEM terrain, letting the atmosphere both scatter and absorb the same colour so the sky gradient from the low-angle sun appears naturally:

<img width="1985" height="857" alt="Ls_KarmaSunset_v01" src="https://github.com/user-attachments/assets/34b49392-95c7-40c3-aed7-08908b59b9fe" />

#### [Ls_MatrixFromChart_v01b.hipnc](./Ls_MatrixFromChart_v01b.hipnc)
Extracts a best-fit 3x3 matrix from two Macbeth chart images similarly to mmColorTarget using everyone's favourite, the Linear Solver SOP:

<img width="2560" height="1487" alt="Ls_MatrixFromChart_v01" src="https://github.com/user-attachments/assets/1a30e0f6-d35c-478f-86aa-d5a005937645" />

#### [Ls_Ramprefine_v01.hiplc](./Ls_Ramprefine_v01.hiplc)
Simplifying colour ramps that have way too many points by treating them as 3D paths in RGB space:

https://github.com/user-attachments/assets/9da0f16f-a628-4aed-a6d0-662202ece5c5

#### [Ls_RotationWalksHome_v03.hipnc](./Ls_RotationWalksHome_v03.hipnc)
Visualizing the main result of https://arxiv.org/abs/2502.14367v3 by showing rotation vectors in SO(3) for 50 walks as their angle scales increase over time, both on the left walking once (which never returns to the origin) and on the right the same walk repeated twice (which returns to the origin many times):

https://github.com/user-attachments/assets/3f226109-32f6-4381-84f9-b048bd06978c

#### [Ls_Semicompressible_Ink2d_v01.hiplc](./Ls_Semicompressible_Ink2d_v01.hiplc)
2D ink simulation from scratch using only microsolvers, blending back the effect of divergence-free projection to avoid excessive mushroom shapes:

https://github.com/user-attachments/assets/f1af625d-02dd-4921-adcc-a04b86c6db06

#### [Ls_Squish_v01.hipnc](./Ls_Squish_v01.hipnc)
Cheap trick to make meshes squish away from each other when in contact without any simulation:

https://github.com/user-attachments/assets/084022c2-775c-4e59-994a-e58003d28d1f

#### [Ls_TerrainFromContours_v02.hipnc](./Ls_TerrainFromContours_v02.hipnc)
Creates a smooth terrain from contour lines using thin plate spline interpolation, adapted from the RBF blendshape example in the Linear Solver SOP help page:

<img width="2560" height="1600" alt="Ls_TerrainFromContours_v01" src="https://github.com/user-attachments/assets/765c99a6-6ef5-4f7a-ac75-bfa5d35cffa6" />

#### [Ls_TurbulenceQ_v01.hipnc](./Ls_TurbulenceQ_v01.hipnc)
Extracts the Q-criterion isosurface beloved by aerospace CFD people from a smoke or pyro sim (it's the difference between the squared frobenius norms of the symmetric and anti-symmetric parts of the velocity gradient tensor, see https://www.m4-engineering.com/q-criterion-for-vortex-visualization):

https://github.com/user-attachments/assets/445e0c6c-a4eb-4907-9ef0-1cb60870c3ee

#### [Ls_ViewportCameraGeoSync.hipnc](./Ls_ViewportCameraGeoSync.hipnc)
Demo of a strange viewport bug. The capy and camera are in sync when hitting play, but when scrubbing the timeline he's all over the shop:

https://github.com/user-attachments/assets/18be003d-dcb7-4d79-834d-a9c52088a267

Everything else in here I have zero memory of don't @ me 🤍 lewis.saunders@gmail.com

(Older stuff might be on https://lewisinthelandofmachines.tumblr.com)
