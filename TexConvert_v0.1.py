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

# alShader codes
ALSURFACE_NODE = 815861509


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

def main():
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

    # connect shaders

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
