from urllib import request
if __name__=='__main__':
    url="http://www.renren.com/965187997/profile"
    headers={
        "cookie":"anonymid=k1xcd3nlt0lane; depovince=GW; jebecookies=cce3b5de-5604-418f-b17e-ade1d1edda02|||||; _r01_=1; ick_login=69169056-5cad-4c1f-a55e-375f60af0465"

    }
    req=request.Request(url,headers=headers)
    rsp=request.urlopen(req)
    html=rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)

