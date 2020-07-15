# Navid-S-B
# 6-07-2020
"""
The lambda function handler is reponsible 
for executing the error_return_script.py and 
serpapi_script.py in the background.
.
"""
import error_return_script as ers

def lambda_handler(event, context):
    
    # If the url is a google search link
    if ers.url_error(event):
        return ers.url_error_return(event)
    else:
        return ers.execute_code(event)
