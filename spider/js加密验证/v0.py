#破解有道词典
from urllib import request,parse
def youdao():
    url=""
    data={
        "i":"girl",
        "from":"AUTO",
        "to":"AUTO",
        "smartresult":"dict",
        "client":"fanyideskweb",
        "salt":"1523100789519",
        "sign":"b8a55a436686cd89873fa46514ccedbe",
        "doctype":"json",
        "version":"2.1",
        "keyform":"fanyi.web",
        "action":"FY_BY_REALTIME",
        "typoResult":"false"

    }
    data=parse.urlencode(data).encode()
    header={


    }