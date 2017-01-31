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
C4DAIN_BUMP2D = 184848913

# from res/description/ainode_standard.h
C4DAIP_STANDARD_KD_COLOR = 338192719
C4DAIP_STANDARD_KS = 1284763298
C4DAIP_STANDARD_KS_COLOR = 1853957632

# from res/description/ainode_noise.h
C4DAIP_NOISE_OCTAVES = 35478650
C4DAIP_NOISE_DISTORTION = 1840107712

# from res/description/ainode_bump2d.h
C4DAIP_BUMP2D_BUMP_MAP = 1722542866
C4DAIP_BUMP2D_BUMP_HEIGHT = 149592681
C4DAIP_BUMP2D_SHADER = 1367502316

# alShader nodes
ALSURFACE_NODE = 815861509

# from res/description/ainode_alSurface.h
C4DAIP_ALSURFACE_DIFFUSESTRENGTH = 1212163586
C4DAIP_ALSURFACE_DIFFUSECOLOR = 1076269102
C4DAIP_ALSURFACE_DIFFUSEROUGHNESS = 1994027635

C4DAIP_ALSURFACE_OPACITY = 234584834

C4DAIP_ALSURFACE_SPECULAR1STRENGTH = 959965816
C4DAIP_ALSURFACE_SPECULAR1COLOR = 1968924664
C4DAIP_ALSURFACE_SPECULAR1IOR = 1098234115
C4DAIP_ALSURFACE_SPECULAR1ROUGHNESS = 2033531479
C4DAIP_ALSURFACE_SPECULAR1ANISOTROPY = 2145841423
C4DAIP_ALSURFACE_SPECULAR1ROTATION = 1577603657

C4DAIP_ALSURFACE_SPECULAR2STRENGTH = 994346633
C4DAIP_ALSURFACE_SPECULAR2COLOR = 2008060057
C4DAIP_ALSURFACE_SPECULAR2IOR = 1098270052
C4DAIP_ALSURFACE_SPECULAR2ROUGHNESS = 2101332856
C4DAIP_ALSURFACE_SPECULAR2ANISOTROPY = 91604018
C4DAIP_ALSURFACE_SPECULAR2ROTATION = 763051190

C4DAIP_ALSURFACE_TRANSMISSIONSTRENGTH = 1356953022
C4DAIP_ALSURFACE_TRANSMISSIONCOLOR = 84572430
C4DAIP_ALSURFACE_TRANSMISSIONROUGHNESS = 1817855569
C4DAIP_ALSURFACE_TRANSMISSIONIOR = 769142403
C4DAIP_ALSURFACE_TRANSMISSIONLINKTOSPECULAR1 = 1303558196

C4DAIP_ALSURFACE_EMISSIONSTRENGTH = 533840799
C4DAIP_ALSURFACE_EMISSIONCOLOR = 1546843503

C4DAIP_ALSURFACE_SSSMIX = 1599486640
C4DAIP_ALSURFACE_SSSDENSITYSCALE = 1920019850
C4DAIP_ALSURFACE_SSSRADIUS = 1389648490
C4DAIP_ALSURFACE_SSSWEIGHT1 = 938517691
C4DAIP_ALSURFACE_SSSRADIUSCOLOR = 601525929
C4DAIP_ALSURFACE_SSSRADIUS2 = 1386240036
C4DAIP_ALSURFACE_SSSWEIGHT2 = 938517692
C4DAIP_ALSURFACE_SSSRADIUSCOLOR2 = 1624480773
C4DAIP_ALSURFACE_SSSRADIUS3 = 1386240035
C4DAIP_ALSURFACE_SSSWEIGHT3 = 938517693
C4DAIP_ALSURFACE_SSSRADIUSCOLOR3 = 1624480772

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


