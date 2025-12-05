#### [Ls_AF1TransonicRegime_v01.hipnc](./Ls_AF1TransonicRegime_v01.hipnc)
Aligning arrows to follow a pyro sim... don't mind that it's on a shoe (loud video):

https://github.com/user-attachments/assets/eee24241-f285-408a-b6ff-8bee8f861d8c

#### [Ls_AncientScrolls_v01.hiplc](./Ls_AncientScrolls_v01.hiplc)
Unwrapping layers of papyrus from CT scans of the Herculaneum scrolls - could see the crosshatching of the reeds woven together but no ink or writing (loud video):

https://github.com/user-attachments/assets/db59fdab-e19f-42d4-babc-3f1de05bb510

#### [Ls_ApexLol_v01.hipnc](./Ls_ApexLol_v01.hipnc)
APEX node graphs are stored as geometry so you can do silly things like move the nodes themselves around with attribnoise:

https://github.com/user-attachments/assets/598374e9-640f-4ea8-b978-7f94de4b3d33

#### [Ls_BlendshapeAlongSurface.hipnc](./Ls_BlendshapeAlongSurface.hipnc)
Using the vague concept of a "volumetric tangent space" for blendshaping so it doesn't move linearly, but follows the surface of the sphere to get to its final point (left is normal linear blendshape with obvious intersection and volume problems):

https://github.com/user-attachments/assets/3daf9345-0d87-436f-a49a-33efca1fd062

#### [Ls_Caustics_v01.hiplc](./Ls_Caustics_v01.hiplc)
Mantra rendered caustics in a quite different way to how Karma now does and they can still be fun to play with... just set photon target on a caustic light to the transparent object and add a zero to the default photon count, then constantly hit render in the IPR to update the map:

<img width="1293" height="717" alt="Ls_Caustics_v01" src="https://github.com/user-attachments/assets/9d99f77c-3bf9-4ee0-831d-fdb37678a0c5" />

#### [Ls_ColourBooper_v01.hipnc](./Ls_ColourBooper_v01.hipnc)
Semi-serious try at 3D colour correction with 5 from/to pickers using radial basis functions to stay smooth, kinda similar to the mesh-like colour warping in Baselight/Flame/Resolve:

https://github.com/user-attachments/assets/ead2cc2e-e160-45a9-83da-68dfa6ef0727

#### [Ls_Cop3AtomicAdd.hipnc](./Ls_Cop3AtomicAdd.hipnc)
Using OpenCL global atomic add tricks to render a buffer of point positions as single pixel particles super fast, a bit like Krakatoa or higx point render:

https://github.com/user-attachments/assets/30609454-98d0-46a3-883d-81831ba6363e

```js
#bind layer src read
#bind layer dummy write opt
#bind layer dst write

// https://violetspace.github.io/blog/atomic-float-addition-in-opencl.html
inline void atomic_add_f(volatile __global float* addr, const float val) {
    #if defined(cl_nv_pragma_unroll)
            float ret; asm volatile("atom.global.add.f32 %0,[%1],%2;":"=f"(ret):"l"(addr),"f"(val):"memory");
    #elif defined(__opencl_c_ext_fp32_global_atomic_add)
            atomic_fetch_add_explicit((volatile global atomic_float*)addr, val, memory_order_relaxed);
    #elif __has_builtin(__builtin_amdgcn_global_atomic_fadd_f32)
            __builtin_amdgcn_global_atomic_fadd_f32(addr, val);
    #else
            float old = val; while((old=atomic_xchg(addr, atomic_xchg(addr, 0.0f)+old))!=0.0f);
    #endif
}

@KERNEL {
    int2 xy = convert_int2(@src.xy * @dst.res);
    int idx = _linearIndex(@dst.stat, xy);
    atomic_add_f((global float *)_bound_dst + idx, 0.01);  
}
```

#### [Ls_Cop3GPUparticles_v01.hipnc](./Ls_Cop3GPUparticles_v01.hipnc)
Crude demo of 6 million particles simulating and rendering at 60fps all on the GPU in COPs, using a simulate block with position and velocity buffers and the above atomic add trick:

