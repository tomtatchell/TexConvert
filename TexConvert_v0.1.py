import c4d

# from api/util/Constants.h
C4DTOA_MSG_TYPE = 1000
C4DTOA_MSG_PARAM1 = 2001
C4DTOA_MSG_PARAM2 = 2002
C4DTOA_MSG_PARAM3 = 2003
C4DTOA_MSG_PARAM4 = 2004
C4DTOA_MSG_RESP1 = 2011
C4DTOA_MSG_ADD_SHADER = 1029
C4DTOA_MSG_ADD_CONNECTION = 1031
C4DTOA_MSG_CONNECT_ROOT_SHADER = 1033

# from c4dtoa_symbols.h
ARNOLD_SHADER_NETWORK = 1033991
ARNOLD_SHADER_GV = 1033990
ARNOLD_C4D_SHADER_GV = 1034190
ARNOLD_REFERENCE_GV = 1035541

# from api/util/ArnolShaderNetworkUtil.h
ARNOLD_BEAUTY_PORT_ID = 537905099
ARNOLD_DISPLACEMENT_PORT_ID = 537905100

# from api/util/NodeIds.h
C4DAIN_STANDARD = 1760354454
C4DAIN_NOISE = 268710787

# from res/description/ainode_standard.h
C4DAIP_STANDARD_KD_COLOR = 338192719
C4DAIP_STANDARD_KS = 1284763298
C4DAIP_STANDARD_KS_COLOR = 1853957632

# from res/description/ainode_noise.h
C4DAIP_NOISE_OCTAVES = 35478650
C4DAIP_NOISE_DISTORTION = 1840107712

# alShader nodes
ALSURFACE_NODE = 815861509

# from res/description/ainode_alSurface.h
C4DAIP_ALSURFACE_DIFFUSESTRENGTH = 1212163586
C4DAIP_ALSURFACE_DIFFUSECOLOR = 1076269102
C4DAIP_ALSURFACE_DIFFUSEROUGHNESS = 1994027635
C4DAIP_ALSURFACE_OPACITY = 234584834

# from res/description/ainode_image.h
C4DAIP_IMAGE_FILENAME = 1737748425




def CreateArnoldShader(material, nodeId, posx, posy):
    msg = c4d.BaseContainer()
    msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_ADD_SHADER)
    msg.SetInt32(C4DTOA_MSG_PARAM1, ARNOLD_SHADER_GV)
    msg.SetInt32(C4DTOA_MSG_PARAM2, nodeId)
    msg.SetInt32(C4DTOA_MSG_PARAM3, posx)
    msg.SetInt32(C4DTOA_MSG_PARAM4, posy)
    material.Message(c4d.MSG_BASECONTAINER, msg)
    return msg.GetLink(C4DTOA_MSG_RESP1)

def CreateC4DShader(material, nodeId, posx, posy):
    msg = c4d.BaseContainer()
    msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_ADD_SHADER)
    msg.SetInt32(C4DTOA_MSG_PARAM1, ARNOLD_C4D_SHADER_GV)
    msg.SetInt32(C4DTOA_MSG_PARAM2, nodeId)
    msg.SetInt32(C4DTOA_MSG_PARAM3, posx)
    msg.SetInt32(C4DTOA_MSG_PARAM4, posy)
    material.Message(c4d.MSG_BASECONTAINER, msg)
    return msg.GetLink(C4DTOA_MSG_RESP1)

def CreateReference(material, ref, posx, posy):
    msg = c4d.BaseContainer()
    msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_ADD_SHADER)
    msg.SetInt32(C4DTOA_MSG_PARAM1, ARNOLD_REFERENCE_GV)
    msg.SetLink(C4DTOA_MSG_PARAM2, ref)
    msg.SetInt32(C4DTOA_MSG_PARAM3, posx)
    msg.SetInt32(C4DTOA_MSG_PARAM4, posy)
    material.Message(c4d.MSG_BASECONTAINER, msg)
    return msg.GetLink(C4DTOA_MSG_RESP1)

def AddConnection(material, srcNode, dstNode, dstPortId):
    msg = c4d.BaseContainer()
    msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_ADD_CONNECTION)
    msg.SetLink(C4DTOA_MSG_PARAM1, srcNode)
    msg.SetInt32(C4DTOA_MSG_PARAM2, 0)
    msg.SetLink(C4DTOA_MSG_PARAM3, dstNode)
    msg.SetInt32(C4DTOA_MSG_PARAM4, dstPortId)
    material.Message(c4d.MSG_BASECONTAINER, msg)
    return msg.GetBool(C4DTOA_MSG_RESP1)

