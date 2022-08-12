
# Python Assessment

An API service to return the current age given a valid date of birth.

## API Reference


#### Get age

```
  GET /v1/api/assessment/howold/
```

| Parameter | Type   | Description                                 |
|:----------|:-------|:--------------------------------------------|
| `dob`     | `date` | **Required**. The date to calculate against |


## Authors

- [@Ajawu](https://www.github.com/ajawu)


## Demo

https://age-tracker.herokuapp.com/

## Run Locally

Clone the project

```bash
  git clone git@github.com:ajawu/python-assessment.git
```

Go to the project directory

```bash
  cd python-assessment
```

Install dependencies

```bash
  poetry install
```

Activate virtual environment

```bash
  poetry shell
```

Start the server

```bash
  python src/manage.py runserver
```
