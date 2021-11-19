# Serverless Test

Example of serverless test automatic post-deployment API testing

## Description

This project shows how to configure and run automated json REST API tests on a deployed API.
The example will run on AWS.

Here you have some useful documentation links:
- https://www.serverless.com/blog/serverless-test-framework
- https://www.serverless.com/framework/docs/guides/testing

## Steps

1. `serverless` (configure your serverless account, required to pass the tests)
2. `serverless deploy`
3. `serverless test`

## Info

- `serverless.yml`: API definition
- `serverless.test.yml`: API tests definition