def SetRootShader(material, shader, rootPortId):
    msg = c4d.BaseContainer()
    msg.SetInt32(C4DTOA_MSG_TYPE, C4DTOA_MSG_CONNECT_ROOT_SHADER)
    msg.SetLink(C4DTOA_MSG_PARAM1, shader)
    msg.SetInt32(C4DTOA_MSG_PARAM2, 0)
    msg.SetInt32(C4DTOA_MSG_PARAM3, rootPortId)
    material.Message(c4d.MSG_BASECONTAINER, msg)
    return msg.GetBool(C4DTOA_MSG_RESP1)

doc = c4d.documents.GetActiveDocument()
mat = doc.GetActiveMaterial()

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
    'DC_TexMapPath' : None, # string
    'DLT_Colour' : mat[c4d.VRAYMATERIAL_COLOR1_TRANSP], # c4d Vector
    'DLT_Amount' : mat[c4d.VRAYMATERIAL_COLOR1_TRANSP_MULT], # float
    'DLT_TextureMap' : mat[c4d.VRAYMATERIAL_COLOR1_TRANSPSHADER], # c4d.BaseShader object
    'DLT_TexMapPath' : None,
    'DO_Roughness' : mat[c4d.VRAYMATERIAL_COLOR1_ROUGHNESS], # float
    'DO_TextureMap' : mat[c4d.VRAYMATERIAL_COLOR1_ROUGHNESSTEX],  # c4d.BaseShader object
    'DO_TexMapPath' : None
    }
    if Diffuse_01['DC_TextureMap'] != None:
        Diffuse_01['DC_TexMapPath'] = mat[c4d.VRAYMATERIAL_COLOR1_SHADER][c4d.BITMAPSHADER_FILENAME]
    if Diffuse_01['DLT_TextureMap'] != None:
        Diffuse_01['DLT_TexMapPath'] = mat[c4d.VRAYMATERIAL_COLOR1_TRANSPSHADER][c4d.BITMAPSHADER_FILENAME]
    if Diffuse_01['DO_TextureMap'] != None:
        Diffuse_01['DO_TexMapPath'] = mat[c4d.VRAYMATERIAL_COLOR1_ROUGHNESSTEX][c4d.BITMAPSHADER_FILENAME]

    return Diffuse_01

def SetDiffuse_01(mat, alSurface, VD01, Layers):
    if 'Diffuse_01' in Layers:
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_DIFFUSECOLOR, VD01['DC_Colour'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_DIFFUSESTRENGTH, VD01['DC_Brightness'])
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_OPACITY, VD01['DLT_Colour'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_DIFFUSEROUGHNESS, VD01['DO_Roughness'])

        # create bitmaps / images
        if VD01['DC_TextureMap'] and VD01['DC_TextureMap'].GetType() == c4d.Xbitmap:
            DCBitmap = CreateC4DShader(mat, c4d.Xbitmap, -150, 150)
            if DCBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            DCBitmap.SetName("Diffuse Colour Bitmap")
            DCBitmapShader = DCBitmap.GetFirstShader()
            DCBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VD01['DC_TexMapPath'])
            AddConnection(mat, DCBitmap, alSurface, C4DAIP_ALSURFACE_DIFFUSECOLOR)

        if VD01['DLT_TextureMap'] and VD01['DLT_TextureMap'].GetType() == c4d.Xbitmap:
            DLTBitmap = CreateC4DShader(mat, c4d.Xbitmap, -150, 100)
            if DLTBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            DLTBitmap.SetName("Diffuse Layer Transparency Bitmap")
            DLTBitmapShader = DLTBitmap.GetFirstShader()
            DLTBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VD01['DLT_TexMapPath'])
            AddConnection(mat, DLTBitmap, alSurface, C4DAIP_ALSURFACE_OPACITY)

        if VD01['DO_TextureMap'] and VD01['DO_TextureMap'].GetType() == c4d.Xbitmap:
            DOBitmap = CreateC4DShader(mat, c4d.Xbitmap, -150, 50)
            if DOBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            DOBitmap.SetName("Diffuse Options Roughness Bitmap")
            DOBitmapShader = DOBitmap.GetFirstShader()
            DOBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VD01['DO_TexMapPath'])
            AddConnection(mat, DOBitmap, alSurface, C4DAIP_ALSURFACE_DIFFUSEROUGHNESS)
    else:
         alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_DIFFUSESTRENGTH, 0.0)