https://github.com/user-attachments/assets/78fb20ec-4bd4-4173-bb92-8214f00ef912

#### [Ls_Cop3GPUparticles_v03.hipnc](./Ls_Cop3GPUparticles_v03.hipnc)
Similar to above but also cheaply rasterizing the particles onto an image layer inside the simulate block then using the derivatives of that image to get a force towards the local concentration of particles, like hard-to-control but very fast flocking or the particle/grid transfer that forms the basis of FLIP:

https://github.com/user-attachments/assets/972a29c1-8473-4e1b-b661-3bfce6ea87cf

#### [Ls_Cop3LUTfromImage_v02](./Ls_Cop3LUTfromImage_v02)
There's no way to apply a 3D LUT in new-style COPs apart from the OCIO node (which is CPU-only) but if you encode one in an image you can do a reasonable job with OpenCL:

<img width="1920" height="1080" alt="Ls_Cop3LUTfromImage_v01" src="https://github.com/user-attachments/assets/5df6ecc2-5160-4cb2-946d-09308966cc55" />

#### [Ls_Cop3MatrixBinding_v01.hipnc](./Ls_Cop3MatrixBinding_v01.hipnc)
Binding a `3@matrix` attribute into OpenCL using `float9`, then loading it with `mat3load()`. Admittedly it's confusing you can't access the mat3 as an array of 9 floats since it's actually an array of fpreal3s (each of which is 4 floats wide even more confusingly):

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

```js
#bind layer src
#bind layer psum
#bind layer !&dst
#bind parm size float
#bind parm shape float
#bind parm layers int

@KERNEL {
    float w = @size / 20;
    float4 acc = 0.0;
    for(int i = 0; i < @layers; i++) {
        // https://en.wikipedia.org/wiki/Summed-area_table
        acc += (@psum(@P + (float2)(w, w)) + @psum(@P + (float2)(-w, -w)) - @psum(@P + (float2)(-w, w)) - @psum(@P + (float2)(w, -w)))
               / (float4)(2 * w * @res.x * w * @res.y);
        w *= 1 + @shape;
    }

    @dst.set(@src + acc / (float4)@layers);
}
```

#### [Ls_Cop3Tile_v01.hipnc](./Ls_Cop3Tile_v01.hipnc)
The Smooth Fill COP can be used for seamless edge blending, useful for tiled textures:

<img width="1918" height="916" alt="Ls_Cop3Tile_v01" src="https://github.com/user-attachments/assets/c5c2381f-b26a-464f-abcb-70ab86c89f56" />

#### [Ls_Cop3UVProject.hipnc](./Ls_Cop3UVProject.hipnc)
Camera projection in COPs by simply projecting UVs from camera as a uv2 attrib in SOPs, then baking from uv2 to uv:

<img width="2672" height="1629" alt="Ls_Cop3UVProject" src="https://github.com/user-attachments/assets/f69d6bc8-82cb-40cb-9154-f8550dec79d8" />

#### [Ls_CurveExtrapolate.hipnc](./Ls_CurveExtrapolate.hipnc)
Extrapolating a curve using Taylor polynomials (can enable gradient3 and gradient4 as well but it gets a bit spicy):

https://github.com/user-attachments/assets/d58d709d-7c4b-41ca-9edc-0990bd77d081

#### [Ls_DopsVolumeStreak_v01.hipnc](./Ls_DopsVolumeStreak_v01.hipnc)
Velocity extrapolation weirdness in DOPs... when velocity sampling is set to streak, velocity at the border is reflected back into the system. Changing velocity sampling to corner keeps it stable, as does turning closed boundaries on (but changes the look a lot). Bizarrely it also stays stable if you enable OpenCL on Gas Enforce Boundary DOP:

https://github.com/user-attachments/assets/fa8a503c-6572-434b-8d7a-85df603bcb7a