def rangeMap(curValue, curMax, curMin, newMax, newMin):
    curRange = (curMax - curMin)
    if (curRange == 0): return 0
    else:
        newRange = (newMax - newMin)
        newVal = (((curValue - curMin) * newRange) / curRange) + newMin
        return newVal


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
    'SLP_TexMapPath' : None,
    'SLA_Anisotropy' : mat[c4d.VRAYMATERIAL_SPECULAR1_ANISOTROPY], # float
    'SLA_AniRot' : mat[c4d.VRAYMATERIAL_SPECULAR1_ANISOTROPYROT], # float
    }
    if Specular_01['SC_TextureMap'] != None:
        Specular_01['SC_TexMapPath'] = mat[c4d.VRAYMATERIAL_SPECULAR1_SHADER][c4d.BITMAPSHADER_FILENAME]
    if Specular_01['SLP_TextureMap'] != None:
        Specular_01['SLP_TexMapPath'] = mat[c4d.VRAYMATERIAL_SPECULAR1_REFLECTIONGLOSSSHADER][c4d.BITMAPSHADER_FILENAME]
    return Specular_01


def SetSpecular_01(mat, alSurface, VS01, Layers):
    if 'Spec_01' in Layers:
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_SPECULAR1COLOR, VS01['SC_Colour'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR1STRENGTH, VS01['SC_Brightness'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR1IOR, VS01['SLT_IOR'])

        VtoA_roughness = 1.0 - VS01['SLP_RefGloss']  # convert vray 0-1 value to c4dtoa 1-0 value
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR1ROUGHNESS, VtoA_roughness)

        VtoA_ani = ((VS01['SLA_Anisotropy'] + 1) / 2)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR1ANISOTROPY, VtoA_ani)

        VtoA_aniRot = rangeMap(VS01['SLA_AniRot'], 6.28318530718, 0, 1, 0)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR1ROTATION, VtoA_aniRot)

        # create bitmaps / images
        if VS01['SC_TextureMap'] and VS01['SC_TextureMap'].GetType() == c4d.Xbitmap:
            SCBitmap = CreateC4DShader(mat, c4d.Xbitmap, -250, 150)
            if SCBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            SCBitmap.SetName("Specular Colour Bitmap")
            SCBitmapShader = SCBitmap.GetFirstShader()
            SCBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VS01['SC_TexMapPath'])
            AddConnection(mat, SCBitmap, alSurface, C4DAIP_ALSURFACE_SPECULAR1COLOR)

        if VS01['SLP_TextureMap'] and VS01['SLP_TextureMap'].GetType() == c4d.Xbitmap:
            SLPBitmap = CreateC4DShader(mat, c4d.Xbitmap, -250, 100)
            if SLPBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            SLPBitmap.SetName("Specular Roughness Bitmap")
            SLPBitmapShader = SLPBitmap.GetFirstShader()
            SLPBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VS01['SLP_TexMapPath'])
            AddConnection(mat, SLPBitmap, alSurface, C4DAIP_ALSURFACE_SPECULAR1ROUGHNESS)
    else:
         alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR1STRENGTH, 0.0)


def GetSpecular_02():
    Specular_02 = {
    'SC_Colour' : mat[c4d.VRAYMATERIAL_SPECULAR2_COLOR], # c4d Vector
    'SC_Brightness' : mat[c4d.VRAYMATERIAL_SPECULAR2_COLOR_MULT], # float
    'SC_TextureMap' : mat[c4d.VRAYMATERIAL_SPECULAR2_SHADER], # c4d.BaseShader object
    'SC_TexMapPath' : None,
    'SLT_IOR' : mat[c4d.VRAYMATERIAL_SPECULAR2_FRESNELIOR1], # float
    'SLP_RefGloss' : mat[c4d.VRAYMATERIAL_SPECULAR2_REFLECTIONGLOSS], # float
    'SLP_TextureMap' : mat[c4d.VRAYMATERIAL_SPECULAR2_REFLECTIONGLOSSSHADER], # c4d.BaseShader object
    'SLP_TexMapPath' : None,
    'SLA_Anisotropy' : mat[c4d.VRAYMATERIAL_SPECULAR2_ANISOTROPY], # float
    'SLA_AniRot' : mat[c4d.VRAYMATERIAL_SPECULAR2_ANISOTROPYROT], # float
    }
    if Specular_02['SC_TextureMap'] != None:
        Specular_02['SC_TexMapPath'] = mat[c4d.VRAYMATERIAL_SPECULAR2_SHADER][c4d.BITMAPSHADER_FILENAME]
    if Specular_02['SLP_TextureMap'] != None:
        Specular_02['SLP_TexMapPath'] = mat[c4d.VRAYMATERIAL_SPECULAR2_REFLECTIONGLOSSSHADER][c4d.BITMAPSHADER_FILENAME]
    return Specular_02


