import asyncio
import websockets
import setup
import uutils
import random

vtube_api = "ws://0.0.0.0:8001"


def vtube_worker(shared_data):
    # 创建事件循环
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)

    async def vtube_run(shared_data):
        # 连接上服务器：
        websocket = await websockets.connect('ws://127.0.0.1:8001')

        # 初始化
        await setup.init(websocket)

        FaceAngleX = 0.00   # 脸左右运动
        FaceAngleY = 0.00   # 脸上下运动
        FaceAngleZ = 0.00   # 左右歪头
        EyeRightX = 0.00    # 眼球左右运动
        EyeRightY = 0.00    # 眼球上下运动
        Brows = 0.50        # 眉毛

        # FaceAngleX_max = 30.00      # 右
        # FaceAngleX_min = -30.00     # 左
        # FaceAngleY_max = 15.00      # 上
        # FaceAngleY_min = -15.00     # 下
        # FaceAngleZ_max = 30.00      # 右
        # FaceAngleZ_min = -30.00     # 左
        # EyeRightX_max = 1.00        # 左
        # EyeRightX_min = -1.00       # 右
        # EyeRightY_max = 1.00        # 上
        # EyeRightY_min = -1.00       # 下
        # Brows_max = 1.00            # 上
        # Brows_min = 0.00            # 下

        parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                            {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]

        V_tt = 0

        while 1:
            await uutils.vtube_control(websocket, parameter_values)
            if shared_data.value == 1:                  # "看右下方"、
                faceY = -10 * 0.04
                faceX = 25 * 0.04
                eyeX = 0.5 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleY += faceY
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 2:                  # "看左下方"、
                faceY = -10 * 0.04
                faceX = -25 * 0.04
                eyeX = -0.5 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleY += faceY
                    EyeRightX += eyeX
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 3:                  # "看右上方"、
                faceY = 15 * 0.04
                faceX = 30 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleY += faceY
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 4:                  # "看左上方"、
                faceY = 15 * 0.04
                faceX = -30 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleY += faceY
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 5:                  # "看向下方"、
                faceY = -15 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleY += faceY
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 6:                  # "看向上方"、
                faceY = 15 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleY += faceY
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 99
            if shared_data.value == 7:                  # "看向右侧"、
                faceX = 20 * 0.04
                faceY = 3 * 0.04
                faceZ = -5 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleY += faceY
                    FaceAngleZ += faceZ
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 8:                  # "看向左侧"、
                faceX = -20 * 0.04
                faceY = 3 * 0.04
                faceZ = 5 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleY += faceY
                    FaceAngleZ += faceZ
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 9:                  # "皱眉"、
                faceX = -20 * 0.04
                faceZ = 20 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleZ += faceZ
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 0
            if shared_data.value == 10:                  # "向左歪头"、
                faceX = 20 * 0.04
                faceZ = -20 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleZ += faceZ
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 99
            if shared_data.value == 11:                  # "向右歪头"、
                faceX = -20 * 0.04
                faceZ = 20 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleZ += faceZ
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                shared_data.value = 99
            if shared_data.value == 12:                  # "左右摇头"、
                faceX = 20 * 0.04
                faceZ = -20 * 0.04
                ss = 0
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleZ += faceZ
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.01)
                    ss += 1
                ss = 0
                faceX = -40 * 0.04
                faceZ = 40 * 0.04
                while ss <= 25:
                    FaceAngleX += faceX
                    FaceAngleZ += faceZ
                    parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                        {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                    await uutils.vtube_control(websocket, parameter_values)
                    await asyncio.sleep(0.02)
                    ss += 1
                ss = 0
                shared_data.value = 99
            if shared_data.value == 99:                 # 复位
                if FaceAngleX != 0 or FaceAngleY != 0 or FaceAngleZ != 0 or EyeRightX != 0 or EyeRightY != 0 or Brows != 0.5:
                    faceX = -FaceAngleX * 0.04
                    faceY = -FaceAngleY * 0.04
                    faceZ = -FaceAngleZ * 0.04
                    eyeX = -EyeRightX * 0.04
                    eyeY = -EyeRightY * 0.04
                    if Brows > 0.50:
                        browss = -((Brows - 0.50)*0.04)
                    elif Brows < 0.50:
                        browss = ((0.50 - Brows)*0.04)
                    elif Brows == 0.50:
                        browss = 0.00
                    ss = 0
                    while ss <= 25:         # 分50段完成动作,看着流畅点,有意愿可以自己改改
                        FaceAngleX += faceX
                        FaceAngleY += faceY
                        FaceAngleZ += faceZ
                        EyeRightX += eyeX
                        EyeRightY += eyeY
                        Brows += browss
                        parameter_values = [{"id": "FaceAngleX", "value": FaceAngleX}, {"id": "FaceAngleY", "value": FaceAngleY}, {"id": "FaceAngleZ", "value": FaceAngleZ},
                                            {"id": "EyeRightX", "value": EyeRightX}, {"id": "EyeRightY", "value": EyeRightY}, {"id": "Brows", "value": Brows}]
                        await uutils.vtube_control(websocket, parameter_values)
                        await asyncio.sleep(0.01)
                        ss += 1
                    ss = 0
                    FaceAngleX = 0.00
                    FaceAngleY = 0.00
                    FaceAngleZ = 0.00
                    EyeRightX = 0.00
                    EyeRightY = 0.00
                    Brows = 0.50
                shared_data.value = 0
            if V_tt == 500:
                shared_data.value = random.randint(1, 12)
            elif V_tt >= 600:
                V_tt = 0
                shared_data.value = 99
            V_tt += 1
            await asyncio.sleep(0.01)

    # 运行协程
    loop.run_until_complete(vtube_run(shared_data))
    loop.close()