#### [Ls_GeoTangentSpaceTransfer_v02.hipnc](./Ls_GeoTangentSpaceTransfer_v02.hipnc)
Easily memorable way to transfer a sculpt or other shape change from a rest pose to a different pose by storing the difference in tangent space, simply using dot products with N/tangentu/tangentv without needing to remember which bit is which in a TBN matrix (may not match the MikkT standard though):

<img width="2560" height="1467" alt="Ls_GeoTangentSpaceTransfer_v02" src="https://github.com/user-attachments/assets/f5c89c54-3096-4ed1-89c7-4318537de982" />

#### [Ls_GeoFreqSep_v02.hipnc](./Ls_GeoFreqSep_v02.hipnc)
Splits a mesh into low and high frequency parts, then uses the tangent space transfer trick above to offset the high frequencies in UV space:

https://github.com/user-attachments/assets/46b41c99-ad94-442c-af1f-75a94465d497

#### [Ls_GlancingReflectionBug_v01.hipnc](./Ls_GlancingReflectionBug_v01.hipnc)
Demo of strangely warped reflections at close-to-tangent ray incidence - goes away in Karma XPU or when changing vertex order/normal direction:

<img width="1919" height="919" alt="Ls_GlancingReflectionBug_v01" src="https://github.com/user-attachments/assets/e80e9e22-db71-47ed-8439-32006cb22361" />

#### [Ls_houCLfuncs.py](./Ls_houCLfuncs.py)
Generates a list of OpenCL functions in Houdini's include folder using the cpp preprocessor and https://ctags.io/ - output looks like [Ls_houCLfuncs.cl](./Ls_houCLfuncs.cl)

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
Pruning primitives outside of an animated camera's accumulated viewing volume by sampling a SOPs VDB at the center of each prim in LOPs to check if it's outside:

<img width="2672" height="1629" alt="Ls_LOPsFrustrumClipMaybe_v01" src="https://github.com/user-attachments/assets/51e6005d-0eb4-4277-b875-925b3015c006" />

```js
vector center = usd_getbbox_center(0, @primpath, @primpurpose);
float sdf = volumesample('op:/stage/sdf/frustrum/FrustrumVDB', 0, center);
if(sdf > 0.0) {
    usd_setactive(0, @primpath, 0);
}
```

#### [Ls_MatrixFromChart_v01c.hipnc](./Ls_MatrixFromChart_v01c.hipnc)
Extracts a best-fit 3x3 matrix from two Macbeth chart images similarly to mmColorTarget using everyone's favourite, the Linear Solver SOP:

<img width="2560" height="1487" alt="Ls_MatrixFromChart_v01" src="https://github.com/user-attachments/assets/1a30e0f6-d35c-478f-86aa-d5a005937645" />

#### [Ls_MatrixInterp_v01.hiplc](./Ls_MatrixInterp_v01.hiplc)
Interpolating between two matrices using `slerp()` so the transform stays rigid and doesn't introduce weird shears like interpolating the matrix values directly does:

<img width="1919" height="919" alt="Ls_MatrixInterp_v01" src="https://github.com/user-attachments/assets/e44d1f4b-f240-4d20-8ebe-d88a2ff799f8" />

#### [Ls_OldBubbleSim_v07.hiplc](./Ls_OldBubbleSim_v07.hiplc)
Soap bubble simulated as 2D smoke with a noise texture mapped to the advected "single rest" field in COPs, rendered with Arnold's thin film shader - doing that keeps far more detail than trying to advect the noise texture directly, and resizing the rest field up 3x before mapping makes it look as if the whole thing was done with an extra 3x3 worth of antialiasing: 

https://github.com/user-attachments/assets/467113a6-0022-4068-886b-ddd9e7b79387

#### [Ls_PackedGeoRayCull.hipnc](./Ls_PackedGeoRayCull.hipnc)
Keeps only packed prims that are visible from a point by casting rays - it may seem surprising that the Ray SOP can trace against packed prims since most SOPs only treat them as a single point, but thinking of them as render time instances hints that it should work and be fast... the rays record hitprim from the packed geo, then `findattribvalcount()` checks if each piece had a hit recorded:

