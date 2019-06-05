# -*- coding: utf-8 -*-
# DO NOT EDIT THIS FILE
# This file was automatically generated by Natron PyPlug exporter version 10.

# Hand-written code should be added in a separate file named Crok_kuwahara_GLExt.py
# See http://natron.readthedocs.org/en/master/devel/groups.html#adding-hand-written-code-callbacks-etc
# Note that Viewers are never exported

import NatronEngine
import sys

# Try to import the extensions file where callbacks and hand-written code should be located.
try:
    from Crok_kuwahara_GLExt import *
except ImportError:
    pass

def getPluginID():
    return "natron.community.plugins.Crok_kuwahara_GL"

def getLabel():
    return "Crok_kuwahara_GL"

def getVersion():
    return 1.1

def getIconPath():
    return "Crok_kuwahara_GL.png"

def getGrouping():
    return "Community/GLSL/Effect"

def getPluginDescription():
    return "Simulates anisotropic kuwahara filtering."

def createInstance(app,group):
    # Create all nodes in the group

    # Create the parameters of the group node the same way we did for all internal nodes
    lastNode = group
    lastNode.setColor(1, 0.2353, 0.2353)

    # Create the user parameters
    lastNode.Controls = lastNode.createPageParam("Controls", "Controls")
    param = lastNode.createStringParam("sep01", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep01 = param
    del param

    param = lastNode.createStringParam("sep02", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep02 = param
    del param

    param = lastNode.createSeparatorParam("SETUP", "Setup")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.SETUP = param
    del param

    param = lastNode.createStringParam("sep03", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep03 = param
    del param

    param = lastNode.createStringParam("sep04", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep04 = param
    del param

    param = lastNode.createIntParam("Shadertoy1_2paramValueInt0", "Radius : ")
    param.setMinimum(0, 0)
    param.setMaximum(100, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(100, 0)
    param.setDefaultValue(5, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Shadertoy1_2paramValueInt0 = param
    del param

    param = lastNode.createStringParam("sep05", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep05 = param
    del param

    param = lastNode.createStringParam("sep06", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep06 = param
    del param

    param = lastNode.createSeparatorParam("OPTIONS", "Options")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.OPTIONS = param
    del param

    param = lastNode.createStringParam("sep07", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep07 = param
    del param

    param = lastNode.createStringParam("sep08", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep08 = param
    del param

    param = lastNode.createBooleanParam("isPremult", "Source is premultiplied : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Source is premultiplied.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.isPremult = param
    del param

    param = lastNode.createStringParam("sep09", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep09 = param
    del param

    param = lastNode.createStringParam("sep10", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep10 = param
    del param

    param = lastNode.createSeparatorParam("MASK", "Mask")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.MASK = param
    del param

    param = lastNode.createStringParam("sep11", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep11 = param
    del param

    param = lastNode.createStringParam("sep12", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep12 = param
    del param

    param = lastNode.createBooleanParam("useMask", "Use mask : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Use mask input.")
    param.setAddNewLine(True)
    param.setAnimationEnabled(False)
    lastNode.useMask = param
    del param

    param = lastNode.createBooleanParam("invertMask", "Invert mask : ")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Invert mask input.")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.invertMask = param
    del param

    param = lastNode.createChoiceParam("channelChoice", "Channel : ")
    entries = [ ("Red", ""),
    ("Green", ""),
    ("Blue", ""),
    ("Alpha", "")]
    param.setOptions(entries)
    del entries
    param.setDefaultValue("Alpha")
    param.restoreDefaultValue()

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("Channel used as mask.")
    param.setAddNewLine(False)
    param.setAnimationEnabled(False)
    lastNode.channelChoice = param
    del param

    param = lastNode.createStringParam("sep13", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep13 = param
    del param

    param = lastNode.createStringParam("sep14", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep14 = param
    del param

    param = lastNode.createSeparatorParam("MIX", "Mix")

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.MIX = param
    del param

    param = lastNode.createStringParam("sep15", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep15 = param
    del param

    param = lastNode.createStringParam("sep16", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep16 = param
    del param

    param = lastNode.createDoubleParam("Dissolve1which", "Mix : ")
    param.setMinimum(0, 0)
    param.setMaximum(1.1, 0)
    param.setDisplayMinimum(0, 0)
    param.setDisplayMaximum(1, 0)
    param.setDefaultValue(1, 0)
    param.restoreDefaultValue(0)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setAddNewLine(True)
    param.setAnimationEnabled(True)
    lastNode.Dissolve1which = param
    del param

    param = lastNode.createStringParam("sep17", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep17 = param
    del param

    param = lastNode.createStringParam("sep18", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Controls.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep18 = param
    del param

    lastNode.Credits = lastNode.createPageParam("Credits", "Credits")
    param = lastNode.createStringParam("sep101", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep101 = param
    del param

    param = lastNode.createStringParam("sep102", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep102 = param
    del param

    param = lastNode.createSeparatorParam("NAME", "Crok_kuwahara_GL v1.1")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.NAME = param
    del param

    param = lastNode.createStringParam("sep103", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep103 = param
    del param

    param = lastNode.createStringParam("sep104", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep104 = param
    del param

    param = lastNode.createSeparatorParam("LINE01", "")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.LINE01 = param
    del param

    param = lastNode.createStringParam("sep105", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep105 = param
    del param

    param = lastNode.createStringParam("sep106", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep106 = param
    del param

    param = lastNode.createSeparatorParam("FR", "ShaderToy 0.8.8")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.FR = param
    del param

    param = lastNode.createStringParam("sep107", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep107 = param
    del param

    param = lastNode.createStringParam("sep108", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep108 = param
    del param

    param = lastNode.createSeparatorParam("CONVERSION", " (Fabrice Fernandez - 2019)")

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setPersistent(False)
    param.setEvaluateOnChange(False)
    lastNode.CONVERSION = param
    del param

    param = lastNode.createStringParam("sep109", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep109 = param
    del param

    param = lastNode.createStringParam("sep110", "")
    param.setType(NatronEngine.StringParam.TypeEnum.eStringTypeLabel)

    # Add the param to the page
    lastNode.Credits.addParam(param)

    # Set param properties
    param.setHelp("")
    param.setAddNewLine(True)
    param.setEvaluateOnChange(False)
    param.setAnimationEnabled(False)
    lastNode.sep110 = param
    del param

    # Refresh the GUI with the newly created parameters
    lastNode.setPagesOrder(['Controls', 'Credits', 'Node', 'Settings'])
    lastNode.refreshUserParamsGUI()
    del lastNode

    # Start of node "Output2"
    lastNode = app.createNode("fr.inria.built-in.Output", 1, group)
    lastNode.setLabel("Output2")
    lastNode.setPosition(4144, 4429)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupOutput2 = lastNode

    del lastNode
    # End of node "Output2"

    # Start of node "Source"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Source")
    lastNode.setLabel("Source")
    lastNode.setPosition(4137, 3480)
    lastNode.setSize(80, 32)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupSource = lastNode

    del lastNode
    # End of node "Source"

    # Start of node "Shadertoy1_2"
    lastNode = app.createNode("net.sf.openfx.Shadertoy", 1, group)
    lastNode.setScriptName("Shadertoy1_2")
    lastNode.setLabel("Shadertoy1_2")
    lastNode.setPosition(4139, 3859)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupShadertoy1_2 = lastNode

    param = lastNode.getParam("paramValueInt0")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("imageShaderFileName")
    if param is not None:
        param.setValue("/users/ffernandez/Natron2-3-6/Plugins/OFX/Natron/Shadertoy.ofx.bundle/Contents/Resources/presets/Shadertoy/Crok_kuwahara.frag.glsl")
        del param

    param = lastNode.getParam("imageShaderSource")
    if param is not None:
        param.setValue("//\n//\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//                        MM.                          .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                     MM.  .MMMM        MMMMMMM    MMM.  .MM\n//                    MM.  .MMM           MMMMMM     MMM.  .MM\n//                   MM.  .MmM              MMMM      MMM.  .MM\n//                  MM.  .MMM                 MM       MMM.  .MM\n//                 MM.  .MMM                   M        MMM.  .MM\n//                MM.  .MMM                              MMM.  .MM\n//                 MM.  .MMM                            MMM.  .MM\n//                  MM.  .MMM       M                  MMM.  .MM\n//                   MM.  .MMM      MM                MMM.  .MM\n//                    MM.  .MMM     MMM              MMM.  .MM\n//                     MM.  .MMM    MMMM            MMM.  .MM\n//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM\n//                        MM.                          .MM\n//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM\n//\n//\n// Adaptation pour Natron par F. Fernandez\n// Code original : crok_kuwahara Matchbox pour Autodesk Flame\n\n// Adapted to Natron by F.Fernandez\n// Original code : crok_kuwahara Matchbox for Autodesk Flame\n\n\n\n// iChannel0: Source, filter = nearest\n// BBox: iChannel0\n\n\nuniform int radius = 5; // Radius : (radius), min=0, max=100.\n\nvoid mainImage( out vec4 fragColor, in vec2 fragCoord )\n{\n    vec2 iChannel0_size = vec2(iResolution.x, iResolution.y);\n    vec2 uv = fragCoord.xy / iResolution.xy;\n    float n = float((radius + 1) * (radius + 1));\n\n    vec3 m[4];\n    vec3 s[4];\n    for (int k = 0; k < 4; ++k) {\n        m[k] = vec3(0.0);\n        s[k] = vec3(0.0);\n    }\n\n    for (int j = -radius; j <= 0; ++j)  {\n        for (int i = -radius; i <= 0; ++i)  {\n            vec3 c = texture2D(iChannel0, uv + vec2(i,j) / iChannel0_size).rgb;\n            m[0] += c;\n            s[0] += c * c;\n        }\n    }\n\n    for (int j = -radius; j <= 0; ++j)  {\n        for (int i = 0; i <= radius; ++i)  {\n            vec3 c = texture2D(iChannel0, uv + vec2(i,j) / iChannel0_size).rgb;\n            m[1] += c;\n            s[1] += c * c;\n        }\n    }\n\n    for (int j = 0; j <= radius; ++j)  {\n        for (int i = 0; i <= radius; ++i)  {\n            vec3 c = texture2D(iChannel0, uv + vec2(i,j) / iChannel0_size).rgb;\n            m[2] += c;\n            s[2] += c * c;\n        }\n    }\n\n    for (int j = 0; j <= radius; ++j)  {\n        for (int i = -radius; i <= 0; ++i)  {\n            vec3 c = texture2D(iChannel0, uv + vec2(i,j) / iChannel0_size).rgb;\n            m[3] += c;\n            s[3] += c * c;\n        }\n    }\n\n\n    float min_sigma2 = 1e+2;\n    for (int k = 0; k < 4; ++k) {\n        m[k] /= n;\n        s[k] = abs(s[k] / n - m[k] * m[k]);\n\n        float sigma2 = s[k].r + s[k].g + s[k].b;\n        if (sigma2 < min_sigma2) {\n            min_sigma2 = sigma2;\n            fragColor = vec4(m[k], 1.0);\n        }\n    }\n}\n")
        del param

    param = lastNode.getParam("mipmap0")
    if param is not None:
        param.set("nearest")
        del param

    param = lastNode.getParam("inputLabel0")
    if param is not None:
        param.setValue("Source")
        del param

    param = lastNode.getParam("inputEnable1")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable2")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("inputEnable3")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("bbox")
    if param is not None:
        param.set("iChannel0")
        del param

    param = lastNode.getParam("NatronParamFormatChoice")
    if param is not None:
        param.set("PC_Video")
        del param

    param = lastNode.getParam("mouseParams")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("paramCount")
    if param is not None:
        param.setValue(1, 0)
        del param

    param = lastNode.getParam("paramType0")
    if param is not None:
        param.set("int")
        del param

    param = lastNode.getParam("paramName0")
    if param is not None:
        param.setValue("radius")
        del param

    param = lastNode.getParam("paramLabel0")
    if param is not None:
        param.setValue("Radius :")
        del param

    param = lastNode.getParam("paramHint0")
    if param is not None:
        param.setValue("radius")
        del param

    param = lastNode.getParam("paramDefaultInt0")
    if param is not None:
        param.setValue(5, 0)
        del param

    param = lastNode.getParam("paramMinInt0")
    if param is not None:
        param.setValue(0, 0)
        del param

    param = lastNode.getParam("paramMaxInt0")
    if param is not None:
        param.setValue(100, 0)
        del param

    del lastNode
    # End of node "Shadertoy1_2"

    # Start of node "Dot1"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot1")
    lastNode.setLabel("Dot1")
    lastNode.setPosition(4170, 3667)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot1 = lastNode

    del lastNode
    # End of node "Dot1"

    # Start of node "Unpremult1"
    lastNode = app.createNode("net.sf.openfx.Unpremult", 2, group)
    lastNode.setScriptName("Unpremult1")
    lastNode.setLabel("Unpremult1")
    lastNode.setPosition(4139, 3746)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupUnpremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Unpremult1"

    # Start of node "Premult1"
    lastNode = app.createNode("net.sf.openfx.Premult", 2, group)
    lastNode.setScriptName("Premult1")
    lastNode.setLabel("Premult1")
    lastNode.setPosition(4139, 4013)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupPremult1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Premult1"

    # Start of node "Shuffle1"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle1")
    lastNode.setLabel("Shuffle1")
    lastNode.setPosition(4139, 3934)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1 = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("A.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    del lastNode
    # End of node "Shuffle1"

    # Start of node "Dot3"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot3")
    lastNode.setLabel("Dot3")
    lastNode.setPosition(4339, 3944)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot3 = lastNode

    del lastNode
    # End of node "Dot3"

    # Start of node "Dot4"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot4")
    lastNode.setLabel("Dot4")
    lastNode.setPosition(4339, 3667)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot4 = lastNode

    del lastNode
    # End of node "Dot4"

    # Start of node "Dissolve1"
    lastNode = app.createNode("net.sf.openfx.DissolvePlugin", 1, group)
    lastNode.setScriptName("Dissolve1")
    lastNode.setLabel("Dissolve1")
    lastNode.setPosition(4144, 4297)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupDissolve1 = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(1, 0)
        del param

    del lastNode
    # End of node "Dissolve1"

    # Start of node "Dot2"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot2")
    lastNode.setLabel("Dot2")
    lastNode.setPosition(4396, 3667)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot2 = lastNode

    del lastNode
    # End of node "Dot2"

    # Start of node "Dot5"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot5")
    lastNode.setLabel("Dot5")
    lastNode.setPosition(4401, 4307)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot5 = lastNode

    del lastNode
    # End of node "Dot5"

    # Start of node "Mask"
    lastNode = app.createNode("fr.inria.built-in.Input", 1, group)
    lastNode.setScriptName("Mask")
    lastNode.setLabel("Mask")
    lastNode.setPosition(3504, 3367)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.5, 0.2)
    groupMask = lastNode

    del lastNode
    # End of node "Mask"

    # Start of node "Shuffle1_2"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Shuffle1_2")
    lastNode.setLabel("Shuffle1_2")
    lastNode.setPosition(3482, 4008)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupShuffle1_2 = lastNode

    param = lastNode.getParam("outputR")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    param = lastNode.getParam("outputG")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    param = lastNode.getParam("outputB")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.A")
        del param

    del lastNode
    # End of node "Shuffle1_2"

    # Start of node "Alpha"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Alpha")
    lastNode.setLabel("Alpha")
    lastNode.setPosition(3658, 3761)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupAlpha = lastNode

    del lastNode
    # End of node "Alpha"

    # Start of node "Red"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Red")
    lastNode.setLabel("Red")
    lastNode.setPosition(3313, 3755)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupRed = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.R")
        del param

    del lastNode
    # End of node "Red"

    # Start of node "Green"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Green")
    lastNode.setLabel("Green")
    lastNode.setPosition(3434, 3758)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupGreen = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.G")
        del param

    del lastNode
    # End of node "Green"

    # Start of node "Blue"
    lastNode = app.createNode("net.sf.openfx.ShufflePlugin", 3, group)
    lastNode.setScriptName("Blue")
    lastNode.setLabel("Blue")
    lastNode.setPosition(3556, 3758)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.6, 0.24, 0.39)
    groupBlue = lastNode

    param = lastNode.getParam("outputA")
    if param is not None:
        param.set("B.uk.co.thefoundry.OfxImagePlaneColour.B")
        del param

    del lastNode
    # End of node "Blue"

    # Start of node "SwitchChannel"
    lastNode = app.createNode("net.sf.openfx.switchPlugin", 1, group)
    lastNode.setScriptName("SwitchChannel")
    lastNode.setLabel("SwitchChannel")
    lastNode.setPosition(3482, 3943)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupSwitchChannel = lastNode

    param = lastNode.getParam("which")
    if param is not None:
        param.setValue(3, 0)
        del param

    del lastNode
    # End of node "SwitchChannel"

    # Start of node "Crop"
    lastNode = app.createNode("net.sf.openfx.CropPlugin", 1, group)
    lastNode.setScriptName("Crop")
    lastNode.setLabel("Crop")
    lastNode.setPosition(3504, 3597)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.7, 0.3, 0.1)
    groupCrop = lastNode

    param = lastNode.getParam("rectangleInteractEnable")
    if param is not None:
        param.setValue(False)
        del param

    param = lastNode.getParam("size")
    if param is not None:
        param.setValue(2048, 0)
        param.setValue(1024, 1)
        del param

    param = lastNode.getParam("reformat")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Crop"

    # Start of node "Blur1"
    lastNode = app.createNode("net.sf.cimg.CImgBlur", 4, group)
    lastNode.setScriptName("Blur1")
    lastNode.setLabel("Blur1")
    lastNode.setPosition(3504, 3489)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.8, 0.5, 0.3)
    groupBlur1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Blur1"

    # Start of node "Invert1"
    lastNode = app.createNode("net.sf.openfx.Invert", 2, group)
    lastNode.setScriptName("Invert1")
    lastNode.setLabel("Invert1")
    lastNode.setPosition(3482, 4173)
    lastNode.setSize(80, 34)
    lastNode.setColor(0.48, 0.66, 1)
    groupInvert1 = lastNode

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(False)
        del param

    del lastNode
    # End of node "Invert1"

    # Start of node "Merge2"
    lastNode = app.createNode("net.sf.openfx.MergePlugin", 1, group)
    lastNode.setScriptName("Merge2")
    lastNode.setLabel("Merge2")
    lastNode.setPosition(4136, 4160)
    lastNode.setSize(80, 60)
    lastNode.setColor(0.3, 0.37, 0.776)
    groupMerge2 = lastNode

    param = lastNode.getParam("operation")
    if param is not None:
        param.set("copy")
        del param

    param = lastNode.getParam("enableMask_Mask")
    if param is not None:
        param.setValue(True)
        del param

    param = lastNode.getParam("disableNode")
    if param is not None:
        param.setValue(True)
        del param

    del lastNode
    # End of node "Merge2"

    # Start of node "Dot6"
    lastNode = app.createNode("fr.inria.built-in.Dot", 1, group)
    lastNode.setScriptName("Dot6")
    lastNode.setLabel("Dot6")
    lastNode.setPosition(3946, 3667)
    lastNode.setSize(15, 15)
    lastNode.setColor(0.7, 0.7, 0.7)
    groupDot6 = lastNode

    del lastNode
    # End of node "Dot6"

    # Now that all nodes are created we can connect them together, restore expressions
    groupOutput2.connectInput(0, groupDissolve1)
    groupShadertoy1_2.connectInput(0, groupUnpremult1)
    groupDot1.connectInput(0, groupSource)
    groupUnpremult1.connectInput(0, groupDot1)
    groupPremult1.connectInput(0, groupShuffle1)
    groupShuffle1.connectInput(0, groupShadertoy1_2)
    groupShuffle1.connectInput(1, groupDot3)
    groupDot3.connectInput(0, groupDot4)
    groupDot4.connectInput(0, groupDot1)
    groupDissolve1.connectInput(0, groupDot5)
    groupDissolve1.connectInput(1, groupMerge2)
    groupDot2.connectInput(0, groupDot4)
    groupDot5.connectInput(0, groupDot2)
    groupShuffle1_2.connectInput(0, groupSwitchChannel)
    groupAlpha.connectInput(0, groupCrop)
    groupRed.connectInput(0, groupCrop)
    groupGreen.connectInput(0, groupCrop)
    groupBlue.connectInput(0, groupCrop)
    groupSwitchChannel.connectInput(0, groupRed)
    groupSwitchChannel.connectInput(1, groupGreen)
    groupSwitchChannel.connectInput(2, groupBlue)
    groupSwitchChannel.connectInput(3, groupAlpha)
    groupCrop.connectInput(0, groupBlur1)
    groupBlur1.connectInput(0, groupMask)
    groupInvert1.connectInput(0, groupShuffle1_2)
    groupMerge2.connectInput(0, groupPremult1)
    groupMerge2.connectInput(1, groupDot6)
    groupMerge2.connectInput(2, groupInvert1)
    groupDot6.connectInput(0, groupDot1)

    param = groupShadertoy1_2.getParam("paramValueInt0")
    group.getParam("Shadertoy1_2paramValueInt0").setAsAlias(param)
    del param
    param = groupUnpremult1.getParam("disableNode")
    param.setExpression("not thisGroup.isPremult.get()", False, 0)
    del param
    param = groupPremult1.getParam("disableNode")
    param.setExpression("not thisGroup.isPremult.get()", False, 0)
    del param
    param = groupDissolve1.getParam("which")
    group.getParam("Dissolve1which").setAsAlias(param)
    del param
    param = groupSwitchChannel.getParam("which")
    param.setExpression("thisGroup.channelChoice.get()", False, 0)
    del param
    param = groupCrop.getParam("size")
    param.setExpression("myWidth = Blur1.getOutputFormat().width()\nret = myWidth", True, 0)
    param.setExpression("myHeight = Blur1.getOutputFormat().height()\nret = myHeight", True, 1)
    del param
    param = groupInvert1.getParam("disableNode")
    param.setExpression("thisGroup.invertMask.get()", False, 0)
    del param
    param = groupMerge2.getParam("disableNode")
    param.setExpression("not thisGroup.useMask.get()", False, 0)
    del param

    try:
        extModule = sys.modules["Crok_kuwahara_GLExt"]
    except KeyError:
        extModule = None
    if extModule is not None and hasattr(extModule ,"createInstanceExt") and hasattr(extModule.createInstanceExt,"__call__"):
        extModule.createInstanceExt(app,group)
