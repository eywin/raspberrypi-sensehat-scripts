#!/usr/bin/python3
# Licensed under the EUPL, Version 1.2 or – as soon they will be approved by
# the European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at:
#
#   https://joinup.ec.europa.eu/software/page/eupl
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Licence is distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the Licence for the specific language governing permissions and
# limitations under the Licence.

import json
import socket
import os
from six.moves import urllib

HEADERS = {'Accept': 'application/json',
            'Content-Type': 'application/json',
            'User-Agent': 'avgangstidstavle',
            'ET-Client-Name': 'avgangstidstavle',
            'ET-Client-ID': socket.gethostname()}

GRAPHQL_ENDPOINT = "https://api.entur.io/journey-planner/v2/graphql"
CONNECT_TIMEOUT_SECONDS = 15

def sendGraphqlQuery(query, variables):
    data = {'query': query, 'variables': variables}

    req = urllib.request.Request(GRAPHQL_ENDPOINT, json.dumps(data).encode('utf-8'), HEADERS)

    response = urllib.request.urlopen(req, timeout=CONNECT_TIMEOUT_SECONDS)
    return response.read().decode('utf-8')


query = """
{
  quay(id: "NSR:Quay:11449") {
    id
    name
    estimatedCalls(timeRange: 72100, numberOfDepartures: 1) {
      realtime
      aimedArrivalTime
      expectedArrivalTime
      destinationDisplay {
        frontText
      }
    }
  }
}"""


def get_departures():
    departures = json.loads(sendGraphqlQuery(query, {}))
    try:
        return departures['data']['quay']['estimatedCalls']
    except:
        return dict()


if __name__ == '__main__':
    print(get_departures())
