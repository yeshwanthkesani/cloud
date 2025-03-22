# Local Setup

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

After pushing your changes, go to the GitHub repository and create a pull request to merge your feature branch into the main branch.

## Contributing

1. Always work on a feature branch, never directly on main
2. Keep commits small and focused
3. Write clear commit messages
4. Update documentation as needed
5. Make sure all tests pass before submitting a pull request
