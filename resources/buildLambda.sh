#!/bin/bash

rm -rf package
mkdir package
cd package
pip3 install charset-normalizer requests -t .

cp ../cfn_lambda.py .
zip -r9 cfn_lambda.zip *

aws s3 mb s3://nttdatacfpy
aws s3 cp cfn_lambda.zip s3://nttdatacfpy/
