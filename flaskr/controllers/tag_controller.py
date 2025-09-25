from flask_smorest import abort
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from flaskr.db import db
from flaskr.models.tag_model import TagModel


class TagController:
    @staticmethod
    def get_all():
        try:
            return db.session.execute(select(TagModel).limit(15)).scalars().all()
        except SQLAlchemyError:
            abort(500, message="Internal server error while fetching tags")

    @staticmethod
    def get_by_id(tag_id):
        try:
            return db.session.execute(
                select(TagModel).where(TagModel.id == tag_id)
            ).scalar_one()
        except NoResultFound:
            abort(404, message="Tag not found")
        except SQLAlchemyError:
            abort(500, message="Internal server error while fetching tag")

    @staticmethod
    def create(data):
        try:
            tag_registered = db.session.execute(
                select(TagModel).where(TagModel.name == data["name"])
            ).scalar_one_or_none()

            if tag_registered:
                abort(409, message="Tag already registered")

            new_tag = TagModel(**data)

            db.session.add(new_tag)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while creating tag")
    
    @staticmethod
    def update(data, tag_id):
        try:
            tag = db.session.execute(
                select(TagModel).where(TagModel.id == tag_id)
            ).scalar_one()
            
            for key, value in data.items():
                setattr(tag, key, value)
            
            db.session.commit()
            return tag.to_dict()
        except NoResultFound:
            abort(404, message="Tag not found")
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while updating tag")
    
    @staticmethod
    def patch(data, tag_id):
        try:
            tag = db.session.execute(
                select(TagModel).where(TagModel.id == tag_id)
            ).scalar_one()
            
            # Only update fields that are provided
            for key, value in data.items():
                if hasattr(tag, key):
                    setattr(tag, key, value)
            
            db.session.commit()
            return tag.to_dict()
        except NoResultFound:
            abort(404, message="Tag not found")
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while patching tag")
    
    @staticmethod
    def delete(tag_id):
        try:
            tag = db.session.execute(
                select(TagModel).where(TagModel.id == tag_id)
            ).scalar_one()
            
            db.session.delete(tag)
            db.session.commit()
        except NoResultFound:
            abort(404, message="Tag not found")
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Internal server error while deleting tag")
