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

## Web App (Cloud Run):

We'll be using Tauri to deploy to Google Cloud by using Cloud Run for web apps or Cloud Build for automated builds and deployments. 

1. **Build a Docker Image:** Create a Dockerfile to package your Tauri application as a container image.
2. **Deploy to Cloud Run:** Use the gcloud run deploy command to deploy your container image to Cloud Run. 
3. **Enable Continuous Deployment (Optional):** Set up Cloud Build triggers to automatically deploy your application whenever changes are pushed to your Git repository. 

[Tauri](https://tauri.app/) provides a convenient direct-distribution of [SwarmUI](https://dreamstudio.com/swarm) using SvelteKit, Svelte and Rust, and hence no Electron.  Tauri provides the benefits of Rust without needing to be a Rust expert.

SwarmUI also supports deploments via Microsoft's [Blazor Hybrid .NET MAUI C#](https://learn.microsoft.com/en-us/training/modules/build-blazor-hybrid/)
