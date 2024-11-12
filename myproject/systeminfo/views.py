from django.shortcuts import render

import os
import subprocess
from datetime import datetime
import pytz
from django.http import HttpResponse

def htop_view(request):
   
    name = "Manaswi Kumar"
    

    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    
    
    tz_ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(tz_ist).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3] + " IST"
    
  
    try:
        top_output = subprocess.getoutput("top -b -n 1")
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"
    
 
    html_content = f"""
    <html>
    <head>
        <title>HTop Endpoint</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            pre {{ font-size: 14px; white-space: pre-wrap; }}
        </style>
    </head>
    <body>
        <h1>System Information</h1>
        <p><b>Name:</b> {name}</p>
        <p><b>User:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>TOP output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)

