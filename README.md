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
Slow apex graph cooking behaviour in COPs, possibly due to preview image generation. How can 3 blurs which must be hundreds of instructions run faster than what should be 3 mults and 3 adds plus some copying? Using invoke to run the same block is faster, even with enable compiling turned off:

<img width="1738" height="834" alt="Ls_Cop3Cooking" src="https://github.com/user-attachments/assets/471d372e-1840-4941-a638-1f5b0ffaff25" />

#### [Ls_Cop3LUTfromImage_v02](./Ls_Cop3LUTfromImage_v02)
There's no way to apply a 3D LUT in new-style COPs apart from the OCIO node (which is CPU-only) but if you encode one in an image you can do a reasonable job with OpenCL:

<img width="1920" height="1080" alt="Ls_Cop3LUTfromImage_v01" src="https://github.com/user-attachments/assets/5df6ecc2-5160-4cb2-946d-09308966cc55" />

#### [Ls_Cop3MatrixBinding_v01.hipnc](./Ls_Cop3MatrixBinding_v01.hipnc)
Binding a `3@matrix` attribute into OpenCL using `float9`, then loading it with `mat3load().`. Admittedly it's confusing you can't access the mat3 as an array of 9 floats since it's actually an array of fpreal3s (each of which is 4 floats wide even more confusingly):

<img width="1490" height="640" alt="copmatrix" src="https://github.com/user-attachments/assets/131eeec3-e7bf-4490-ac45-73cc366732a4" />

```js
#bind layer src? val=0
#bind layer !&dst
#bind point mat float9 port=geo

@KERNEL
{
    // Load 3@ matrix attrib from point chosen by pixel y coord
    mat3 m;
    mat3load(0, @mat.tupleAt(@iy), m);
    @dst.set((float4)(m[0].x, m[0].y, m[0].z, m[1].x));
}
```

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

#### [Ls_DopsVolumeStreak_v01.hipnc](./Ls_DopsVolumeStreak_v01.hipnc)
Velocity extrapolation bug in DOPs. When velocity sampling is set to streak, velocity at the border is reflected back into the system. Changing velocity sampling to corner keeps it stable, as does turning closed boundaries on (but changes the look a lot). Bizarrely it also stays stable if you enable OpenCL on Gas Enforce Boundary DOP:

https://github.com/user-attachments/assets/fa8a503c-6572-434b-8d7a-85df603bcb7a

#### [Ls_GlancingReflectionBug_v01.hipnc](./Ls_GlancingReflectionBug_v01.hipnc)
Demo of a strange bent reflection bug. It can be fixed by reversing the normals or vertex order, or by rotating the grid:

<img width="1919" height="919" alt="Ls_GlancingReflectionBug_v01" src="https://github.com/user-attachments/assets/e80e9e22-db71-47ed-8439-32006cb22361" />

#### [Ls_HairgenFromLines_v03.hiplc](./Ls_HairgenFromLines_v03.hiplc)
Using hairgen to create geo at render time from guide hairs which are just SOPs lines, with random variation done inside the hairgen:

<img width="2560" height="1600" alt="Ls_HairgenFromLines_v03" src="https://github.com/user-attachments/assets/eb9b10c7-639a-4515-838a-048e0761be55" />

#### [Ls_KarmaMandelbulb](./Ls_KarmaMandelbulb)
The HDK comes with a Karma procedural that renders a mandelbulb in VEX without having to create any geometry (sadly it crashes as soon as you change any of the parameters in 20.5.361 unless you switch the renderer from Karma CPU to something else and then back again):

<img width="2560" height="1462" alt="Ls_KarmaMandelbulb" src="https://github.com/user-attachments/assets/8ee538ab-d207-4d4f-9962-f442dbbd91ff" />

#### [Ls_KarmaPNGslapcompACES_v01.hipnc](./Ls_KarmaPNGslapcompACES_v01.hipnc)
Probably the best we can do in 21.0 to render PNGs from Karma with an OCIO view transform baked in, by applying it with a slapcomp block and passing `--ocio 0` to husk so it doesn't do another transform... it matches rendering an EXR and applying the view transform afterwards in COPs:

<img width="2559" height="1320" alt="Ls_KarmaPNGslapcompACES_v01" src="https://github.com/user-attachments/assets/c23c8a5b-a734-488d-ae2d-15baaaa40658" />

#### [Ls_KarmaSunset_v01](./Ls_KarmaSunset_v01)
You can sorta render a sunset using a uniform volume on a sphere as big as the entire earth with a geo-referenced DEM terrain, letting the atmosphere both scatter and absorb the same colour so the sky gradient from the low-angle sun appears naturally:

<img width="1985" height="857" alt="Ls_KarmaSunset_v01" src="https://github.com/user-attachments/assets/34b49392-95c7-40c3-aed7-08908b59b9fe" />

