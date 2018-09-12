import requests
from ipywidgets import widgets
from IPython.display import display
from os.path import expanduser
import os
import json


def connect_to_queue(button_type='help', disp_input_fields=False, base_url="http://jhell3.pythonanywhere.com"):
    home = expanduser("~")
    config_file = os.path.join(home, ".pyqueue")
    contents = None
    if os.path.isfile(config_file):
        with open(config_file, 'r') as file:
            contents = file.read()

    help_button = widgets.Button(description="Request Help") 
    checkoff_button = widgets.Button(description="Request Checkoff")
    status_text = widgets.Label(value="")
    if contents:
        res = contents.split(',')
        name, kerberos = res[0].strip(), res[1].strip()
        name_field = widgets.Text(description='Name', placeholder='Ben Bitdiddle', value=name)
        kerberos_field = widgets.Text(description='Kerberos', placeholder='benbit', value=kerberos)
    else:
        name_field = widgets.Text(description='Name', placeholder='Ben Bitdiddle')
        kerberos_field = widgets.Text(description='Kerberos', placeholder='benbit')

    queue_button = help_button if button_type == 'help' else checkoff_button

    if disp_input_fields:
        widget_list = [name_field, kerberos_field, queue_button, status_text]
    else:
        widget_list = [queue_button, status_text]

    queue_box = widgets.HBox(widget_list)
    display(queue_box)

    def get_field_values():
        try:
            res = name_field.value.split(' ')
            first_name, last_name = res[0].strip(), res[1].strip()
            kerberos = kerberos_field.value.strip()

            if len(first_name) > 0 and len(last_name) > 0 and len(kerberos) > 0:
                return first_name, last_name, kerberos
            else:
                raise ValueError
        except:
            print("Please enter a first and last name, and a kerberos")
            return None

    def save_config(first_name, last_name, kerberos):
        with open(config_file, 'w') as file:
            file.write(first_name+' '+last_name+','+kerberos)

    def make_help_request(a):
        fields = get_field_values()
        if fields:
            params = {"first_name": fields[0], "last_name": fields[1], "kerberos": fields[2]}
            r = requests.post(base_url+'/queue/help', data=params)
            save_config(fields[0], fields[1], fields[2])
            response = json.loads(r.text)
            status_text.value = response['message']

    def make_checkoff_request(a):
        fields = get_field_values()
        if fields:
            params = {"first_name": fields[0], "last_name": fields[1], "kerberos": fields[2]}
            r = requests.post(base_url+'/queue/checkoff', data=params)
            save_config(fields[0], fields[1], fields[2])
            response = json.loads(r.text)
            status_text.value = response['message']

    help_button.on_click(make_help_request)
    checkoff_button.on_click(make_checkoff_request)
