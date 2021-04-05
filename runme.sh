timestamp=`date +"%Y-%m-%d"`

./bbmain2021.py > reports/output.csv
./sort.py
cp -rf reports/${timestamp}.csv reports/latest.csv
