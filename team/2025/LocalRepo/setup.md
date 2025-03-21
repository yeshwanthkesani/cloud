# RealityStream - Local Setup Guide

## Prerequisites

Ensure you have the following installed on your system before proceeding:
- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/downloads/)
- [Virtualenv](https://docs.python.org/3/library/venv.html)

## Setting Up the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/{username}/cloud.git
```

### 2. Navigate to the Project Directory

```bash
cd cloud
```

### 3. Create a New Feature Branch

Always create a new branch for development to keep the main or develop branch clean.

```bash
git checkout -b feature_branch_name
```

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
