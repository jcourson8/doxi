Title: Railway - SolidDocs

URL Source: https://docs.solidjs.com/guides/deployment-options/railway

Markdown Content:
Deploying your App[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/railway.mdx)

[Railway](https://railway.app/) is a well-known platform for deploying a variety of web and cloud-based projects. For an in-depth look at the features offered by Railway, as well as detailed deployment guidelines, you can consult the [Railway documentation](https://docs.railway.app/).

* * *

To begin, you need to update the start command in your `package.json` file to make it compatible with Railway. Change the start command to `npx http-server ./dist` instead of using `vite`. This adjustment means you will need to build the app to generate the `dist` folder.

For local development, continue using the original `dev` command. Reserve the modified start command specifically for Railway deployments. Below is an example of how your `package.json` may be configured:

```
"scripts": {  "start": "npx http-server ./dist",  "dev": "vite",  "build": "vite build",  "serve": "vite preview",  "predeploy": "npm run build",  "deploy": "gh-pages -d build"},
```

* * *

1.  Visit Railway's homepage and click "Start a New Project." You will be redirected to connect with GitHub. Log in or create an account using your GitHub credentials and authorize Railway to access your account.

2.  After authorization, choose the repository that has your Solid project. During this step, you can also add any required environment variables.

3.  Once your project is configured, click "Deploy Now." After a successful deployment, a confirmation screen will appear.

4.  Railway does not automatically assign a domain to your project. To do this, go to the settings and manually generate a domain for your deployed project.

Once a domain has been generated, your Solid project should be live.

* * *

1.  Using your preferred package manager and install the Railway CLI:

2.  Open your terminal and run the following command to log in:

3.  You have the option to link your local Solid project to an existing Railway project using railway link. Alternatively, you can create a new project with `railway init` and follow the on-screen prompts.
    
4.  To deploy your project to Railway, use the following command:
    

```
railway up# orrailway up --detach # if you prefer to avoid logs
```

Your project will now be live on Railway.

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/railway.mdx)
