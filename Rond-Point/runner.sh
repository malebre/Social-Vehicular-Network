#!/bin/bash

duarouter --repair --ignore-errors -n data/RondPoint.net.xml -f data/RondPoint.flow.xml -o data/RondPoint.rou.xml
duarouter --repair --ignore-errors -n data/RondPoint.net.xml -f data/RondPointBus.flow.xml -o data/RondPointBus.rou.xml

