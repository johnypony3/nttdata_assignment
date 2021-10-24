FROM centos:7

RUN yum install -y zip unzip git python3

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install

RUN pip3 install cloudformation-cli cloudformation-cli-java-plugin \
    cloudformation-cli-go-plugin cloudformation-cli-python-plugin \
    cloudformation-cli-typescript-plugin 'jsonschema<4.0'