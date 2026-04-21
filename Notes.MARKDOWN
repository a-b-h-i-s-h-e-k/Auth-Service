## To start a Virtual Enviorment
- python -m venv auth
- . auth/bin/activate

- pip freeze > requirements.txt


Small improvement 

our next upgrade should be:

move SECRET_KEY to .env
prevent users from assigning themselves admin during public registration
use EmailStr validation fully
add refresh tokens later