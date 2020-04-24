import serverconnect
import bd
import pickle
import json

#connect
conn = serverconnect.connectclient()
cur,con = bd.connectbd()
#login and password proverka
while True:
    #priem logpas
    data = conn.recv(1024)
    data = json.loads(data.decode("utf-8"))

    #check logpas
    otvet = bd.checklogpas(data[0],data[1],cur,con)
    #otpravka
    conn.send(json.dumps(otvet).encode('utf-8'))
    if otvet == 1:
        break
#rabota s osnovnoi formoi
while True:
    data = conn.recv(1024) #priem dannih
    data = json.loads(data.decode("utf-8"))

    if data[0] == 0: #vibor nuhnoi funkcii
        selecttabl = bd.selecttabl(data[1], cur, con) #vivod tabl
        conn.send(json.dumps(selecttabl).encode('utf-8')) #otpravka
    elif data[0] == 1:
        dannie = data[len(data) - 1]
        bd.inserttabl(data[1],dannie, cur, con)# vstavka v tablicu
    elif data[0] == 2:
        bd.deletstroku(data[1], data[2], data[3], cur, con) #udalenie iz nee
    elif data[0] == 3:
        break

#con close
con.close()
conn.close()
