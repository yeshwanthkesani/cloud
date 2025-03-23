# Local Setup

We haven't confirmed the following.
Avoid creating branches, fork then clone and work in the main branch.


# RealityStream - Local Setup Guide

## Prerequisites

Ensure you have the following installed on your system before proceeding:
- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Virtualenv](https://docs.python.org/3/library/venv.html)

## Setting Up the Project Locally

### 1. Fork in Github, then use GitHub Desktop to clone the Repository



### 2. Navigate to the Project Directory

```bash
cd cloud
```

### 3. Avoid creating a new Branch

Simply work in a fork

### 4. Create a Virtual Environment

Create a virtual environment to manage dependencies properly.

```bash
python3 -m venv ./venv
```
#### OR

if using vscode, please setup venv through default approach of selecting python environment in kernel options and then the environment should be able to find requieremnts.txt located in the models folder.

Activate the virtual environment:

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 5. Install Dependencies

After activating the virtual environment, install the required dependencies:

```bash
pip3 install -r path/to/models/requirements.txt
```

### 6. Mac Users - Install libomp

Mac users may encounter errors related to OpenMP when running certain ML/AI models. This is because macOS does not include OpenMP support by default. To resolve this, install libomp:

```bash
brew install libomp
```

If you encounter issues after installation, try running:

```bash
export DYLD_LIBRARY_PATH="/opt/homebrew/opt/libomp/lib:$DYLD_LIBRARY_PATH"
```

### 7. Updating Dependencies

Whenever you add new modules or packages, update requirements.txt using:

```bash
pip freeze > requirements.txt
```

## Git Workflow

To ensure a smooth development process, follow this Git workflow:

### 1. Always Pull Latest Changes Before Starting Development

Before making any changes, pull the latest updates from the remote repository to avoid merge conflicts.

```bash
git pull origin main  # Or replace `main` with your active branch
```

### 2. Add Your Changes

After modifying files, add them to staging:

```bash
git add .  # Adds all modified files
```

Alternatively, add specific files:

```bash
git add filename.py
```

### 3. Commit Your Changes with a Meaningful Message

```bash
git commit -m "<your meaningful commit message>"
```

Example:
```bash
git commit -m "Added user authentication feature"
```

### 4. Push Changes to Remote Repository

Push your changes to the remote repository.

```bash
git push origin feature_branch_name
```

### 5. Create a Pull Request (PR)

After pushing your changes, go to the repository on GitHub and create a Pull Request (PR) to merge your branch into main or develop.

## Additional Notes

- Always pull the latest changes before merging:
  ```bash
  git pull origin main
  ```
- If you switch branches, always activate the virtual environment again.
- If you face dependency issues, try reinstalling requirements:
  ```bash
  pip install --upgrade -r requirements.txt
  ```





### Prerequisites
- Git
- Python 3.8+
- pip (Python package manager)
- Homebrew (for macOS users)

### Initial Setup

1. Clone the repository
   ```bash
   git clone https://github.com/cvnad1/RealityStream.git
   ```

2. Navigate to the project directory
   ```bash
   cd RealityStream
   ```

3. Create a feature branch
   ```bash
   git checkout -b feature_branch
   ```
   Replace `feature_branch` with a descriptive name related to your work (e.g., `user-authentication`, `video-streaming`).

4. Create a virtual environment
   ```bash
   python3 -m venv ./venv
   ```

5. Activate the virtual environment
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

6. For macOS users: Install libomp
   ```bash
   brew install libomp
   ```
   **Note:** libomp is required for certain machine learning libraries. Some users might encounter an error related to OpenMP when installing dependencies. This step preemptively solves that issue.

7. Install required dependencies
   ```bash
   pip3 install -r requirements.txt
   ```

## Git Workflow

### Before Starting Development

Always pull the latest changes from the main branch before starting your work:

```bash
git pull origin main
```

### Adding New Packages

If you install new Python packages:

1. Add them to your development environment:
   ```bash
   pip3 install package_name
   ```

2. Update the requirements.txt file:
   ```bash
   pip freeze > requirements.txt
   ```

### Committing Changes

1. Check the status of your changes:
   ```bash
   git status
   ```

2. Add your changes to the staging area:
   ```bash
   git add .
   ```
   Or to add specific files:
   ```bash
   git add file_name
   ```

3. Commit your changes with a descriptive message:
   ```bash
   git commit -m "Add feature X" 
   ```

4. Push your changes to the remote repository:
   ```bash
   git push origin feature_branch
   ```

## TO DO

TO DO: Add these to a requirements file and document.
Try to reduce to only the ones needed.

      import os
      import pandas as pd
      import yaml
      import requests

      import pandas as pd
      import regex as re
      import os
      import pandas as pd
      import numpy as np
      import matplotlib.pyplot as plt
      import pickle
      import yaml
      import requests
      #from collections import OrderedDict # Effort to retain incoming yaml order rather than alphabetizing.
      from sklearn.ensemble import RandomForestClassifier
      from sklearn.linear_model import LogisticRegression
      from sklearn.svm import SVC
      from sklearn.neural_network import MLPClassifier
      from sklearn.metrics import accuracy_score, classification_report, roc_curve, roc_auc_score
      from imblearn.over_sampling import SMOTE
      from sklearn.impute import SimpleImputer
      from sklearn.model_selection import GridSearchCV
      from sklearn.model_selection import train_test_split
      from sklearn.preprocessing import StandardScaler

      // This probably includes scipy
      pip install imbalanced-learn

      import xgboost as xgb
      from xgboost import plot_importance
      import seaborn as sns
      import scipy.stats as stats


### Creating a Pull Request

After pushing your changes, go to the GitHub repository and create a pull request.
