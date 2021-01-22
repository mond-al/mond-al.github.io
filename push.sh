timestamp=`date +%Y%m%d%H%M`

bundle exec jekyll build
cd output
git add --all .
git commit -m "updating site $timestamp"
git push https://github.com/mond-al/mond-al.github.io
cd ..