def SetSpecular_02(mat, alSurface, VS02, Layers):
    if 'Spec_02' in Layers:
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_SPECULAR2COLOR, VS02['SC_Colour'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR2STRENGTH, VS02['SC_Brightness'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR2IOR, VS02['SLT_IOR'])

        VtoA_roughness = 1.0 - VS02['SLP_RefGloss']  # convert vray 0-1 value to c4dtoa 1-0 value
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR2ROUGHNESS, VtoA_roughness)

        VtoA_ani = ((VS02['SLA_Anisotropy'] + 1) / 2)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR2ANISOTROPY, VtoA_ani)

        VtoA_aniRot = rangeMap(VS02['SLA_AniRot'], 6.28318530718, 0, 1, 0)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR2ROTATION, VtoA_aniRot)

        # create bitmaps / images
        if VS02['SC_TextureMap'] and VS02['SC_TextureMap'].GetType() == c4d.Xbitmap:
            SCBitmap = CreateC4DShader(mat, c4d.Xbitmap, -250, 150)
            if SCBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            SCBitmap.SetName("Specular Colour Bitmap")
            SCBitmapShader = SCBitmap.GetFirstShader()
            SCBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VS02['SC_TexMapPath'])
            AddConnection(mat, SCBitmap, alSurface, C4DAIP_ALSURFACE_SPECULAR2COLOR)

        if VS02['SLP_TextureMap'] and VS02['SLP_TextureMap'].GetType() == c4d.Xbitmap:
            SLPBitmap = CreateC4DShader(mat, c4d.Xbitmap, -250, 100)
            if SLPBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            SLPBitmap.SetName("Specular Roughness Bitmap")
            SLPBitmapShader = SLPBitmap.GetFirstShader()
            SLPBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VS02['SLP_TexMapPath'])
            AddConnection(mat, SLPBitmap, alSurface, C4DAIP_ALSURFACE_SPECULAR2ROUGHNESS)
    else:
         alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SPECULAR2STRENGTH, 0.0)


def GetTransmission():
    transmission = {
    'RC_Colour' : mat[c4d.VRAYMATERIAL_TRANSPARENCY_COLOR], # c4d Vector
    'RC_Brightness' : mat[c4d.VRAYMATERIAL_TRANSPARENCY_COLOR_MULT], # float
    'RC_TextureMap' : mat[c4d.VRAYMATERIAL_TRANSPARENCY_SHADER], # c4d.BaseShader object
    'RC_TexMapPath' : None,
    'RLP_IOR' : mat[c4d.VRAYMATERIAL_TRANSPARENCY_IOR], # float
    'RLP_Gloss' : mat[c4d.VRAYMATERIAL_TRANSPARENCY_GLOSSINESS], # float
    'RLP_TextureMap' : mat[c4d.VRAYMATERIAL_TRANSPARENCY_GLOSSINESSSHADER], # c4d.BaseShader object
    'RLP_TexMapPath' : None,
    }
    if transmission['RC_TextureMap'] != None:
        transmission['RC_TexMapPath'] = mat[c4d.VRAYMATERIAL_TRANSPARENCY_SHADER][c4d.BITMAPSHADER_FILENAME]
    if transmission['RLP_TextureMap'] != None:
        transmission['RLP_TexMapPath'] = mat[c4d.VRAYMATERIAL_TRANSPARENCY_GLOSSINESSSHADER][c4d.BITMAPSHADER_FILENAME]
    return transmission


