timestamp=`date +%Y%m%d%H%M`
echo "-------------------------------------------------source upload [1] -------------------------------------------------"
git add --all .
git commit -m "updating site $timestamp ${1}"
git push
echo "-------------------------------------------------source compile [2]-------------------------------------------------"
bundle exec jekyll build
cd ../mond-al.github.io
git add --all .
git commit -m "updating site $timestamp ${1}"
echo "-------------------------------------------------ouput upload Strart-------------------------------------------------"
git push https://github.com/mond-al/mond-al.github.io
cd ../mond-al.github.io_maker/
./update.sh
