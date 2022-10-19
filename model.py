from typing import Iterable

from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD_Param: Iterable[str] = {
    'filter',
    'map',
    'unique',
    'sort',
    'limit',
    'regex',
}


class RequestParams(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)
    cmd2 = fields.Str(required=True)
    value2 = fields.Str(required=True)


    @validates_schema
    def validate_cmd_params(self, values: dict[str, str], *args, **kwargs) -> dict:
        if values['cmd1'] not in VALID_CMD_Param:
            raise ValidationError("Не корректная команда")
        if values['cmd2'] not in VALID_CMD_Param:
            raise ValidationError("Не корректная команда")

        return values
