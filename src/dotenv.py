from dotenv import load_dotenv
from pyprojroot import here
import os

dotenv_path = here() / ".env"
load_dotenv(
    dotenv_path=dotenv_path
)  # this will load the .env file in your project directory root.

# Now, get the environment variable.
DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")
