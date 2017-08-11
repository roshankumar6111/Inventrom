import requests
import json

tracking_number = input("Enter the tracking_number")


data = requests.post('https://www.fedex.com/trackingCal/track', data={
    'data': json.dumps({
        'TrackPackagesRequest': {
            'appType': 'wtrk',
            'uniqueKey': '',
            'processingParameters': {
                'anonymousTransaction': True,
                'clientId': 'WTRK',
                'returnDetailedErrors': True,
                'returnLocalizedDateTime': False
            },
            'trackingInfoList': [{
                'trackNumberInfo': {
                    'trackingNumber': tracking_number,
                    'trackingQualifier': '',
                    'trackingCarrier': ''
                }
            }]
        }
    }),
    'action': 'trackpackages',
    'locale': 'en_US',
    'format': 'json',
    'version': 99
}).json()

for printdata in data['TrackPackagesResponse']['packageList']:
    row_array={"tracking no":printdata['trackingNbr'],"ship date":printdata['shipDt'],"status":printdata['keyStatus'],"scheduled delivery":printdata['statusWithDetails']}

print (json.dumps(row_array, indent=4))
