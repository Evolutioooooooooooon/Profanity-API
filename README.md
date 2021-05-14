# 욕설 감지 API v1

made by [Chul0721](https://github.com/chul0721) from [Team Sirius](https://teamsirius.xyz), GNU GENERAL PUBLIC LICENSE v3

## 문서

목차
* [1. Hello World](#Hello-World)
    - [1-1. Base URL](#BaseURL)
    - [1-2. Status Codes](#Status-Codes)
* [2. Request](#Request)
* [3. Response](#Response)

## Hello World

API가 작동하는지의 여부를 확인하기 위한 테스트 과정입니다. 해당 API는 별도의 키값을 통한 인증 과정이 없기 때문에 이 과정은 건너 뛰어도 무방합니다.

ex)
```http
GET /api/v1/
```

### Base URL

호스팅 준비 중입니다.

### Status Codes

API의 상태에 따라 아래 HTTP 상태 코드를 반환합니다.

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |

## Request

API로 보내는 요청은 전부 GET으로 통일되어 있습니다. <br />
요청을 보낼 때 파라미터를 통해 반환 값을 사용자화 할 수 있습니다. 아래 표에 따라 알맞는 값을 보낼 수 있습니다. "필수"로 적혀 있는 값을 요청하지 않는다면 값을 받을 수 없습니다.

| Parameter | Type | Description | Value | Required |
| :---      | :--- | :---        | :---  | :---     |
| `message` | `string` | 메시지 내용에 욕설이 있는지 검사합니다. | 검사할 메시지 내용 | **필수** |

ex)
```http
GET /api/v1/data?message=메시지
```

## Response

해당 API는 아래 값과 같이 값을 반환합니다.

ex) 욕설이 포함되어 있을 경우
```
cuss
```

ex) 욕설이 포함되어 있지 않을 경운
```
clean
```

반환 값은 모두 문자열의 형태로 반환되기 때문에 확인해주시기 바랍니다.


```
해당 문서 및 코드에 기여하고 싶으신가요?
PR을 넣을 경우 관리자가 검토 후 승인 여부를 결정해 드립니다!
많은 도움 부탁드립니다 :)
```