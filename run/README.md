# Google Cloud Run with CoLab+GitHub

Our guide provides commands for Google Cloud Run service setup with Flask to execute a Jupyter notebook from a GitHub repository.

- **Cmds for Google Cloud** - Creates a new project ID and enables necessary APIs
- **GitHub integration** - Setting up access tokens and webhooks for repository updates
- **Flask application** - Complete code for a web service with a button to trigger notebook execution
- **Security setup** - Storing GitHub tokens securely in Secret Manager
- **Notebook modification** - Adding the GitHub upload functionality to your notebook
- **Deployment** - Commands to deploy the service to Cloud Run
- **Automatic updates** - Setting up webhooks to update when your GitHub repo changes
- **Service account permissions** - Configuring proper access for secure GitHub interactions

The application creates a simple web interface with a button that, when pressed, will:

- Clone your GitHub repository (Later we'll sync when the repo changes instead.)
- Execute the specified notebook
- Push the resulting files to your target repository

The guide also includes options for setting up scheduled executions if you want the notebook to run automatically at specific intervals.

[Our initial code was vibe-promoted with](https://claude.ai/public/artifacts/a3d76132-45f4-4155-aef8-4870adf64f20): Create commands for creating a Google Cloud Run containing Flask and use the resulting project ID to create a website that executes a .ipynb file that resides in a Github repo. Whenever the repo is updated, update the website. The .ipynb file will be triggered by a button on a page and it will push files to another GitHub repo. Set permissions in Google to allow the push from the Google server to occur. Here's the function we use to push the files. (I provided the upload_reports_to_github function from the last step in our Run Models colab.)

TO DO: Let's add a form here where users can enter their Google ProjectID, GitHub repo+token to populate in the commands.

Let's also creat deployment cmds for [Thundercompute.com](https://www.thundercompute.com)

<!--
https://claude.ai/public/artifacts/a3d76132-45f4-4155-aef8-4870adf64f20

Promoted with: Create commands for creating a Google Cloud Run containing Flask and use the resulting project ID to create a website that executes a .ipynb file that resides in a Github repo. Whenever the repo is updated, update the website. The .ipynb file will be triggered by a button on a page and it will push files to another GitHub repo. Set permissions in Google to allow the push from the Google server to occur. Here's the function we use to push the files. (I provided the upload_reports_to_github function from the last step in our Run Models colab.)
-->

## Prerequisites

1. Google Cloud account
2. GitHub account
3. Two GitHub repositories:
   - Source repo: Contains the .ipynb notebook to execute
   - Target repo: Where the generated files will be pushed

## Part 1: Set Up Google Cloud Project

Open a terminal in the folder where your site will reside.

```bash
# Install Google Cloud SDK if not already installed
# https://cloud.google.com/sdk/docs/install

# Initialize gcloud - (2) Create a new configuration, or (1 or 3) use existing.
gcloud init

# If you add a new configuration, you may want to name if different from the project.

modelearth-config

# You'll be prompted to create a project and it will be set as active.
# Here are the equivalent commands;

# Create a new project - change the name as desired
gcloud projects create your-project-id --name="modelearth-run-models"

# Set the project as active
gcloud config set project your-project-id

# You'll likely be advised to update Google Cloud CLI components by running:

gcloud components update

# Get your billing account ID

gcloud billing accounts list

# For the following, you'll be promted to install gcloud Alpha Commands

gcloud alpha billing accounts describe 000000-000000-000000

# The above will fail initially, so
# associate a billing account to your new "modelearth-run-models" project

gcloud billing projects link modelearth-run-models --billing-account=BILLING_ACCOUNT_ID

# TODO: If you don't have a billing account yet, fork this repo and document commands to add it here. Send a PR.

# Enable required APIs
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable cloudscheduler.googleapis.com
gcloud services enable secretmanager.googleapis.com
```

## Part 2: Create GitHub Access Token

1. In your [GitHub account](https://github.com), navigate to Settings (upper right menu)
2. Navigate to Developer settings (lower left) > Personal access tokens. Choose Fine-grained tokens.
3. Create a new Fine-grained token so you can limit to one repo.

<!-- Should we add more specific details on scope/permission settings? -->


## Part 3: Store GitHub Token in Secret Manager

```bash
# Create a secret for the GitHub token
echo -n "your-github-token" | gcloud secrets create github-token --data-file=-

# Grant the Cloud Run service account access to the secret
gcloud secrets add-iam-policy-binding github-token \
    --member="serviceAccount:your-project-id@appspot.gserviceaccount.com" \
    --role="roles/secretmanager.secretAccessor"
```

## Part 4: Create Flask Application

Create a directory for your project and set up the following files:

### `Dockerfile`

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set environment variables
ENV PORT=8080

# Run the application
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
```

### `requirements.txt`

```
flask==2.0.1
gunicorn==20.1.0
nbconvert==6.1.0
nbformat==5.1.3
papermill==2.3.3
ipykernel==6.4.1
requests==2.26.0
google-cloud-secret-manager==2.8.0
gitpython==3.1.24
```

### `app.py`

```python
import os
import tempfile
import subprocess
import requests
import json
from flask import Flask, render_template, request, jsonify
from google.cloud import secretmanager
import git
import papermill as pm
import nbformat
from nbconvert import HTMLExporter

app = Flask(__name__)

# Configuration
SOURCE_REPO_URL = "https://github.com/username/source-repo.git"
TARGET_REPO = "username/target-repo"
NOTEBOOK_PATH = "path/to/notebook.ipynb"

# Get the GitHub token from Secret Manager
def get_github_token():
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{os.environ.get('GOOGLE_CLOUD_PROJECT')}/secrets/github-token/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-notebook', methods=['POST'])
def run_notebook():
    try:
        # Create a temporary directory
        with tempfile.TemporaryDirectory() as temp_dir:
            # Clone the source repository
            repo = git.Repo.clone_from(SOURCE_REPO_URL, temp_dir)
            
            # Path to the notebook in the cloned repo
            notebook_file = os.path.join(temp_dir, NOTEBOOK_PATH)
            
            # Execute the notebook
            output_path = os.path.join(temp_dir, 'output.ipynb')
            pm.execute_notebook(
                notebook_file,
                output_path,
                parameters={}
            )
            
            # Read the executed notebook
            with open(output_path, 'r') as f:
                nb = nbformat.read(f, as_version=4)
            
            # Convert to HTML for display
            html_exporter = HTMLExporter()
            html_data, resources = html_exporter.from_notebook_node(nb)
            
            # The notebook execution will trigger the upload_reports_to_github function
            # which is defined in the notebook itself
            
            return jsonify({
                'status': 'success',
                'message': 'Notebook executed successfully'
            })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle webhook from GitHub to update when the repo changes"""
    try:
        payload = request.json
        if 'ref' in payload and payload['ref'] == 'refs/heads/main':
            # Pull the latest changes
            subprocess.run(["git", "pull"], cwd="/app")
            return jsonify({'status': 'success'})
        return jsonify({'status': 'no action'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
```

### `page.html`

Page.html contains the button that will run our .ipynb file.

[View page.html](page.html)

## Part 5: Create Modified Notebook 

Create a modified version of your notebook that incorporates the upload function:

```python
# Add this to the beginning of your notebook as a cell:
import os
import requests
from google.cloud import secretmanager

# Get the GitHub token from Secret Manager
def get_github_token():
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{os.environ.get('GOOGLE_CLOUD_PROJECT')}/secrets/github-token/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

# Set the token as an environment variable for the upload function
GITHUB_TOKEN = get_github_token()

# The rest of your notebook code...

# At the end of your notebook, include the upload function
def upload_reports_to_github(repo, token, branch='main', commit_message='Reports from Run Models colab'):
    """
    Upload all files from the report folder to GitHub repository.

    Args:
        repo (str): GitHub repository in the format 'username/repo'
        token (str): GitHub personal access token
        branch (str): Branch to push to (default: 'main')
        commit_message (str): Commit message (can include {report_file_count} placeholder)
    """
    # First, set up the report folder and get file count
    report_file_count = setup_report_folder(REPORT_FOLDER)

    # Format the commit message with the file count if needed
    if "{report_file_count}" in commit_message:
        commit_message = commit_message.format(report_file_count=report_file_count)

    print(f"Preparing to push {report_file_count} reports to: {repo}")

    # GitHub API endpoint for getting the reference
    api_url = f"https://api.github.com/repos/{repo}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Get the current reference (SHA) of the branch
        ref_response = requests.get(f"{api_url}/git/refs/heads/{branch}", headers=headers)
        ref_response.raise_for_status()
        ref_sha = ref_response.json()["object"]["sha"]

        # Get the current commit to which the branch points
        commit_response = requests.get(f"{api_url}/git/commits/{ref_sha}", headers=headers)
        commit_response.raise_for_status()
        base_tree_sha = commit_response.json()["tree"]["sha"]

        # Create a new tree with all the files in the report folder
        new_tree = []

        report_path = Path(REPORT_FOLDER)
        for file_path in report_path.glob("**/*"):
            if file_path.is_file():
                # Calculate the path relative to the report folder
                relative_path = file_path.relative_to(report_path)
                github_path = f"reports/{relative_path}"

                # Read file content and encode as base64
                with open(file_path, "rb") as f:
                    content = f.read()

                # Add the file to the new tree
                new_tree.append({
                    "path": github_path,
                    "mode": "100644",  # File mode (100644 for regular file)
                    "type": "blob",
                    "content": content.decode('utf-8', errors='replace')
                })

        # Create a new tree with the new files
        new_tree_response = requests.post(
            f"{api_url}/git/trees",
            headers=headers,
            json={
                "base_tree": base_tree_sha,
                "tree": new_tree
            }
        )
        new_tree_response.raise_for_status()
        new_tree_sha = new_tree_response.json()["sha"]

        # Create a new commit
        new_commit_response = requests.post(
            f"{api_url}/git/commits",
            headers=headers,
            json={
                "message": commit_message,
                "tree": new_tree_sha,
                "parents": [ref_sha]
            }
        )
        new_commit_response.raise_for_status()
        new_commit_sha = new_commit_response.json()["sha"]

        # Update the reference to point to the new commit
        update_ref_response = requests.patch(
            f"{api_url}/git/refs/heads/{branch}",
            headers=headers,
            json={"sha": new_commit_sha}
        )
        update_ref_response.raise_for_status()

        print(f"Successfully pushed {report_file_count} files to GitHub repository: {repo}")
        print(f"Branch: {branch}")
        print(f"Commit message: {commit_message}")
        return True

    except Exception as e:
        print(f"Error uploading files to GitHub: {e}")
        return False

# Execute the upload at the end of the notebook
TARGET_REPO = "username/target-repo"  # Replace with your target repository
upload_reports_to_github(TARGET_REPO, GITHUB_TOKEN, branch='main', commit_message='Pushed report files from Cloud Run')
```

## Part 6: Deploy to Cloud Run

```bash
# Build and deploy the application
gcloud builds submit --tag gcr.io/your-project-id/notebook-executor

gcloud run deploy notebook-executor \
  --image gcr.io/your-project-id/notebook-executor \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars="GOOGLE_CLOUD_PROJECT=your-project-id"
```

## Part 7: Set Up GitHub Webhook

1. Go to your source GitHub repository settings
2. Navigate to Webhooks
3. Add a new webhook with the following settings:
   - Payload URL: `https://your-cloud-run-url.run.app/webhook`
   - Content type: `application/json`
   - Secret: (Optional, but recommended for security)
   - Events: Select "Just the push event"

## Part 8: Set Up Service Account Permissions

```bash
# Create a service account for the Cloud Run service
gcloud iam service-accounts create notebook-executor-sa \
  --display-name="Notebook Executor Service Account"

# Grant necessary permissions
gcloud projects add-iam-policy-binding your-project-id \
  --member="serviceAccount:notebook-executor-sa@your-project-id.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"

# Update the Cloud Run service to use this service account
gcloud run services update notebook-executor \
  --service-account="notebook-executor-sa@your-project-id.iam.gserviceaccount.com" \
  --region us-central1
```

## Part 9: (Optional) Set Up Scheduled Execution

If you want to run the notebook on a schedule, you can use Cloud Scheduler:

```bash
# Create a scheduler job
gcloud scheduler jobs create http notebook-executor-scheduler \
  --schedule="0 */6 * * *" \
  --uri="https://your-cloud-run-url.run.app/run-notebook" \
  --http-method=POST \
  --time-zone="America/New_York"
```

## Testing

1. Visit your Cloud Run URL (`https://your-cloud-run-url.run.app`)
2. Click the "Run Notebook" button
3. The notebook will be executed and results will be pushed to the target GitHub repository

## Troubleshooting

- Check Cloud Run logs: `gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=notebook-executor" --limit 50`
- Ensure all API permissions are correctly set
- Verify that the GitHub token has the necessary permissions
- Check the notebook execution logs in Cloud Run
