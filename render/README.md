This directory contains code that generates partial point clouds from ShapeNet models. To use it:
1. Install [Blender](https://blender.org/download/).
2. Create a model list. Each line of the model list should be in the format `[synset_id]/[model_id]`.
3. Run `blender -b -P render_depth.py [ShapeNet directory] [model list] [output directory] [num scans per model]` to render the depth images. The images will be stored in OpenEXR format.
```
 blender -b -P render_depth.py /home/zq/zq/git-space/pcn/render/test/obj /home/zq/zq/git-space/pcn/render/test/list.txt  /home/zq/zq/git-space/pcn/render/output_exr  10
```
```
blender -b -P render_depth.py /home/zq/zq/git-space/pcn/data/data_preprocess/chair_obj /home/zq/zq/git-space/pcn/data/data_preprocess/chair_obj/list.txt  /home/zq/zq/git-space/pcn/render/output_exr_1  3
```
4. Run `python3 process_exr.py [model list] [intrinsics file] [output directory] [num scans per model]` to convert the `.exr` files into 16 bit PNG depth images and point clouds in the model's coordinate frame.

```
 
 pip --no-cache-dir install OpenEXR
  python3 process_exr.py  /home/zq/zq/git-space/pcn/render/test/list.txt  /home/zq/zq/git-space/pcn/render/output_exr/intrinsics.txt /home/zq/zq/git-space/pcn/render/output_exr 10
```
