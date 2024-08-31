# This directory includes the AWS cloud formation template for the infrastructure

Commands:

```bash
 aws cloudformation create-stack --stack-name App-Stack --template-body file://temlpate.yml --capabilities CAPABILITY_NAMED_IAM --profile embeddedinn
```

```bash
aws ecr get-login-password --region us-east-2 --profile embeddedinn | docker login --username AWS --password-stdin <accountID>.dkr.ecr.us-east-2.amazonaws.com
```

```bash
docker push <accountID>.dkr.ecr.us-east-2.amazonaws.com/app_repository:latest
```
