from marshmallow import Schema, fields, validate


class PlainUserSchema(Schema):
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
            validate.Length(min=8, max=128),
            validate.Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)', error='Password must contain at least one lowercase letter, one uppercase letter, and one digit')
        ]
    )


class PlainSignInSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=120))
    password = fields.Str(required=True, validate=validate.Length(min=1, max=128))


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True, validate=validate.Range(min=1))
    name = fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, max=20),
            validate.Regexp(r'^[a-zA-Z0-9\s_-]+$', error='Tag name must contain only letters, numbers, spaces, underscores, and hyphens')
        ]
    )


class PlainTaskSchema(Schema):
    id = fields.Int(dump_only=True, validate=validate.Range(min=1))
    title = fields.Str(
        required=True,
        validate=[
            validate.Length(min=1, max=40),
            validate.Regexp(r'^[a-zA-Z0-9\s.,!?_-]+$', error='Title contains invalid characters')
        ]
    )
    content = fields.Str(
        required=True,
        validate=validate.Length(min=1, max=600)
    )
    status = fields.Str(
        validate=validate.OneOf(["PENDING", "IN_PROGRESS", "COMPLETED"]), 
        required=True
    )
    created_at = fields.DateTime(dump_only=True, data_key="createdAt")
