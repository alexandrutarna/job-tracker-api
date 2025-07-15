import sys
import os

# Add parent directory of 'app' to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base
from app.models import Job

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("Done.")
