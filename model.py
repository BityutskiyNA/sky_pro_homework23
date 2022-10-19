import function_query as funct

import function_query as functions
from marshmallow import Schema, fields, validates_schema, ValidationError
import function_query

VALID_CMD_Param = {
    'filter',
    'map',
    'unique',
    'sort',
    'limit',
}

class RequestParams(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)


    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        if values['cmd1'] not in VALID_CMD_Param:
            raise ValidationError
        if values['cmd2'] not in VALID_CMD_Param:
            raise ValidationError

        return values