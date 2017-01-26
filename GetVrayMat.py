import c4d
from c4d import gui

doc = c4d.documents.GetActiveDocument()
mat = doc.GetActiveMaterial()

MatLayers = {
'MatMatte' : 0,
'MatWeight' : 0,
'Bump' : 0,
'Luminosity' : 0,
'Flakes' : 0,
'Spec_05' : 0,
'Spec_04' : 0,
'Spec_03' : 0,
'Spec_02' : 0,
'Spec_01' : 0,
'Diffuse_01' : 0,
'Diffuse_02' : 0,
'Refraction' : 0,
'SSS' : 0
}


def MatType():
    """
    Returns the type of the currently active material.
    """
    if mat == None:
        pass
    elif 'VRay' in str(mat):
        return "VRay"
    elif 'Arnold' in str(mat):
        return "Arnold"
    else:
        return "Standard"



def ActiveLayers(mat):
    """
    mat: c4d.BaseMaterial, the current active material of the scene
    returns: List of active layers within the material.
    """
    activeLayers = []
    if MatType() == "VRay":
        if mat[c4d.VRAYMATERIAL_USE_MATTE]:
            MatLayers['MatMatte'] = 1
        if mat[c4d.VRAYMATERIAL_USE_TRANSP]:
            MatLayers['MatWeight'] = 1
        if mat[c4d.VRAYMATERIAL_USE_MATTE]:
            MatLayers['MatMatte'] = 1
        if mat[c4d.VRAYMATERIAL_USE_BUMP]:
            MatLayers['Bump'] = 1
        if mat[c4d.VRAYMATERIAL_USE_LUMINANCE]:
            MatLayers['Luminosity'] = 1
        if mat[c4d.VRAYMATERIAL_USE_FLAKES]:
            MatLayers['Flakes'] = 1
        if mat[c4d.VRAYMATERIAL_USE_SPECULAR5]:
            MatLayers['Spec_05'] = 1
        if mat[c4d.VRAYMATERIAL_USE_SPECULAR4]:
            MatLayers['Spec_04'] = 1
        if mat[c4d.VRAYMATERIAL_USE_SPECULAR3]:
            MatLayers['Spec_03'] = 1
        if mat[c4d.VRAYMATERIAL_USE_SPECULAR2]:
            MatLayers['Spec_02'] = 1
        if mat[c4d.VRAYMATERIAL_USE_SPECULAR1]:
            MatLayers['Spec_01'] = 1
        if mat[c4d.VRAYMATERIAL_USE_COLOR1]:
            MatLayers['Diffuse_01'] = 1
        if mat[c4d.VRAYMATERIAL_USE_COLOR2]:
            MatLayers['Diffuse_02'] = 1
        if mat[c4d.VRAYMATERIAL_USE_TRANSPARENCY]:
            MatLayers['Refraction'] = 1
        if mat[c4d.VRAYMATERIAL_USE_SSS]:
            MatLayers['SSS'] = 1

    for x in MatLayers:
        if MatLayers[x]:
            activeLayers.append(x)

    return activeLayers

    if MatType() != "VRay":
        c4d.gui.MessageDialog("Please select a VRay Material")




def GetDiffuse_01():
    Diffuse_01 = {
    'DC_Colour' : mat[c4d.VRAYMATERIAL_COLOR1_COLOR], # c4d Vector
    'DC_Brightness' : mat[c4d.VRAYMATERIAL_COLOR1_MULT], # float
    'DC_TextureMap' : mat[c4d.VRAYMATERIAL_COLOR1_SHADER], # c4d.BaseShader object
    'DC_TexMapPath' : None # string
    }
    if Diffuse_01['DC_TextureMap'] != None:
        Diffuse_01['DC_TexMapPath'] = mat[c4d.VRAYMATERIAL_COLOR1_SHADER][c4d.BITMAPSHADER_FILENAME]

    return Diffuse_01


def main():
    if 'Diffuse_01' in ActiveLayers(mat):
        VrayD01 = GetDiffuse_01()



if __name__=='__main__':
    main()