def SetTransmission(mat, alSurface, VT, Layers):
    if 'Refraction' in Layers:
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_TRANSMISSIONCOLOR, VT['RC_Colour'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_TRANSMISSIONSTRENGTH, VT['RC_Brightness'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_TRANSMISSIONIOR, VT['RLP_IOR'])

        VtoA_roughness = 1.0 - VT['RLP_Gloss']  # convert vray 0-1 value to c4dtoa 1-0 value
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_TRANSMISSIONROUGHNESS, VtoA_roughness)

        # create bitmaps / images
        if VT['RC_TextureMap'] and VT['RC_TextureMap'].GetType() == c4d.Xbitmap:
            RCBitmap = CreateC4DShader(mat, c4d.Xbitmap, -250, 150)
            if RCBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            RCBitmap.SetName("Transmission Colour Bitmap")
            RCBitmapShader = RCBitmap.GetFirstShader()
            RCBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VT['RC_TexMapPath'])
            AddConnection(mat, RCBitmap, alSurface, C4DAIP_ALSURFACE_TRANSMISSIONCOLOR)

        if VT['RLP_TextureMap'] and VT['RLP_TextureMap'].GetType() == c4d.Xbitmap:
            RLPBitmap = CreateC4DShader(mat, c4d.Xbitmap, -250, 100)
            if RLPBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            RLPBitmap.SetName("Transmission Roughness Bitmap")
            RLPBitmapShader = SLPBitmap.GetFirstShader()
            RLPBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VT['RLP_TexMapPath'])
            AddConnection(mat, RLPBitmap, alSurface, C4DAIP_ALSURFACE_TRANSMISSIONROUGHNESS)

        if 'Spec_01' in Layers:
            alSurface.GetOpContainerInstance().SetInt32(C4DAIP_ALSURFACE_TRANSMISSIONLINKTOSPECULAR1, 1)
        elif 'Spec_01' not in Layers:
            alSurface.GetOpContainerInstance().SetInt32(C4DAIP_ALSURFACE_TRANSMISSIONLINKTOSPECULAR1, 0)
    else:
         alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_TRANSMISSIONSTRENGTH, 0.0)


def GetEmission():
        emission = {
        'LC_Colour' : mat[c4d.VRAYMATERIAL_LUMINANCE_COLOR], # c4d Vector
        'LC_Amount' : mat[c4d.VRAYMATERIAL_LUMINANCE_COLOR_MULT], # float
        'LC_TextureMap' : mat[c4d.VRAYMATERIAL_LUMINANCE_SHADER], # c4d.BaseShader object
        'LC_TexMapPath' : None,
        }
        if emission['LC_TextureMap'] != None:
            emission['LC_TexMapPath'] = mat[c4d.VRAYMATERIAL_LUMINANCE_SHADER][c4d.BITMAPSHADER_FILENAME]
        return emission


def SetEmission(mat, alSurface, VE, Layers):
    if 'Luminosity' in Layers:
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_EMISSIONCOLOR, VE['LC_Colour'])
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_EMISSIONSTRENGTH, VE['LC_Amount'])

        # create bitmaps / images
        if VE['LC_TextureMap'] and VE['LC_TextureMap'].GetType() == c4d.Xbitmap:
            LCBitmap = CreateC4DShader(mat, c4d.Xbitmap, -250, 150)
            if LCBitmap is None:
                raise Exception("Failed to create Bitmap shader")
            LCBitmap.SetName("Transmission Colour Bitmap")
            LCBitmapShader = LCBitmap.GetFirstShader()
            LCBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VE['LC_TexMapPath'])
            AddConnection(mat, LCBitmap, alSurface, C4DAIP_ALSURFACE_EMISSIONCOLOR)
    else:
         alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_EMISSIONSTRENGTH, 0.0)


def GetBump():
    bump = {
    'BTextureMap' : mat[c4d.VRAYMATERIAL_BUMP_SHADER], # c4d.BaseShader object
    'BTexMapPath' : None,
    'BAmount' : mat[c4d.VRAYMATERIAL_BUMP_BUMPTEXMULT] # float
    }
    if bump['BTextureMap'] != None:
        bump['BTexMapPath'] = mat[c4d.VRAYMATERIAL_BUMP_SHADER][c4d.BITMAPSHADER_FILENAME]
    return bump


