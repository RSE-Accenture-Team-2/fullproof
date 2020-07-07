#!/usr/bin/sh
# Navid-S-B
# Shell script to build on the lambda_function.zip 
# in my local library.

virtualenv -p /usr/bin/python3.8 temp_soup
source temp_soup/bin/activate
pip3 install beautifulsoup4
pip3 install lxml
pip3 install google-search-results
deactivate
cp lambda_function.py temp_soup/lib/python3.8/site-packages/
cp serpapi_script.py temp_soup/lib/python3.8/site-packages/
cp error_return_script.py temp_soup/lib/python3.8/site-packages/
cd temp_soup/lib/python3.8/site-packages/
zip -r9 lambda_function.zip *
mv lambda_function.zip /home/navid_b/fullproof/backend_scripts
cd /home/navid_b/fullproof/backend_scripts
rm -r temp_soup