#### [Ls_LOPsFrustrumClipMaybe_v01.hipnc](./Ls_LOPsFrustrumClipMaybe_v01.hipnc)
Pruning primitives outside of an SDF VDB in LOPs. Sample your SOP VDB at the center of each prim in LOPs to check if it's outside:

<img width="2672" height="1629" alt="Ls_LOPsFrustrumClipMaybe_v01" src="https://github.com/user-attachments/assets/51e6005d-0eb4-4277-b875-925b3015c006" />

#### [Ls_MantraShadowMask_v01.hipnc](./Ls_MantraShadowMask_v01.hipnc)
Making a shadow map by grabbing the direct shadow AOV from the PBR Lighting VOP, then slipping it into a multiply of Ce before adding to the main lighting result. This way you get a soft shadow mask even from texture displacement:

<img width="2219" height="993" alt="Ls_MantraShadowMask_v01" src="https://github.com/user-attachments/assets/0b986631-177a-4b66-b46c-62414e4201fa" />

#### [Ls_MatrixFromChart_v01b.hipnc](./Ls_MatrixFromChart_v01b.hipnc)
Extracts a best-fit 3x3 matrix from two Macbeth chart images similarly to mmColorTarget using everyone's favourite, the Linear Solver SOP:

<img width="2560" height="1487" alt="Ls_MatrixFromChart_v01" src="https://github.com/user-attachments/assets/1a30e0f6-d35c-478f-86aa-d5a005937645" />

#### [Ls_MeshDivergence.hipnc](./Ls_MeshDivergence.hipnc)
The Measure node can compute the gradient of an attribute, but the divergence in cartesian coordinates is harder to compute. This HIP compares the gradient sum to Jake Rice's method:

<img width="2672" height="1629" alt="Ls_MeshDivergence" src="https://github.com/user-attachments/assets/f59848c7-838c-4676-a64f-a2adfc467d69" />

Jake Rice notes:

> The divergence of a vector field on the surface is not the same as the laplacian of that vector field. If you want the divergence of the gradient of a scalar field, then the laplacian option on the neasure SOP does work. But if you just want the actual divergence of an arbitrary vector field, you'd have to write the math yourself I believe.
>
> Divergence on discrete surfaces is a troublesome idea, and it's not as simple as summing the components of the gradients of the vector field. The way you compute divergence depends on what element the vector field is discretized on. The easiest form I know is when your vector field is described on faces. It requires you have a div attribute set to 0 on your points:

```js
vector edge (int h) {
    return vector(point(0, "P", hedge_dstpoint(0, h))) - vector(point(0, "P", hedge_srcpoint(0, h)));
}

float cot_weight (int h) {
    int next = hedge_next(0, h);
    int prev = hedge_next(0, next);
    vector e1 = -normalize(edge(next));
    vector e2 = normalize(edge(prev));
    return dot(e1, e2) / (length(cross(e1, e2)) + 1e-8);
}

int h = primhedge(0, @primnum);
int temp = h;
vector field = prim(0, chs("YOUR_VECTOR_FIELD_HERE"), @primnum);

do {
    int src = hedge_srcpoint(0, h);
    int prev = hedge_prev(0, h);
    
    float e1_ang = cot_weight(h); //angle opposite the edge
    float e2_ang = cot_weight(prev);//angle opposite the prev
    
    float div_at_src = e1_ang * dot(edge(h), field) + e2_ang * dot(-edge(prev), field);
    setpointattrib(0, "div", src,  div_at_src * .5, "add");

    h = hedge_next(0, h);
} while (h != temp);
```

More Jake notes:

