#!/usr/bin/env bash
# Navid-S-B
# Shell script to build on the lambda_function.zip 
# in my local library.

virtualenv -p /usr/bin/python3.7 temp_soup
source temp_soup/bin/activate
pip install beautifulsoup4
pip install requests
cp lambda_function_requests.py temp_soup/lib/python3.7/site-packages/
cd temp_soup/lib/python3.7/site-packages/
zip -r9 lambda_function_requests.zip *
mv lambda_function_requests.zip /Users/tom/Desktop/Fullproof/Full_Project/fullproof/backend_scripts/ELAFunction
cd /Users/tom/Desktop/Fullproof/Full_Project/fullproof/backend_scripts/ELAFunction
rm -r temp_soup