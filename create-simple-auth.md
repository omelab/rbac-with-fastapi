## Write a simple authentication

Let's go through the step-by-step process of setting up a FastAPI project with user registration, login, PostgreSQL integration, and Alembic for database migrations.

### Step 1: Create a virtual environment (Optional but recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

### Step 2: Install required packages

```bash
pip install fastapi uvicorn sqlalchemy 'databases[postgresql]' passlib alembic python-dotenv
```

if you have an error like  zsh: no matches found: databases[asyncpg]

It seems like your shell (zsh) is interpreting the square brackets as a globbing pattern, and since there are no matches, it's giving you the "no matches found" error. To install the databases[asyncpg] package using pip, you can either escape the square brackets or use quotes to prevent the shell from interpreting them as a globbing pattern

1. Escape Square Brackets:
```bash
pip install databases\[asyncpg\]
```

2. Use Quotes:
```bash
pip install 'databases[asyncpg]'
```

### Step 3: Create the project structure

Create the necessary directories and files as described in the previous responses. You can use the provided directory structure and code snippets.


### Step 4: Database Configuration

Create a PostgreSQL database and update the .env file with your database URL. For example:

```bash
# .env
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```


### Step 5: Initialize Alembic and Create Initial Migration

```bash
# Initialize Alembic
alembic init alembic

# Modify alembic.ini to set the database URL

# Create an initial migration
alembic revision --autogenerate -m "Initial migration"
```

### Step 6: Run Initial Migration
```bash
alembic upgrade head
```


### Step 7: Code Modifications

Add the provided code snippets to the respective files in your project structure. Make sure to replace placeholders like your-secret-key and database connection details with your actual values.

### Step 8: Run the FastAPI application

```bash
# Run the FastAPI application
uvicorn app.main:app --reload
```