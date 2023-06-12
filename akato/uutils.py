import json
from png import png_base64

PLUGIN_NAME = "Akato's sport"
PLUGIN_DEVELOPER = "by sugar"
REQUEST_ID = "VTubeAkato"
API_VERSION = "1.0"

FaceAngleX = 1


# 验证并获取令牌
# 返回值信息：
# "authenticationToken" 是API 身份验证的令牌
async def vtube_token(websocket):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": API_VERSION,
        "requestID": REQUEST_ID,
        "messageType": "AuthenticationTokenRequest",
        "data": {
            "pluginName": PLUGIN_NAME,
            "pluginDeveloper": PLUGIN_DEVELOPER,
            "pluginIcon": png_base64
        }
    }

    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    authtoken = pack['data']['authenticationToken']
    # print(authtoken)
    return authtoken


# 使用已有的令牌进行验证
# 返回值信息：
# true or false
async def vtube_plugin(websocket, authtoken):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": API_VERSION,
        "requestID": REQUEST_ID,
        "messageType": "AuthenticationRequest",
        "data": {
            "pluginName": PLUGIN_NAME,
            "pluginDeveloper": PLUGIN_DEVELOPER,
            "authenticationToken": authtoken
        }
    }
    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    pack = json.loads(json_data)
    a = pack['data']['authenticated']
    return a


# 获取当前统计信息
# 返回值信息：
# "uptime"包含自 VTube Studio 启动以来的毫秒数。
# "framerate"是当前渲染 FPS 值。
# "allowedPlugins"是用户当前允许使用 VTube Studio 的插件数量，
# "connectedPlugins"是当前连接到 VTube Studio API 的插件数量。
# "startedWithSteam"如果应用已使用 Steam 启动，则为 true，否则为 false
# （如果文件.bat已用于在没有 Steam 的情况下启动 VTS）。
async def vtube_statistics(websocket):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": API_VERSION,
        "requestID": REQUEST_ID,
        "messageType": "StatisticsRequest",
    }

    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    # print(json_data)
    return json_data


async def vtube_control(websocket, parameter_values):
    payload = {
        "apiName": "VTubeStudioPublicAPI",
        "apiVersion": API_VERSION,
        "requestID": REQUEST_ID,
        "messageType": "InjectParameterDataRequest",
        "data": {
            "faceFound": False,
            "mode": "set",
            "parameterValues": parameter_values
        }
    }

    await websocket.send(json.dumps(payload))
    json_data = await websocket.recv()
    # print(json_data)
    return json_data