def GetSpecular_01():
    Specular_01 = {
    'SC_Colour' : mat[c4d.VRAYMATERIAL_SPECULAR1_COLOR], # c4d Vector
    'SC_Brightness' : mat[c4d.VRAYMATERIAL_SPECULAR1_COLOR_MULT], # float
    'SC_TextureMap' : mat[c4d.VRAYMATERIAL_SPECULAR1_SHADER], # c4d.BaseShader object
    'SC_TexMapPath' : None,
    'SLT_IOR' : mat[c4d.VRAYMATERIAL_SPECULAR1_FRESNELIOR1], # float
    'SLP_RefGloss' : mat[c4d.VRAYMATERIAL_SPECULAR1_REFLECTIONGLOSS], # float
    'SLP_TextureMap' : mat[c4d.VRAYMATERIAL_SPECULAR1_REFLECTIONGLOSSSHADER], # c4d.BaseShader object
    'SLP_TexMapPath' : None
    }
    if Specular_01['SC_TextureMap'] != None:
        Specular_01['SC_TexMapPath'] = mat[c4d.VRAYMATERIAL_SPECULAR1_SHADER][c4d.BITMAPSHADER_FILENAME]
    if Specular_01['SLP_TextureMap'] != None:
        Specular_01['SLP_TexMapPath'] = mat[c4d.VRAYMATERIAL_SPECULAR1_REFLECTIONGLOSSSHADER][c4d.BITMAPSHADER_FILENAME]

def SetSpecular_01():
def main():
    doc = c4d.documents.GetActiveDocument()
    activemat = doc.GetActiveMaterial()
    Layers = ActiveLayers(activemat)

    VD01 = GetDiffuse_01()
    VS01 = GetSpecular_01()

    # create material
    mat = c4d.BaseMaterial(ARNOLD_SHADER_NETWORK)
    if mat is None:
        raise Exception("Failed to create material")
    mat.SetName("mat01")
    doc.InsertMaterial(mat)

    # create shaders
    alSurface = CreateArnoldShader(mat, ALSURFACE_NODE, 150, 100)
    if alSurface is None:
        raise Exception("Failed to create alSurface shader")




    # set shader parameters
    alSurface.SetName("VRay to A")



    SetDiffuse_01(mat, alSurface, VD01, Layers)




    # connect shaders
    SetRootShader(mat, alSurface, ARNOLD_BEAUTY_PORT_ID)
    #if VD01['DC_TextureMap'] != None:
        #AddConnection(mat, bitmap, alSurface, C4DAIP_ALSURFACE_DIFFUSECOLOR)


    """
    # create shaders
    standard = CreateArnoldShader(mat, C4DAIN_STANDARD, 150, 100)
    if standard is None:
        raise Exception("Failed to create standard shader")
    noise = CreateArnoldShader(mat, C4DAIN_NOISE, 0, 50)
    if noise is None:
        raise Exception("Failed to create noise shader")
    bitmap = CreateC4DShader(mat, c4d.Xbitmap, 0, 150)
    if bitmap is None:
        raise Exception("Failed to create Bitmap shader")

    # set shader parameters
    standard.SetName("mystandard")
    standard.GetOpContainerInstance().SetVector(C4DAIP_STANDARD_KS_COLOR, c4d.Vector(0.9, 0.9, 0.4))
    standard.GetOpContainerInstance().SetFloat(C4DAIP_STANDARD_KS, 0.2)
    noise.SetName("mynoise")
    noise.GetOpContainerInstance().SetInt32(C4DAIP_NOISE_OCTAVES, 3)
    noise.GetOpContainerInstance().SetFloat(C4DAIP_NOISE_DISTORTION, 3.42)

    # connect shaders
    SetRootShader(mat, standard, ARNOLD_BEAUTY_PORT_ID)
    AddConnection(mat, noise, standard, C4DAIP_STANDARD_KD_COLOR)
    """

    # redraw
    c4d.EventAdd(c4d.EVENT_FORCEREDRAW)

if __name__=='__main__':
    main()
