import requests
from django.http import JsonResponse

LIGHT_OID = '5213bf96-c25a-40bf-891c-49cb84db2844'
OPENHAB_HOST = 'localhost'
OPENHAB_PORT = 3000

PREDEFINED_COLORS = {
    'green': '',
    'red': '',
}


def lightbulb_color(request, oid, pid):
    response = {
        'property': 'color',
        'value': -1
    }

    # Temporary logic as this is a quick-fix adapter that will most likely be replaced
    if oid != LIGHT_OID:
        return JsonResponse(data=response, status=404)

    if pid != 'color':
        return JsonResponse(data=response, status=404)

    if request.method == 'GET':
        res = requests.get('https://{HOST}/')
        if res.status_code == 200:
            # response['value'] = res.json()
            pass
        return JsonResponse(data=response, status=200)
    elif request.method == 'PUT':
        return JsonResponse(data=response, status=200)
    else:
        response['error_message'] = 'unsupported method'
        return JsonResponse(data=response, status=400)


def thing_descriptor(request):
    td = {
        "adapter-id": "openhab-ikea-lightbulb",
        "thing-descriptions": [{
            "oid": LIGHT_OID,
            "name": "IKEA light 1",
            "type": "core:Device",
            "properties": [{
                "pid": "color",
                "monitors": "adapters:DeviceStatus",
                "read_link": {
                    "href": "/devices/{oid}/properties/color".format(oid=LIGHT_OID),
                    "output": {
                        "type": "object",
                        "field": [{
                            "name": "property",
                            "schema": {
                                "type": "string"
                            }
                        }, {
                            "name": "value",
                            "schema": {
                                "type": "integer"
                            }
                        }]
                    }
                },
                "write_link": {
                    "href": "/devices/{oid}/properties/color".format(oid=LIGHT_OID),
                    "input": {
                        "type": "object",
                        "field": [{
                            "name": "value",
                            "schema": {
                                "type": "integer"
                            }
                        }, {
                            "name": "blink",
                            "schema": {
                                "type": "boolean"
                            }
                        }]
                    },
                    "output": {
                        "type": "object",
                        "field": [{
                            "name": "success",
                            "schema": {
                                "type": "boolean"
                            }
                        }]
                    }
                }
            }],
            "actions": [],
            "events": []
        }]
    }

    return JsonResponse(data=td, status=200)