def SetBump(mat, alSurface, VB, Layers):
    if 'Bump' in Layers:
        VBump = CreateArnoldShader(mat, C4DAIN_BUMP2D, 400, 100)
        if VBump is None:
            raise Exception("Failed to create bump2d node")
        VBump.SetName("VtoA_Bump2D")
        VBump.GetOpContainerInstance().SetFloat(C4DAIP_BUMP2D_BUMP_HEIGHT, VB['BAmount'])

        # create bitmaps / images
        if VB['BTextureMap'] and VB['BTextureMap'].GetType() == c4d.Xbitmap:
            VBBitmap = CreateC4DShader(mat, c4d.Xbitmap, 0, 0)
            if VBBitmap is None:
                raise Exception("Failed to create bitmap shader")
            VBBitmap.SetName("VtaA Bump Bitmap shader")
            VBBitmapShader = VBBitmap.GetFirstShader()
            VBBitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VB['BTexMapPath'])
            AddConnection(mat, VBBitmap, VBump, C4DAIP_BUMP2D_BUMP_MAP)

        AddConnection(mat, alSurface, VBump, C4DAIP_BUMP2D_SHADER)
        SetRootShader(mat, VBump, ARNOLD_BEAUTY_PORT_ID)


def GetSSS():
    sss = {
        'GP_Scale' : mat[c4d.VRAYMATERIAL_SSS_SCALE], # float
        'GP_MaxDistance' : mat[c4d.VRAYMATERIAL_SSS_MAXDISTANCE], # float
        'SP_C1' : mat[c4d.VRAYMATERIAL_SSS_OVERALLCOLOR],
        'SP_C1_TexMap' : mat[c4d.VRAYMATERIAL_SSS_OVERALLCOLORSHADER],
        'SP_C1_TexPath' : None,
        'SP_C2' : mat[c4d.VRAYMATERIAL_SSS_SSSCOLOR],
        'SP_C2_TexMap' : mat[c4d.VRAYMATERIAL_SSS_SSSCOLORSHADER],
        'SP_C2_TexPath' : None,
        'SP_C3' : mat[c4d.VRAYMATERIAL_SSS_SCATTERCOLOR],
        'SP_C3_TexMap' : mat[c4d.VRAYMATERIAL_SSS_SCATTERSHADER],
        'SP_C3_TexPath' : None,
    }

    if sss['SP_C1_TexMap'] != None:
        sss['SP_C1_TexPath'] = mat[c4d.VRAYMATERIAL_SSS_OVERALLCOLORSHADER][c4d.BITMAPSHADER_FILENAME]
    if sss['SP_C2_TexMap'] != None:
        sss['SP_C2_TexPath'] = mat[c4d.VRAYMATERIAL_SSS_SSSCOLORSHADER][c4d.BITMAPSHADER_FILENAME]
    if sss['SP_C3_TexMap'] != None:
        sss['SP_C3_TexPath'] = mat[c4d.VRAYMATERIAL_SSS_SCATTERSHADER][c4d.BITMAPSHADER_FILENAME]
    return sss


