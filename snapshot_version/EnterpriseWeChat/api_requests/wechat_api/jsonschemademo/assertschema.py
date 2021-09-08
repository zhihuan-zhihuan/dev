#!/usr/bin/evn python
# -*- coding=utf8 -*-

import jsonschema


class Validator(object):
    def __init__(self, schema):
        self.schema = schema
        checker = jsonschema.FormatChecker()
        self.validator = jsonschema.validators.Draft6Validator(
            self.schema, format_checker=checker)

    def validate_request_params(self, data):
        try:
            self.validator.validate(data)
        except jsonschema.ValidationError as ex:
            field_name = "-".join(ex.absolute_path)
            print ("Validate Error, flied[%s], error msg: %s" %
                   (field_name, ex.message))
            # detail_info = "([%s]: %s) " % (field_name, ex.message)
            # raise expt.JsonSchemaValidateFailed(detail=detail_info)

    def validate_data(self, data):
        try:
            self.validator.validate(data)
        except jsonschema.ValidationError as ex:
            field_name = "-".join(ex.absolute_path)
            print("Validate Error, flied[%s], error msg: %s" %
                  (field_name, ex.message))
            # err_dict = {field_name: [ex.message]}
            # raise expt.JsonSchemaValidateFailed(detail=err_dict)


if __name__ == '__main__':
    schema_format = {
        "type": "object",
        "title": "empty object",
        "properties": {
            "name": {
                "type": "string",
                "minLength": 3,
                "maxLength": 6,
                "description": "name test"
            },
            "service1": {
                "type": "object",
                "properties": {
                    "age": {
                        "type": "integer",
                        "description": "1",
                        "minimum": 16,
                        "maximum": 30,
                        "default": "18",
                        "exclusiveMinimum": 16,
                        "exclusiveMaximum": 30
                    },
                    "service2": {
                        "type": "object",
                        "properties": {
                            "service3": {
                                "type": "object",
                                "properties": {
                                    "service4": {
                                        "type": "string"
                                    }
                                },
                                "required": [
                                    "service4"
                                ]
                            }
                        },
                        "description": "gender test",
                        "required": [
                            "service3"
                        ]
                    }
                },
                "description": "service test",
                "required": [
                    "age",
                    "service2"
                ]
            },
            "list": {
                "type": "array",
                "items": {
                    "type": "string",
                    "description": "list item test"
                },
                "description": "list test"
            }
        },
        "required": [
            "name",
            "service1",
            "list"
        ]
    }

    data = {
        "name": u"张三123",
        "service1": {
            "age": 17,
            "service2": {
                "service3": {
                    "service4": 123
                }

            }
        },
        "list": ["123", "45"],
    }
    validator = Validator(schema_format)
    validator.validate_data(data=data)