<img width="2560" height="1600" alt="Ls_PackedGeoRayCull" src="https://github.com/user-attachments/assets/434751f3-c2ab-4e95-8b93-878eff904c09" />

### [Ls_PyroType_v03.hiplc](./Ls_PyroType_v03.hiplc)
Silly experiment advecting the control points of beziers with a pyro sim:

https://github.com/user-attachments/assets/f7bc62d7-0bdf-49cd-b7ab-6521e6f4323c

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

```js
int squashcount = 0;
for(int i = 0; i < nprimitives(0); i++) {
    if(inprimgroup(0, "squash", i-1)) {
        squashcount++;
    }
    foreach(int p; primpoints(0, i)) {
        vector oldpos = point(0, 'P', p);
        vector newpos = oldpos;
        newpos.x -= squashcount * chf('squashfactor');
        setpointattrib(0, 'P', p, newpos);
    }
}
```

#### [Ls_Squish_v01.hipnc](./Ls_Squish_v01.hipnc)
Cheap trick to make meshes squish away from each other when in contact without any simulation:

https://github.com/user-attachments/assets/084022c2-775c-4e59-994a-e58003d28d1f

#### [Ls_Skeletonize_v01.hiplc](./Ls_Skeletonize_v01.hiplc)
Generates a 2D straight skeleton by advecting points toward the SDF center, similar to [Labs Straight Skeleton 2D](https://www.sidefx.com/docs/houdini/nodes/sop/labs--straight_skeleton_2D.html):

<img width="1918" height="916" alt="Ls_Skeletonize_v01" src="https://github.com/user-attachments/assets/f0a97a45-bd10-48bb-9bfa-b9f4b0efc421" />

#### [Ls_TerrainFromContours_v02.hipnc](./Ls_TerrainFromContours_v02.hipnc)
Creates a smooth terrain from contour lines using thin plate spline interpolation, adapted from the RBF blendshape example in the Linear Solver SOP help page:

<img width="2560" height="1600" alt="Ls_TerrainFromContours_v01" src="https://github.com/user-attachments/assets/765c99a6-6ef5-4f7a-ac75-bfa5d35cffa6" />

#### [Ls_TurbulenceQ_v01.hipnc](./Ls_TurbulenceQ_v01.hipnc)
Extracts the Q-criterion isosurface beloved by aerospace CFD people from a smoke or pyro sim (it's the difference between the squared frobenius norms of the symmetric and anti-symmetric parts of the velocity gradient tensor, see https://www.m4-engineering.com/q-criterion-for-vortex-visualization):

https://github.com/user-attachments/assets/445e0c6c-a4eb-4907-9ef0-1cb60870c3ee

#### [Ls_TwitterArea_v04.hipnc](./Ls_TwitterArea_v04.hipnc)
Builds a geometry network with friend/following relations from a social media graph and simulates it to see which parts cluster naturally together (big mess, for more see https://github.com/lcrs/twarea):

https://github.com/user-attachments/assets/28b10797-facb-440a-a38a-d5f20abe4c73

#### [Ls_ViewportCameraGeoSync.hipnc](./Ls_ViewportCameraGeoSync.hipnc)
Showing how deceptive the viewport can be when working with fast-moving cameras - the capy and camera are in sync when hitting play, but when scrubbing the timeline he's all over the shop:

https://github.com/user-attachments/assets/18be003d-dcb7-4d79-834d-a9c52088a267

#### [Ls_ViewportText_v01.hip](./Ls_ViewportText_v01.hip)
Using tag visualizers in dummy geo objects parented under the camera. This allows color control, and is easy to move around rather than being stuck in the corner.

<img width="1917" height="916" alt="Ls_ViewportText_v01" src="https://github.com/user-attachments/assets/95f28272-254b-4536-8f5f-df1d04f544d9" />

&nbsp;
&nbsp;

Everything else in here I have zero memory of don't @ me 🤍 lewis.saunders@gmail.com

(Older stuff might be on https://lewisinthelandofmachines.tumblr.com)
