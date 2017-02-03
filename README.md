# TexConvert
## A Texture converter for VRay and C4DtoA - alSurface
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
- Simply import the script into C4D's script manager  
- Select the material you wish to convert  
- Click execute and bam! it should have converted it. *There are some limitations being worked on*  

---

## Current Limitations
- Not all features of the VRay material can translate across *yet...*  
- Only tested using a VRayAdvancedMaterial  
- No support for textures inside filters, c4d noises or builtin elements such as checkerboard.  
- Will convert multiple VRay materials at a time **Unknown upper limit**  

---

## What does convert:
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
- **SSS Layer**  

  *This is more of a template transfer to get your texture map / colours across.  
  Refinement will be needed on the radius / depth and weightings*
  - Scale  
  - Overall Colour (*colour 1 in AlSurface*)  
  - Overall Colour Texture Map (if present)  
  - Sub Surface Colour (*colour 2 in AlSurface*)  
  - Sub Surface Colour Texture Map (if present)  
  - Scatter Colour (*colour 3 in AlSurface*)  
  - Scatter Colour Texture Map (if present)  


---
