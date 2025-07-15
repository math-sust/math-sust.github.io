#!/usr/bin/env sh
python updateCourses.py
# abort on errors
set -e
echo "courses compiled"
# build
/usr/local/n/versions/node/14.19.0/bin/npm run build
echo "npm build finished"
# navigate into the build output directory
cd dist
mv /var/www/html /var/www/html_$(date "+%Y.%m.%d-%H.%M.%S")
echo "backup created"
mkdir /var/www/html
cp -R * /var/www/html
echo "done"
