#!/bin/bash
set -e

coverage run -m unittest discover
coverage report -m --include=t3* | tee ./tmp/coverage-report

echo -e "\nSource files with no test coverage:"
echo -e "---------------------------------------"
# ./tmp/covered-files should contain each line of the the coverage report output
# beginning with the string "t3", discarding each character from the first space
# onward
cat ./tmp/coverage-report | grep ^t3 | sed 's/ .*//' > ./tmp/covered-files
# ./tmp/all-source-files should contain the relative path to every .py file 
# under this directory.
find t3 -name "*.py" > ./tmp/all-source-files
# ./tmp/uncovered files should contain all filenames not in ./tmp/covered-files
grep -Fxv -f ./tmp/covered-files ./tmp/all-source-files | tee ./tmp/uncovered-files
echo -e "----------------------------------------\n"
