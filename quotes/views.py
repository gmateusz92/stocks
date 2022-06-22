from django.shortcuts import render

def home(request):
    import requests
    import json

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_297824bdbb614725932cf143763397a7")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})