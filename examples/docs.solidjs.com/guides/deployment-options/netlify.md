Title: Netlify - SolidDocs

URL Source: https://docs.solidjs.com/guides/deployment-options/netlify

Markdown Content:
[Netlify](https://www.netlify.com/) is a widely-used hosting platform suitable for various types of projects. For detailed guidance on build procedures, deployment options, and the range of features available, you can visit the [Netlify documentation](https://docs.netlify.com/).

* * *

[Using the Netlify web interface](https://docs.solidjs.com/guides/deployment-options/netlify#using-the-netlify-web-interface)
-----------------------------------------------------------------------------------------------------------------------------

1.  Begin by navigating to [Netlify's website](https://app.netlify.com/) and logging in or creating a new Netlify. Once logged in, you will be take to your dashboard. Click the `New site from Git` button to start a new project.

2.  On the following page, choose "Connect to GitHub" or your preferred Git repository hosting service.

3.  After selecting your Solid project repository, you'll be directed to a configuration screen. Update the "Publish directory" field from `netlify` to `dist`. Then, click "Deploy" to start the deployment process.

4.  Once the build and deployment are complete, you will be taken to a screen that displays the URL of your live site.

* * *

[Using the Netlify CLI](https://docs.solidjs.com/guides/deployment-options/netlify#using-the-netlify-cli)
---------------------------------------------------------------------------------------------------------

1.  Install the Netlify CLI using your preferred package manager:

**Note:** Before proceeding, ensure that your Netlify account and team are fully set up. This is crucial for a seamless project setup and deployment.

2.  Open your terminal, navigate to your project directory, and run the `netlify init` command. Authenticate using one of the supported login options.
    
3.  Follow the on-screen instructions from the CLI. When prompted for the 'Directory to deploy,' specify `dist` — this is where Solid stores the built project files.
    

After completing the process, your project will be deployed on Netlify and can be accessed via the provided URL.
