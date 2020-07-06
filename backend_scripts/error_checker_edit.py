# Navid-S-B
# Error checking functions
# 6-07-2020

def url_error(event):

    # Checks for inputted google search links
    if 'google' in event['image_url']:
        return True
    else:
        return False

