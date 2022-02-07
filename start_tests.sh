#!/bin/bash

logs="logs/test_runs"
rm $logs

if [ $# -eq 0 ]; then
	echo "Running tests once..."
	pkill tor
	pkill firefox.real
	/usr/bin/python3 -m tests.sqlite_tests 2> >(tee -a $logs)
	exit 0
fi

if [ $1 == "fail" ]; then
	echo "Running tests until failure..."
	while ! grep "FAILED" $logs; do
		pkill tor
		pkill firefox.real
		/usr/bin/python3 -m tests.sqlite_tests 2> >(tee -a $logs)
	done
fi