def SetSSS(mat, alSurface, VSSS, Layers):
    if 'SSS' in Layers:
        diffuse = alSurface.GetOpContainerInstance().GetFloat(C4DAIP_ALSURFACE_DIFFUSESTRENGTH)
        if diffuse == 0:
            alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_DIFFUSESTRENGTH, 1)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSMIX, 1)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSDENSITYSCALE, VSSS['GP_Scale'])

        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSRADIUS, 1)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSWEIGHT1, 0.5)
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_SSSRADIUSCOLOR, VSSS['SP_C1'])

        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSRADIUS2, 2)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSWEIGHT2, 0.3)
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_SSSRADIUSCOLOR2, VSSS['SP_C2'])

        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSRADIUS3, 3)
        alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_SSSWEIGHT3, 0.2)
        alSurface.GetOpContainerInstance().SetVector(C4DAIP_ALSURFACE_SSSRADIUSCOLOR3, VSSS['SP_C3'])

        # create bitmaps / images
        if VSSS['SP_C1_TexMap'] and VSSS['SP_C1_TexMap'].GetType() == c4d.Xbitmap:
            C1Bitmap = CreateC4DShader(mat, c4d.Xbitmap, -150, 150)
            if C1Bitmap is None:
                raise Exception("Failed to create Bitmap shader")
            C1Bitmap.SetName("SSS Layer 1")
            C1BitmapShader = C1Bitmap.GetFirstShader()
            C1BitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VSSS['SP_C1_TexPath'])
            AddConnection(mat, C1Bitmap, alSurface, C4DAIP_ALSURFACE_SSSRADIUSCOLOR)
        if VSSS['SP_C2_TexMap'] and VSSS['SP_C2_TexMap'].GetType() == c4d.Xbitmap:
            C2Bitmap = CreateC4DShader(mat, c4d.Xbitmap, -150, 50)
            if C2Bitmap is None:
                raise Exception("Failed to create Bitmap shader")
            C2Bitmap.SetName("SSS Layer 2")
            C2BitmapShader = C2Bitmap.GetFirstShader()
            C2BitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VSSS['SP_C2_TexPath'])
            AddConnection(mat, C2Bitmap, alSurface, C4DAIP_ALSURFACE_SSSRADIUSCOLOR2)
        if VSSS['SP_C3_TexMap'] and VSSS['SP_C3_TexMap'].GetType() == c4d.Xbitmap:
            C3Bitmap = CreateC4DShader(mat, c4d.Xbitmap, -150, 0)
            if C3Bitmap is None:
                raise Exception("Failed to create Bitmap shader")
            C3Bitmap.SetName("SSS Layer 3")
            C3BitmapShader = C3Bitmap.GetFirstShader()
            C3BitmapShader.GetDataInstance().SetFilename(c4d.BITMAPSHADER_FILENAME, VSSS['SP_C3_TexPath'])
            AddConnection(mat, C3Bitmap, alSurface, C4DAIP_ALSURFACE_SSSRADIUSCOLOR3)

    else:
         alSurface.GetOpContainerInstance().SetFloat(C4DAIP_ALSURFACE_DIFFUSESTRENGTH, 0.0)

def main():
    doc = c4d.documents.GetActiveDocument()
    activemat = doc.GetActiveMaterial()
    Layers = ActiveLayers(activemat)

    VD01 = GetDiffuse_01()
    VS01 = GetSpecular_01()
    VS02 = GetSpecular_02()
    VT = GetTransmission()
    VE = GetEmission()
    VB = GetBump()
    VSSS = GetSSS()

    # create material
    mat = c4d.BaseMaterial(ARNOLD_SHADER_NETWORK)
    if mat is None:
        raise Exception("Failed to create material")
    mat.SetName("VtoAl01")
    doc.InsertMaterial(mat)

    # create shaders
    alSurface = CreateArnoldShader(mat, ALSURFACE_NODE, 150, 100)
    if alSurface is None:
        raise Exception("Failed to create alSurface shader")


    # set shader parameters
    alSurface.SetName("VtoAlSurface")
    SetDiffuse_01(mat, alSurface, VD01, Layers)
    SetSpecular_01(mat, alSurface, VS01, Layers)
    SetSpecular_02(mat, alSurface, VS02, Layers)
    SetTransmission(mat, alSurface, VT, Layers)
    SetEmission(mat, alSurface, VE, Layers)
    SetBump(mat, alSurface, VB, Layers)
    SetSSS(mat, alSurface, VSSS, Layers)

    # connect root shader
    if 'Bump' not in Layers:
        SetRootShader(mat, alSurface, ARNOLD_BEAUTY_PORT_ID)

    # redraw
    c4d.EventAdd(c4d.EVENT_FORCEREDRAW)


if __name__=='__main__':
    main()
