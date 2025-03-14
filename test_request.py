import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "UsingIP": 1, "LongURL": 0, "ShortURL": 1, "Symbol@": -1,
    "Redirecting//": 1, "PrefixSuffix-": 0, "SubDomains": 1,
    "HTTPS": -1, "DomainRegLen": 1, "Favicon": -1, "NonStdPort": 0,
    "HTTPSDomainURL": 1, "RequestURL": -1, "AnchorURL": 0,
    "LinksInScriptTags": 1, "ServerFormHandler": -1, "InfoEmail": 1,
    "AbnormalURL": 0, "WebsiteForwarding": 1, "StatusBarCust": -1,
    "DisableRightClick": 1, "UsingPopupWindow": 0, "IframeRedirection": -1,
    "AgeofDomain": 1, "DNSRecording": 0, "WebsiteTraffic": -1,
    "PageRank": 1, "GoogleIndex": 0, "LinksPointingToPage": -1, "StatsReport": 1
}

response = requests.post(url, json=data)
print(response.json())
