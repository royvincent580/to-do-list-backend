#!/usr/bin/env python3
"""
Script to ensure migrations run on Render deployment
"""
import os
from flask import Flask
from flask_migrate import upgrade
from flaskr import create_app

def deploy():
    """Run deployment tasks."""
    app = create_app()
    
    with app.app_context():
        # Create database tables
        upgrade()

if __name__ == '__main__':
    deploy()