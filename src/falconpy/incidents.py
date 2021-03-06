################################################################################################################
# CROWDSTRIKE FALCON                                                                                           #
# OAuth2 API - Customer SDK                                                                                    #
#                                                                                                              #
# incidents - Falcon X Incidents API Interface Class                                                           #
################################################################################################################
# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>

import requests
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

class Incidents:
    """ The only requirement to instantiate an instance of this class
        is a valid token provided by the Falcon API SDK OAuth2 class.
    """

    def __init__(self, access_token, base_url='https://api.crowdstrike.com'):
        """ Instantiates the base class, ingests the authorization token, 
            and initializes the headers and base_url global variables. 
        """
        self.headers = { 'Authorization': 'Bearer {}'.format(access_token) }
        self.base_url = base_url

    class Result:
        """ Subclass to handle parsing of result client output. """
        def __init__(self):
            """ Instantiates the subclass and initializes the result object. """
            self.result_obj = {}
            
        def __call__(self, status_code, headers, body):
            """ Formats values into a properly formatted result object. """
            self.result_obj['status_code'] = status_code
            self.result_obj['headers'] = dict(headers)
            self.result_obj['body'] = body
            
            return self.result_obj

    def CrowdScore(self, parameters):
        """ Query environment wide CrowdScore and return the entity data. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/CrowdScore
        FULL_URL = self.base_url+'/incidents/combined/crowdscores/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def GetBehaviors(self, body):
        """ Get details on behaviors by providing behavior IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/GetBehaviors
        FULL_URL = self.base_url+'/incidents/entities/behaviors/GET/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def PerformIncidentAction(self, body):
        """ Perform a set of actions on one or more incidents, such as 
            adding tags or comments or updating the incident name or description.
        """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/PerformIncidentAction
        FULL_URL = self.base_url+'/incidents/entities/incident-actions/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def GetIncidents(self, body):
        """ Get details on incidents by providing incident IDs. """
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/GetIncidents
        FULL_URL = self.base_url+'/incidents/entities/incidents/GET/v1'
        HEADERS = self.headers
        BODY = body
        result = self.Result()
        try:
            response = requests.request("POST", FULL_URL, json=BODY, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def QueryBehaviors(self, parameters):
        """ Search for behaviors by providing an FQL filter, sorting, and paging details. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/QueryBehaviors
        FULL_URL = self.base_url+'/incidents/queries/behaviors/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned

    def QueryIncidents(self, parameters):
        """ Search for incidents by providing an FQL filter, sorting, and paging details. """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/incidents/QueryIncidents
        FULL_URL = self.base_url+'/incidents/queries/incidents/v1'
        HEADERS = self.headers
        PARAMS = parameters
        result = self.Result()
        try:
            response = requests.request("GET", FULL_URL, params=PARAMS, headers=HEADERS, verify=False)
            returned = result(response.status_code, response.headers, response.json())
        except Exception as e:
            returned = result(500, {}, str(e))

        return returned
