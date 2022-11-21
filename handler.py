from os import path
import sys, random


def response_path():
    base_path = getattr(sys, '_MEIPASS', path.abspath('.'))
    return path.join(base_path, 'responses')


def application(environ, start_response):
#    print('\n'.join([str((f'{key}: {value}').encode('utf-8'))
#                     for key, value in environ.items()]))

    status = '200 OK'
    headers = [('Content-Type', 'application/json')]
    path_info = environ['PATH_INFO']
    # service = path_info.split('/')[-1]
    if  '/environment' in path_info:
        response = '{"applicationId":"danmakujp4-v1","isProd":true}'
    elif '/identity/transfer/' in path_info and '/execute' in path_info:
        response = '{"accessToken":"eyJraWQiOiJiYzk2ZDMxMS05NzFiLTQ4NWEtOTU5Yy1jMGYyOWI2MWY0YTEiLCJhbGciOiJSUzI1NiJ9.eyJkYXRhIjp7ImNoIjoiU0RLIiwic2Vzc2lvbiI6eyJzdG9yZUFjY291bnRJZEhhc2giOiJiUEc2Z0pwQldndEgxRkx5emJlNkhraEZtbzg0d296QjFaR3pDM3VycEl3PSIsImJ1bmRsZUlkIjoiY29tLmRlbmEuYTEyMDI2ODAxIiwidXNlclJlZ2lzdGVyZWRBdE1pbGxpcyI6MTY2NjM2NDU1ODc1OSwic3RvcmUiOiJHVUVTVCIsInVzZXJJZCI6IjA5OGZhZDFhLTYwMWEtNDcyNS1iM2Y5LTZkOTM4MjFkYzEyZCJ9fSwia2luZCI6IkFDQ0VTU19UT0tFTiIsImV4cCI6MTY2NjM2NjIwNiwiaWF0IjoxNjY2MzY1NjA2LCJqdGkiOiIyYTQ0OGYxNi1hMjA5LTQ0ODEtODQyZi1hYmRjYTQ2MDJmYWIifQ.kg8ED6cqVJ6HaToykN_ntyCwpcER37f_ZpzhT--NSVZNvbMUcz9sP0vc-yLuzAK9i9I1UtsMngsEREHFxsEWf4oZow07yueOgD-R-iNw7lE8fxtLQhp_C1fzCSeFiNRZFL4rmUS91g0uSC9IHUZZbNBe8oxlixjrp9WyUL_dtQ18cBvC67G__tBR7hjdGna4z5owDmy1Q19YX3WPEVeW2gzACSo_U-_YouD8s7OgjEEU1iNV1AfwIy42H_pDxAyVwgTzsCaoIyBo57AP0HUMpl4ght06Z0dPZvF0QiY1Bj_i_NZM9O0zI6zAoZoHjFjni310pFo3TAxaxizGI6tKaQ","lcxUserIdToken":"eyJraWQiOiJiYzk2ZDMxMS05NzFiLTQ4NWEtOTU5Yy1jMGYyOWI2MWY0YTEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIwOThmYWQxYS02MDFhLTQ3MjUtYjNmOS02ZDkzODIxZGMxMmQiLCJkYXRhIjp7InVzZXJSZWdpc3RlcmVkQXQiOjE2NjYzNjQ1NTh9LCJraW5kIjoiTENYX1VTRVJfSURfVE9LRU4iLCJleHAiOjE2NjY0NTIwMDYsImlhdCI6MTY2NjM2NTYwNn0.b3v5IRtWdI3eY_YAprSZzctawScw89i3ZPjqu6mgXZjggKDS0sDBhyFbeXL8UA-WC0d5ZTOz38NNdN7o-GIaini3gxt3UREXSXWhtK3Iwdmrt08Yj3Sk239kHbwZ9X6OKsUyLbewxLVx-apeXeHgS7YwQmZMxzz6QkCtCcu-JMCrdgJvmVUGD2JF9aJ_zVuAnfwq9pDw-jU_X7adysOVi2YBSoUez8kRX809VK3ln58DDmttJmm5L_SGw7jf7-UMckBbhAfLeUuP0XTHeT5zWwD5GRMslEGzeEdR3UEVL28QfLk7H_773Il3tB-3hF8lX8qN4yrIy6AlBLLfgHGBig","user":{"id":"098fad1a-601a-4725-b3f9-6d93821dc12d","registeredAt":1666364558},"signInSessionToken":"eyJraWQiOiI2M2UxZTE5OC0xY2I0LTQ0ZjktODIzNS0wZjA2ZGM1MDNkODEiLCJhbGciOiJSUzI1NiJ9.eyJkYXRhIjp7InN0b3JlQWNjb3VudElkSGFzaCI6ImJQRzZnSnBCV2d0SDFGTHl6YmU2SGtoRm1vODR3b3pCMVpHekMzdXJwSXc9IiwiaXNNb2NrIjpmYWxzZSwic3RvcmUiOiJHVUVTVCIsInNlc3Npb25JZCI6IjQ2NTE4NGVkLTM0ZDctNDNiOC04MzI3LTcwYWU1MWRhNzY1NCIsInVzZXJJZCI6IjA5OGZhZDFhLTYwMWEtNDcyNS1iM2Y5LTZkOTM4MjFkYzEyZCJ9LCJraW5kIjoiU0lHTl9JTl9TRVNTSU9OX1RPS0VOIiwiZXhwIjozMzYzNDM2NTYwNiwiaWF0IjoxNjY2MzY1NjA2fQ.hpqnx1rxJ-W8zRPITNBzvqnEnZvWjFJaidqrcHBts3GBO9NvWsDBvqtz-hB70iaJ_h-RBNCrypR227vyW7bGgrcYh8uB0qC4CD8gzP3iBQFepyYSr-Gl36sdWog8LrIty1-N58DV5nz4YIA2tQnvHp62qu7_5wXxzLO-T0xLicp4SIaBzyLvLE-UOpxgnm2jCmFEd9FEJl6ZxDAn4yUzMxLizMu4z0OnLTcBJhHConPSYhB9JIwCszocRszqjwG2D0XRRDpp9Dt-WCwfC2iEGhDUNB54gENRxv-Qy_16vDxgSqe2yGfrkXHLv8Z4kQgWLCPvvNJCQMOpotpUHlOtIQ","signInSessionId":"465184ed-34d7-43b8-8327-70ae51da7654","govPolicy":{"enablePopup":false,"popupSkippable":true},"analyticsSessionId":"2a448f16-a209-4481-842f-abdca4602fab"}'
    elif '/auth/user-access-token' in path_info:
        response = '{"userId":"3267a5ec-edeb-44ed-bb07-371145947f54","accessToken":"eyJraWQiOiJiYzk2ZDMxMS05NzFiLTQ4NWEtOTU5Yy1jMGYyOWI2MWY0YTEiLCJhbGciOiJSUzI1NiJ9.eyJkYXRhIjp7ImNoIjoiU0RLIiwic2Vzc2lvbiI6eyJzdG9yZUFjY291bnRJZEhhc2giOiJ3Um1kcjZxaWRjMFk3S1hBUTRaNWNXeHErRzVEVDUrUG1RSnBUY2VoUmdnPSIsImJ1bmRsZUlkIjoiY29tLmRlbmEuYTEyMDI2ODAxIiwidXNlclJlZ2lzdGVyZWRBdE1pbGxpcyI6MTY2NTgzNjU2NzEzNiwic3RvcmUiOiJBUFBMRSIsInVzZXJJZCI6IjMyNjdhNWVjLWVkZWItNDRlZC1iYjA3LTM3MTE0NTk0N2Y1NCJ9fSwia2luZCI6IkFDQ0VTU19UT0tFTiIsImV4cCI6MTY2NjM2NTQ2OSwiaWF0IjoxNjY2MzY0ODY5LCJqdGkiOiIyY2Q3MDFjZS05MTUzLTQxOTQtYjllYS1kNjhjMjNmNTZiNzMifQ.ftiqI1oq4tQI3aTcxR8PKi5XuxanCT-TFq3nvv2gbbvmb5y0NQMKI_dLaT75XuLZQX-UsQTyPXnwfi0klTxtQG8003hdxPN7c3iI5D8uXPU8EIFgZxKk2H_tZQvRRiXEqLfa1wQgls_BGfmqTfsodvzgr_KS_DUXGIw5dOWFpFX5wA6tV2agS5oy8Y9U9RhPbJvHzZJLn9PAgGZQZf_V2SUWlMiMhzrGhdtD8i5QDKtIngdM_RlevqOfwYBPfFB_9hUeNHavGP1zt7CRQ9Q5Iav8YAWnCfUYUlxlFyvVgnaTTM5oGlsZmEsLMYfhJRMgyRc0cF6IMV7z7IhHeOHn7Q","signInSessionId":"3e87aee1-e928-418b-9fbd-00dd69ae1a35","analyticsSessionId":"2cd701ce-9153-4194-b9ea-d68c23f56b73"}'
    elif '/gcp/analytics/config' in path_info:
        response = '{"isPubsubEnabled":true,"topicPath":"projects/dena-lcx-live-prod-jp-gcp/topics/analytics-sdk","pubsubAccessToken":"ya29.c.b0AUFJQsGaeygLl5JHRN9HQNY7eekQ5m4xaKMdExva2Ql6wkSjWA1C2nbnsKrivAo2JgSLvlJnt15nZh0Y4dzeo9_0timRiwJoNxG2wBDZtEQb4JfzbKXQzIUixPLYHIFLxEVvAXYuPHNfvRHy1Ha5Epq1LcEA5WwK87Vf-9peg8s7menyJ7NVCqEZ5w02wtjN1Uqo32LvQQWJqOVnRSNLPqS6sZq5Uyj9kaRNwKs6wQ_AyYQw5zt2cM5-HqwIE6SSPhbTOail9wGHFDPGw5YuaUM2T-YAVKg3xR3Mja01jsyhvGNOzRabgAYle7ZhnQsKXl8OA4Wtzsrfxrlx-mqNozHvPtTX6b4YHe9symzNY3v4dXCRdZrAmA_UBUyrxu0vQ8_fF3GGII-GURJfmqhoU3-gnEKMnkGjjQVWwmRQFXjxsjhsk4cmhq4UWvSxyWLFql3pD0GPmEJwVZ-Amr0d-8sHtQdYfN4YpFx3a61otO35Ktc........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................"}'
    elif 'identity/user-id-token/' in path_info:
        response = '{"lcxUserIdToken":"eyJraWQiOiJiYzk2ZDMxMS05NzFiLTQ4NWEtOTU5Yy1jMGYyOWI2MWY0YTEiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMjY3YTVlYy1lZGViLTQ0ZWQtYmIwNy0zNzExNDU5NDdmNTQiLCJkYXRhIjp7InVzZXJSZWdpc3RlcmVkQXQiOjE2NjU4MzY1Njd9LCJraW5kIjoiTENYX1VTRVJfSURfVE9LRU4iLCJleHAiOjE2NjY0NTEyNzAsImlhdCI6MTY2NjM2NDg3MH0.k_qNqCawa-IntGXOJp9tYlHaOZGSe9uBOnC8R2aks-KHm4dsskclNJYiL4zVFTqUR_NNQkKf_Ff0cv3QFi-BsDTIFjiXBTyyXWpj1Enx0cSr8FlNBjId48khzayMlku9R91XNzk7wJlF9ffpqpfxig_VqkcjvJppWLbGQ2iSwGuoSq8Uj8D4jmXbARCoVems8hZ6nSJ4px0dE1lzO7s2VosUUSXtXl3OISfei3mKAksDLuFsKZZTfJ2eZXL547VMBW-dzVjUZXHb8oSUOp-NAmTVOZr4jeLDkfMmuDDPD2JLbIjEaNpl3CiiqYSc5LsnoRG1iGONveaOM8ZL9YpapA"}'
    elif '/push/user-token/' in path_info:
        response = ''
    elif '/identity/link-state' in path_info:
        response = '{"hasAnyLink":true}'
    elif '/identity/sign-out' in path_info:
        status = '204 No Content'
        response = ''
    elif '/subs/' in path_info:
        response = '[]'
    else:
        status = '503 Service Unavailable'
        headers = [('Content-Type', 'text/html')]
        response = '503 Service Unavailable'

        return [b'503 Service Unavailable']

    headers.append(('Content-Length', str(len(response))))
    start_response(status, headers)
    return [bytes(response, 'ascii')]

