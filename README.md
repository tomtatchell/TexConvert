# TexConvert
## A Texture converter for VRay and C4DtoA - alSurface
---
  - Gets VRay material.  
  - Gets active material layers.  
  - Gets data from active layers.  
  - Stores active layer data.  
  - Create C4DtoA shader network.  
  - Create alShader node.  
  - Applies stored VRay data to alShader node, creating
  necessary nodes (eg. image, bitmap, noise, bump2d etc.)

---

## How to use
---
- Simply import the script (TexConver_v0.1.py) into C4D's script manager
- Select the material you wish to convert
- Click execute and bam! it should have converted it. *There are some limitations being worked on*

---

## Current Limitations
---
- Only supports 1 selected VRay material at a time
- Not all features of the VRay material can translate across *yet...*
- Only tested using a VRayAdvancedMaterial

---

## What does convert:
---
- **Bump**  
  - Texture Map  
  - Bump amount
- **Luminosity Layer**
  - Colour  
  - Amount  
  - Texture Map (if present)  
- **Specular Layer 2**  
  - Colour  
  - Brightness  
  - Texture Map (if present)  
  - Fresnel IOR  
  - Reflection Glossiness  
  - Reflection Glossiness Texture Map (if present)  
  - Anisotropy  
  - Anisotropy Texture Map (if preset)  
  - Anisotropy Rotation  
- **Specular Layer 2**  
  - Colour  
  - Brightness  
  - Texture Map (if present)  
  - Fresnel IOR  
  - Reflection Glossiness  
  - Reflection Glossiness Texture Map (if present)  
  - Anisotropy  
  - Anisotropy Texture Map (if preset)  
  - Anisotropy Rotation  
- **Diffuse Layer 1**  
  - Colour  
  - Brightness  
  - Texture Map (if present)
  - Transparency Colour  
  - Transparency Amount  
  - Transparency Texture Map (if present)  
  - Roughness  
  - Roughness Texture Map (if present)  
- **Refraction Layer**  
  - Colour  
  - Brightness  
  - Texture Map (if present)  
  - IOR
  - Glossiness  
  - Glossiness Texture Map (if present)  


---
