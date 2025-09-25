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
    tag_id = fields.Int(
        required=True, 
        load_only=True, 
        data_key="tagId",
        validate=validate.Range(min=1, error='Tag ID must be a positive integer')
    )
    tags = fields.List(fields.Nested("TagSchema"), dump_only=True)


class TaskTagSchema(Schema):
    id = fields.Int(dump_only=True, validate=validate.Range(min=1))
    task_id = fields.Int(required=True, validate=validate.Range(min=1, error='Task ID must be a positive integer'))
    tag_id = fields.Int(required=True, validate=validate.Range(min=1, error='Tag ID must be a positive integer'))
    priority = fields.Str(
        validate=validate.OneOf(["low", "medium", "high"], error='Priority must be low, medium, or high'), 
        missing="medium"
    )
    assigned_at = fields.DateTime(dump_only=True)


class UpdateTaskSchema(Schema):
    title = fields.Str(
        validate=[
            validate.Length(min=1, max=40),
            validate.Regexp(r'^[a-zA-Z0-9\s.,!?_-]+$', error='Title contains invalid characters')
        ]
    )
    content = fields.Str(validate=validate.Length(min=1, max=600))
    status = fields.Str(validate=validate.OneOf(["PENDING", "IN_PROGRESS", "COMPLETED"]))
    tag_id = fields.Int(
        validate=validate.Range(min=1, error='Tag ID must be a positive integer'),
        data_key="tagId"
    )


class AdminSchema(Schema):
    id = fields.Int(dump_only=True, validate=validate.Range(min=1))
    username = fields.Str(
        required=True,
        validate=[
            validate.Length(min=3, max=20),
            validate.Regexp(r'^[a-zA-Z0-9_]+$', error='Username must contain only letters, numbers, and underscores')
        ]
    )
    email = fields.Email(required=True, validate=validate.Length(max=120))
    password = fields.Str(
        required=True, 
        load_only=True,
        validate=[
            validate.Length(min=8, max=255),
            validate.Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', error='Password must contain at least one lowercase letter, one uppercase letter, and one digit')
        ]
    )


class AdminSignInSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=120))
    password = fields.Str(required=True, validate=validate.Length(min=1, max=255))


class TagUpdateSchema(Schema):
    name = fields.Str(
        validate=[
            validate.Length(min=1, max=20),
            validate.Regexp(r'^[a-zA-Z0-9\s_-]+$', error='Tag name must contain only letters, numbers, spaces, underscores, and hyphens')
        ]
    )


class UserUpdateSchema(Schema):
    username = fields.Str(
        validate=[
            validate.Length(min=3, max=20),
            validate.Regexp(r'^[a-zA-Z0-9_]+$', error='Username must contain only letters, numbers, and underscores')
        ]
    )
    email = fields.Email(validate=validate.Length(max=120))
    password = fields.Str(
        load_only=True,
        validate=[
            validate.Length(min=8, max=128),
            validate.Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', error='Password must contain at least one lowercase letter, one uppercase letter, and one digit')
        ]
    )


class UserTaskSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=120))
    role = fields.Str(
        validate=validate.OneOf(["collaborator", "viewer"], error='Role must be either collaborator or viewer'), 
        missing="collaborator"
    )
