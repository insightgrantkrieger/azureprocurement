#!/usr/bin/env python3
"""
This script will re-build the database.
It will drop the tables first, so run with care.
"""

from lib.database import Base, engine

print("Dropping and Creating database tables...")
Base.metadata.drop_all(bind=engine, checkfirst=True)
Base.metadata.create_all(bind=engine)
print("Database tables created!")
