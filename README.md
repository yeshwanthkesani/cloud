[DreamStudio](https://dreamstudio.com)
# ModelEarth Cloud

## Flask via Google Cloud

Create a [cloud/team/2025/[handle]](https://github.com/modelearth/cloud/) folder where you'll add deployment steps to launch a Flask site using Google Cloud. 

For your [handle] use lowercase firstname and optionally your last initial, or your nickname.

Our [webhook repo](https://github.com/modelearth/webhook/) has a sample with Google Cloud Flask deployment steps you can copy and improve.


## Integration with localsite navigation

1. Fork and clone our [cloud repo](https://github.com/modelearth/cloud) and [localsite repo](https://github.com/modelearth/localsite). 

2. Turn on GitHub Pages for both. So [account].github.io/cloud works.

3. In the "team/2025" subfolder, add a folder with your handle (firstname) from our [Member List](https://model.earth/community/members).
Use lowercase and optionally include your last initial.

4. Copy the [index.html page](https://github.com/ModelEarth/cloud/blob/main/index.html) to your new folder. Change the title to a description of the folder's content and/or add your handle in parentheses.

5. Add your code additions and document in a README.md file.

6. Submit a Pull Request (PR), and include a URL link in the following format when sending an email to Loren to pull your additions.
[account].github.io/cloud/team/2025/[handle]


Generally avoid commiting datasets in the cloud repo.  
Pull datasets directly from other GitHub repos, Google Sheets and/or APIs.

<!--
Let's document trying [Cursor AI with Claude](https://cursor.com).

CoLabs + [Anvil](https://anvil.works/learn/tutorials/data-science#connecting-notebooks) + [Plotly](https://plotly.com/python) and [Seaborn](https://seaborn.pydata.org/examples/index.html) + [Cursor](https://www.cursor.com/) 

[Cloudflare Workers](https://developers.cloudflare.com/workers/) to create an app.
-->


## Web App (with Google Cloud Run - for Flask)

[Starter code](RunModels) to run a colab using Google Cloud Run.

https://claude.ai/public/artifacts/a3d76132-45f4-4155-aef8-4870adf64f20

Promoted with: Create commands for creating a Google Cloud Run containing Flask and use the resulting project ID to create a website that executes a .ipynb file that resides in a Github repo. Whenever the repo is updated, update the website. The .ipynb file will be triggered by a button on a page and it will push files to another GitHub repo. Set permissions in Google to allow the push from the Google server to occur. Here's the function we use to push the files. (I provided the upload_reports_to_github function from the last step in our Run Models colab.)


## Firebase

[Firebase + Flask Auth Setup](team/2025/revanth) - For Static hosting with User Auth

