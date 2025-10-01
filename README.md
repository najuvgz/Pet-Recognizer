# Pet Recognizer

This is a machine learning project, the goal is to make an streamlit app where u can find out if ur pet is a dog or a cat

## Structure

The project is organized as follows:

- **`src/app.py`** → Main Python script where your project will run.
- **`src/explore.ipynb`** → Notebook for exploration and testing. Once exploration is complete, migrate the clean code to `app.py`.
- **`src/utils.py`** → Auxiliary functions, such as database connection.
- **`requirements.txt`** → List of required Python packages.
- **`models/`** → Will contain your SQLAlchemy model classes.
- **`data/`** → Stores datasets at different stages:
  - **`data/raw/`** → Raw data.
  - **`data/interim/`** → Temporarily transformed data.
  - **`data/processed/`** → Data ready for analysis.




## 💻 Local Setup 

**Prerequisites**

Make sure you have Python 3.11+ installed on your machine. You will also need pip to install the Python packages.

**Installation**

Clone the project repository to your local machine.

Navigate to the project directory and install the required Python packages:

```bash
pip install -r requirements.txt
```



## Running the Application

To run the application, execute the this command inside the terminal

```bash
streamlit run src/app.py
```



