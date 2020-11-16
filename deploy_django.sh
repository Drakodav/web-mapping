#!/bin/bash

# shh in our server
echo "########### connecting to server and run commands in sequence ###########"
sudo ssh -i web-mapping_key.pem azureuser@40.121.42.196 \
'
git clone https://github.com/Drakodav/web-mapping.git;
sudo find web-mapping/ -type f -iname "*.sh" -exec chmod +x {} \;
cd web-mapping/frontend;
npm install;
npm run build;
cd ../;
sudo ./django.sh;
cd ..;
sudo rm -r web-mapping;
'

echo "Cleaning up..."
echo "Finished updating django to latest version"



