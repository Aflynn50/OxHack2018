from flask import Flask, render_template,jsonify
app = Flask(__name__,static_url_path='/static')
import time
import threading
from DispatchStrategy import ManageSit
import VictumInfo as vi
from GeoInfo import VolunteersCenter, GeoPosition,VictimInfo,VictimRegion
import json


thousand = 1
centers = []
centers.append(VolunteersCenter(GeoPosition(45.4, 21, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(46, 24, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(44.5, 28, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(47, 27.5, 4), thousand))
centers.append(VolunteersCenter(GeoPosition(44.3, 28, 4), thousand))

disp = -1
assocs = -1

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/getTweets")
def getTweets():
    return json.dumps(vi.getUpdateTweets())


@app.route("/getDispatches")
def getDispatches():
    global assocs
    if assocs == -1:
        return "[]"
    data = []
    for dispatch in assocs:
        thisData = []
        thisData.append( {"lat":dispatch[0].latitude,"lng":dispatch[0].longitude} )
        thisData.append( {"lat":dispatch[1].latitude,"lng":dispatch[1].longitude} )
        thisData.append(dispatch[2])
        data.append(thisData)


    return json.dumps(data)

@app.route("/getIdleCenters")
def getIdleCenters():
    global disp
    if disp == -1:
        return "[]"
    data = []
    for center in disp.centers:
        data.append( [{"lat":center.location.latitude,"lng":center.location.longitude},center.responderNumbers] )
    return json.dumps(data)


@app.route("/getUnresolvedRegions")
def getUnresolvedRegions():
    global disp
    if disp == -1:
        return "[]"
    data = []
    for region in disp.affectedRegions:
        data.append( [{"lat":region.location.latitude,"lng":region.location.longitude},region.populationCount] )
    return json.dumps(data)





victims2 = []
for i in range(1):
    victims2.append(VictimRegion(GeoPosition(46.766667, 23.583333,1),1))
for i in range(1):
    victims2.append(VictimRegion(GeoPosition(46.583333, 26.916667,1),1))
for i in range(1):
    victims2.append(VictimRegion(GeoPosition(44.333333, 23.816667,1),1))
for i in range(1):
    victims2.append(VictimRegion(GeoPosition(44.435278, 26.102778,1),1))

disp2 = -1
assocs2s = -1

disp2 = ManageSit([], centers,victims2,True)
assocs2 = disp2.dispatch()

@app.route("/situation")
def index2():
    return render_template("situation.html")


@app.route("/getDispatches2")
def getDispatches2():
    global assocs2
    if assocs2 == -1:
        return "[]"
    data = []
    for disp2atch in assocs2:
        thisData = []
        thisData.append( {"lat":disp2atch[0].latitude,"lng":disp2atch[0].longitude} )
        thisData.append( {"lat":disp2atch[1].latitude,"lng":disp2atch[1].longitude} )
        thisData.append(disp2atch[2])
        data.append(thisData)


    return json.dumps(data)

@app.route("/getIdleCenters2")
def getIdleCenters2():
    global disp2
    if disp2 == -1:
        return "[]"
    data = []
    for center in disp2.centers:
        data.append( [{"lat":center.location.latitude,"lng":center.location.longitude},center.responderNumbers] )
    return json.dumps(data)


@app.route("/getUnresolvedRegions2")
def getUnresolvedRegions2():
    global disp2
    if disp2 == -1:
        return "[]"
    data = []
    for region in disp2.affectedRegions:
        data.append( [{"lat":region.location.latitude,"lng":region.location.longitude},region.populationCount] )
    return json.dumps(data)













def worker():
    while(True):
        victims = vi.getVictims()
        global disp
        global assocs
        disp = ManageSit(victims, centers,[],False)
        assocs = disp.dispatch()
        print(assocs)
        time.sleep(1)



if __name__ == '__main__':
    t = threading.Thread(target=worker)
    t.start()

    app.debug=True
    app.run()