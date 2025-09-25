from marshmallow import Schema, fields, validate
from flaskr.schemas.plain_schema import (
    PlainSignInSchema,
    PlainTagSchema,
    PlainTaskSchema,
    PlainUserSchema,
)


class UserSchema(PlainUserSchema):
    pass


class SignInSchema(PlainSignInSchema):
    pass


class TagSchema(PlainTagSchema):
    pass


class TaskSchema(PlainTaskSchema):
    tag_name = fields.Str(dump_only=True, data_key="tagName")
    tag_id = fields.Int(required=True, load_only=True, data_key="tagId")
    tags = fields.List(fields.Nested("TagSchema"), dump_only=True)


class TaskTagSchema(Schema):
    id = fields.Int(dump_only=True)
    task_id = fields.Int(required=True)
    tag_id = fields.Int(required=True)
    priority = fields.Str(validate=validate.OneOf(["low", "medium", "high"]), missing="medium")
    assigned_at = fields.DateTime(dump_only=True)


class UpdateTaskSchema(PlainTaskSchema):
    pass


class AdminSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)


class AdminSignInSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(required=True)


class UserTaskSchema(Schema):
    email = fields.Email(required=True)
    role = fields.Str(validate=validate.OneOf(["collaborator", "viewer"]), missing="collaborator")