> Divergence of a vector field on prims results in values on points. To explain requires a large amount of discrete differential geometry, you'd have to watch [Keenan Crane's lectures](https://www.youtube.com/watch?v=8JCR6z3GLVI).
>
> Divergence corresponds with the inflow and outflow of values from a region of space. To take the divergence of your field on a surface, you need to do it with respect to the "basis directions" of that geometry. In this case it's somewhat defined by the edge vectors of a given prim.
>
> In the world of differential geo, the vector field defined on faces is described as a "discrete 1-form", which is actually scalars on edges. Any vector tangent to the face of a triangle can be composed by taking a weighted sum of the edge vectors of that triangle. 
>
> There are operators called "exterior derivatives", ways of interpolating values from points to edges and then to faces (in the case of triangle meshes). Then there are duals, which let you interpolate values from faces to edges and to points by working on the dual mesh instead. To be clear you can only really go from points to faces, but since you work on the dual mesh, a face in our original mesh is a dual point in the dual mesh. The hodge star operator lets you switch from points to dual faces, or edges to dual edges, etc.
>
> The way you compute the divergence of a field is by starting with a vector field (values per edge, or vectors on faces). Then you apply this set of operations `* d *` where `*` is the hodge star and `d` is the exterior derivative. We start with a 1 form, and as we apply the operators in order we end up with a 0 form, and the divergence of our original field.

| 1 form | --> | --> | 0 form |
| --- | --- | --- | --- |
| <img src="https://github.com/user-attachments/assets/af6bc34b-5ebe-4ac9-a74f-29199ee9aa08" /> | <img src="https://github.com/user-attachments/assets/9039eaa8-bbe0-4314-b720-aaa47021bae6" /> | <img src="https://github.com/user-attachments/assets/bb6ae6c4-a0fd-4e53-af19-142229604068" /> | <img src="https://github.com/user-attachments/assets/481f5e09-ce9c-41bd-bbe1-9d16243cd368" /> |

#### [Ls_MotionVectors_v01.hip](./Ls_MotionVectors_v01.hip)
Inline code snippet to output 2D motion vectors in absolute pixels, for 2D vector blur in comp. Works on both geometry and volumes, as seen in [Ls_VolumeMotionVectors](#ls_volumemotionvectors_v01hipnc--ls_volumemotionvectorsnodes_v01hipnc):

<img width="1919" height="919" alt="Ls_MotionVectors_v01" src="https://github.com/user-attachments/assets/c6c31036-6acf-4e69-85d5-89653d9a7e79" />

```js
// 2D motion vector output in absolute pixels, lewis@lewissaunders.com July 2018
// Paste this in an Inline Code VOP, enable "Expand Expressions in Code"
// Connect a Bind set to "vel", type Vector, to the first input
// Set Output 1 Name to "mv", type Vector
// Connect the output to a Bind Export set to the name used in Mantra's image planes
// Make sure motion blur is enabled on the ROP, even if "Allow Image Motion Blur" is not
vector ndcv = toNDC(getblurP(1.0)) - toNDC(getblurP(0.0));
string engine; renderstate("renderer:renderengine", engine);
if((engine == "raytrace" || engine == "pbrraytrace") && isbound("vel")) {
    // When rendering volumes in raytrace mode the getblurP() method doesn't work, but we do the best we can
    // It's correct for a static camera but there's no way to incorporate camera motion. For simple camera moves
    // the camera motion vectors can be added to this in comp before the blur is done... to get solid vectors
    // from a volume the density normally needs to be increased a lot anyway, and rendered as another pass, so
    // it might be better to just do that pass in micropoly mode :)
    vector p0 = getblurP(0.0);
    vector framev = vel / $FPS;
    vector camerav = vtransform("space:object", "space:camera", framev);
    ndcv = toNDC(p0 + camerav) - toNDC(p0);
}
vector res; renderstate("image:resolution", res);
ndcv *= set(res.x, res.y, 0.0);
\$mv = ndcv;
```

#### [Ls_PackedGeoRayCull.hipnc](./Ls_PackedGeoRayCull.hipnc)
Culls packed prims based on the Ray SOP. The sphere rays out in every direction, records hitprim from the packed geo, then `findattribvalcount()` checks if each piece of packed geo had a hit recorded:

<img width="2560" height="1600" alt="Ls_PackedGeoRayCull" src="https://github.com/user-attachments/assets/434751f3-c2ab-4e95-8b93-878eff904c09" />

#### [Ls_PopTrails_v01.hipnc](./Ls_PopTrails_v01.hipnc)
Particle trail using a Trail SOP followed by an Add SOP set to connect points with a matching ID attribute.

<img width="1189" height="812" alt="Ls_PopTrails_v01" src="https://github.com/user-attachments/assets/471ba3fe-98ba-48c2-8b4a-be9da376f3a9" />

#### [Ls_Ramprefine_v01.hiplc](./Ls_Ramprefine_v01.hiplc)
Simplifying colour ramps that have way too many points by treating them as 3D paths in RGB space:

https://github.com/user-attachments/assets/9da0f16f-a628-4aed-a6d0-662202ece5c5

#### [Ls_RotationWalksHome_v03.hipnc](./Ls_RotationWalksHome_v03.hipnc)
Visualizing the main result of https://arxiv.org/abs/2502.14367v3 by showing rotation vectors in SO(3) for 50 walks as their angle scales increase over time, both on the left walking once (which never returns to the origin) and on the right the same walk repeated twice (which returns to the origin many times):

https://github.com/user-attachments/assets/3f226109-32f6-4381-84f9-b048bd06978c

#### [Ls_Semicompressible_Ink2d_v01.hiplc](./Ls_Semicompressible_Ink2d_v01.hiplc)
2D ink simulation from scratch using only microsolvers, blending back the effect of divergence-free projection to avoid excessive mushroom shapes:

https://github.com/user-attachments/assets/f1af625d-02dd-4921-adcc-a04b86c6db06

#### [Ls_Shadowgeo_v01.hiplc](./Ls_Shadowgeo_v01.hiplc)
Faking shadows using geometry raycast away from a point light source.

<img width="1916" height="917" alt="Ls_Shadowgeo_v01" src="https://github.com/user-attachments/assets/0896a152-d2af-46fa-9aac-931ce4e39ffe" />

#### [Ls_SquashSomePrims_v01.hiplc](./Ls_SquashSomePrims_v01.hiplc)
VEX snippet to squash some primitives and accumulate the offset to maintain the spacing of the others.

<img width="1916" height="920" alt="Ls_SquashSomePrims_v01" src="https://github.com/user-attachments/assets/80fbca4b-4b92-4e49-9cfe-4cbc69516f7c" />

#### [Ls_Squish_v01.hipnc](./Ls_Squish_v01.hipnc)
Cheap trick to make meshes squish away from each other when in contact without any simulation:

https://github.com/user-attachments/assets/084022c2-775c-4e59-994a-e58003d28d1f

#### [Ls_Skeletonize_v01.hiplc](./Ls_Skeletonize_v01.hiplc)
Generates a 2D straight skeleton by advecting points toward the SDF center, similar to [Labs Straight Skeleton 2D](https://www.sidefx.com/docs/houdini/nodes/sop/labs--straight_skeleton_2D.html):

<img width="1918" height="916" alt="Ls_Skeletonize_v01" src="https://github.com/user-attachments/assets/f0a97a45-bd10-48bb-9bfa-b9f4b0efc421" />

#### [Ls_TerrainFromContours_v02.hipnc](./Ls_TerrainFromContours_v02.hipnc)
Creates a smooth terrain from contour lines using thin plate spline interpolation, adapted from the RBF blendshape example in the Linear Solver SOP help page:

<img width="2560" height="1600" alt="Ls_TerrainFromContours_v01" src="https://github.com/user-attachments/assets/765c99a6-6ef5-4f7a-ac75-bfa5d35cffa6" />

#### [Ls_TiledVDBRender_v01.hipnc](./Ls_TiledVDBRender_v01.hipnc)
Attempting to render multiple VDB volumes without edge artifacts:

<img width="1919" height="916" alt="Ls_TiledVDBRender_v01" src="https://github.com/user-attachments/assets/e1e8e396-8dd3-4b1a-a11d-5260b3e6d0c2" />

#### [Ls_TurbulenceQ_v01.hipnc](./Ls_TurbulenceQ_v01.hipnc)
Extracts the Q-criterion isosurface beloved by aerospace CFD people from a smoke or pyro sim (it's the difference between the squared frobenius norms of the symmetric and anti-symmetric parts of the velocity gradient tensor, see https://www.m4-engineering.com/q-criterion-for-vortex-visualization):

https://github.com/user-attachments/assets/445e0c6c-a4eb-4907-9ef0-1cb60870c3ee

#### [Ls_ViewportCameraGeoSync.hipnc](./Ls_ViewportCameraGeoSync.hipnc)
Strange viewport bug with camera syncing. The capy and camera are in sync when hitting play, but when scrubbing the timeline he's all over the shop:

https://github.com/user-attachments/assets/18be003d-dcb7-4d79-834d-a9c52088a267

#### [Ls_ViewportText_v01.hip](./Ls_ViewportText_v01.hip)
Using tag visualizers in dummy geo objects parented under the camera. This allows color control, and is easy to move around rather than being stuck in the corner.

<img width="1917" height="916" alt="Ls_ViewportText_v01" src="https://github.com/user-attachments/assets/95f28272-254b-4536-8f5f-df1d04f544d9" />

#### [Ls_VolumeMotionVectors_v01.hipnc](./Ls_VolumeMotionVectors_v01.hipnc) / [Ls_VolumeMotionVectorsNodes_v01.hipnc](./Ls_VolumeMotionVectorsNodes_v01.hipnc)
Inline code snippet to output 2D motion vectors in absolute pixels, as seen in [Ls_MotionVectors](#ls_motionvectors_v01hip). Motion vectors for volumes are tricky because of transparency. A wispy bit of smoke moving fast will get motion vectors near 0 because it's not opaque enough for its true velocity colour to show. One solution is increasing the density so you only see the vel at the front of the volume:

<img width="1919" height="916" alt="Ls_VolumeMotionVectors_v01" src="https://github.com/user-attachments/assets/f93329e8-ca8f-47a6-a1fb-d29a291784e9" />

Everything else in here I have zero memory of don't @ me 🤍 lewis.saunders@gmail.com

(Older stuff might be on https://lewisinthelandofmachines.tumblr.com)
