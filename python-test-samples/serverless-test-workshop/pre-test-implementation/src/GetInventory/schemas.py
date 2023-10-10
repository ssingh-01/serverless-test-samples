# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

OUTPUT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "object",
    "title": "Sample Output schema",
    "description": "The root schema comprises the entire JSON document of the Return Schema.",
    "examples": [{"statusCode": 200, "body": "OK", "unicorn_list":[] }],
    "required": ["statusCode", "body"],
    "properties": {
        "statusCode": {
            "type": "integer",
            "title": "HTTP Status Code",
            "examples": [200,401,500]
        },
        "body": {
            "type": "string",
            "title": "The return message",
            "examples": ["OK","Error"]
        }
    }
}