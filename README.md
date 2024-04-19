# Trippy

Trippy is a one-stop solution for a travel assistant that not only plans trips but introduces people for the user to travel with as per their common preferecnes.

# Getting started

- Install Poetry

```
curl -sSL https://install.python-poetry.org | python3 -
```

- Add Poetry's bin directory in your `PATH` environment variable as prompted in the terminal. Example:

```
export export PATH="/Users/atishayjain/.local/bin:$PATH"
```

- Create virtual environment and install all the required dependencies

```
poetry install
```

- Create a .env file in the src directory with the required API keys

```
cd ./src
nano .env
```

```
export RAPIDAPI_API_KEY="{GET THE API KEY}"
export GEMINI_API_KEY="{GET THE API KEY}"
export SERPAPI_API_KEY="{GET THE API KEY}"
```

```
source .env
```
