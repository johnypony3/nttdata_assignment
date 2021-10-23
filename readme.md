Purpose: nttdatas python/cloudformation assignment

```
Assignment:
**Python/Cloudformation:**

Develop an independent Cloudformation template which takes State/Province as a parameter and exports the unix time for the given State/province in Europe in the stack. Present your findings and challenges once assignment is done.
Goal : To understand if the candidate can read documentation and implement them in real projects.

Guidance : → Make use of Python and AWS Cloudformation(YAML Syntax) → Unix Time for London can be found by using the world api. Below is an example of open available API which we can use to get the unix time for London

Sample Curl: curl “http://worldtimeapi.org/api/timezone/Europe/London.txt"

Sample Output: abbreviation: GMT datetime: 2019-03-08T09:01:01.258877+00:00 day_of_week: 5 day_of_year: 67 dst: false dst_from: dst_until: timezone: Europe/London unixtime: 1552035661 utc_offset: +00:00

→ The Unix time can be parsed from the Sample output for a given province/state → There is no Standard Cloudformation resource for finding unix time, hence the developer needs to make use of cloudformation custom resources to achieve the goal.
```

Repo overview:

- template.yml: cloudformation template
- cfn_lambda.py: lambda python code
- resources/buildLambda.sh: shell script to build lambda zip file and upload to s3

Workflow:

1. `resources/buildLambda.sh`
    - any time the lambda contents need to be updated
2. `aws cloudformation deploy --stack-name nttdata --template-file template.yml --capabilities CAPABILITY_NAMED_IAM --parameter-overrides TimeZone=America/Boise`
    - deploy stack
    - specify the timezone from here: http://worldtimeapi.org/api/timezone
3. `aws cloudformation delete-stack --stack-name nttdata`
    - destroy stack
4. `aws cloudformation describe-stacks --stack-name nttdata`
    - get stack info

Techinical overview:

1. cloudformation:
    - Resources
        1. GetTimeInfo lambda function
        2. GetTimeInfoRole role for lambda function
        3. Custom resource to interact with lambda and customer
    - Outputs
        1. Time zone, current information
        2. Unix time, current information
    - Parameters
        1. Time zone, full string
2. cloudformation passes information to lambda by setting an environment variable in the lambda function

Result:

1. TimeInformation: abbreviation: BST datetime: 2021-10-23T18:25:51.459325+01:00 day_of_week: 6 day_of_year: 296 dst: true dst_from: 2021-03-28T01:00:00+00:00 dst_until: 2021-10-31T01:00:00+00:00 timezone: Europe/London unixtime: 1635009951 utc_offset: +01:00