#!/bin/bash
 cd "`dirname "$0"`"
 cd ..
 
 mkdir -p build
 cd build
 [ -e _resources ] && rm -rf *
 cd ..
 zim --export \
   --format=html --template=scripts/templates/zim-essnine-theme.html \
   --output=./../website --index-page=sitemap src/

  cd ../../website
  git add .
  git commit -m "Automated website build"
  git push origin main
