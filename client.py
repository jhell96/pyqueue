import requests
from ipywidgets import widgets
from IPython.display import display

def connect_to_queue(first_name, last_name, kerberos, base_url="http://127.0.0.1:5000/"):
    help_button = widgets.Button(description="Request Help") 
    checkoff_button = widgets.Button(description="Request Checkoff")

    display(help_button)
    display(checkoff_button)

    params = {"first_name": first_name, "last_name": last_name, "kerberos": kerberos}

    def make_help_request(a):
        r = requests.post(base_url+'queue/help', data=params)

    def make_checkoff_request(a):
        r = requests.post(base_url+'queue/checkoff', data=params)

    help_button.on_click(make_help_request)
    checkoff_button.on_click(make_checkoff_request)