# FastAPI Project for Hash Codes

This project utilizes FastAPI to receive requests and generate hash codes in response. The application is hosted on AWS.

## Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Endpoints](#endpoints)
- [Deployment on AWS](#deployment-on-aws)
- [Contribute](#contribute)

## Description

This FastAPI application provides an API to receive text and generate different types of hash codes, such as MD5, SHA-1, SHA-256, and more.

## Features

- Hash code generation for the provided text.
- Hash code generation for files and multiple text.
- Supports various hash algorithms, including MD5, SHA-1, SHA-256, etc.
- Deployment on AWS for remote access.

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/your_username/your_project.git
    cd your_project
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate   # For Windows: venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. Run the FastAPI application:

    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```

2. Access the API at [http://localhost:8000](http://localhost:8000) and use the specified endpoints.

## Endpoints

- `/hash/algorithm/{algorithmStr}/value/{valueStr}`: Generate a hash code for the provided text using the specified algorithm.
- `/hash/algorithm/{algorithmStr}/value/{valueStr}/salt/{saltStr}`: Generate a hash code, of the value provided using the hash algorithm selected and adding salt before hasing.
- `/hash/algorithm/{algorithmStr}/value/{valueStr}/pepper/{pepperStr}`: Generate a hash code, of the value provided using the hash algorithm selected and adding peper after hasing.
- `/hash/compare/algorithm/{algorithmStr}/value/{valueStr}/hash/{hashStr}`: Return True if the hash is equal to the value hashed using the algorithm selected otherwise return False.
- `/hash/compare/algorithm/{algorithmStr}/salt/{saltStr}value/{valueStr}/hash/{hashStr}`: Compare Hash adding salt", description="Return True if the hash is equal to the value hashed using the algorithm selected and adding salt otherwise return False.
- `/hash/compare/algorithm/{algorithmStr}/pepper/{pepperStr}value/{valueStr}/hash/{hashStr}`: Return True if the hash is equal to the value hashed using the algorithm selected and adding pepper otherwise return False.
- `/hash/multiple/algorithm/{algorithmStr}`: Return a list of hash using the algorithm selected.
- `/hash/multiple/algorithm/{algorithmStr}/salt/{saltStr}`: Return a list of hash using the algorithm selected adding salt before hasing.
- `/hash/multiple/algorithm/{algorithmStr}/pepper/{pepperStr}`: Return a list of hash using the algorithm selected and adding pepper after hasing.
- `/hash/multiple/file/algorithm/{algorithmStr}`: Return the hash of the File provided using the algorithm selected.

    Example usage:

    ```bash
    curl -X GET "http://localhost:8000/hash/algorithm/md5/value/hello"
    ```

## Deployment on AWS

This api is depoid in AWS in [http://localhost:8000](http://16.170.244.5:8000/)].

Documentation in [Api Docs](http://16.170.244.5:8000/docs)

## Contribute

If you wish to contribute to this project, we welcome collaborations! 
