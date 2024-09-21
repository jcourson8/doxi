Title: AWS via Flightcontrol - SolidDocs

URL Source: https://docs.solidjs.com/guides/deployment-options/aws-via-flightcontrol

Markdown Content:
Deploying your App[Edit this page](https://github.com/solidjs/solid-docs-next/edit/main/src/routes/guides/deployment-options/aws-via-flightcontrol.mdx)

[Flightcontrol](https://www.flightcontrol.dev/) is a platform that fully automates deployments to Amazon Web Services (AWS). For more information on Flightcontrol's capabilities, you can [visit their docs](https://www.flightcontrol.dev/docs).

* * *

Flightcontrol offers a GitHub integration, leveraging its continuous development actions.

To get started with Flightcontrol's GitHub integration, you'll first need to log in or sign up to the Flightcontrol platform. After you're logged in, simply link your GitHub account to Flightcontrol.

Once connected, Flightcontrol will take care of the rest. It automatically detects any new pushes to your specified GitHub branches and builds your project. The build process uses the commands in your `package.json` file and adheres to the settings that you have configured in Flightcontrol. No additional setup is needed.

* * *

1.  In the Flightcontrol dashboard, create a new project and select the repository you wish to use as the source.
    
2.  Choose the GUI as your configuration type.
    
3.  Add your Solid site as a static site by clicking the "Add a Static Site" option.
    

5.  Label your output directory as `dist`.
    
6.  If your project requires environment variables, add them in the designated area:
    

7.  Finally, connect your AWS account to complete the setup.

* * *

1.  Navigate to your Flightcontrol dashboard and initiate a new project. Choose the repository you'd like to use as the source.
    
2.  Opt for the `flightcontrol.json` as your configuration type.
    

3.  Add a new file named `flightcontrol.json` at the root of your selected repository. Below is an example configuration:

```
{  "$schema": "https://app.flightcontrol.dev/schema.json",  "environments": [    {      "id": "production",      "name": "Production",      "region": "us-west-2",      "source": {        "branch": "main"      },      "services": [        {          "id": "my-static-solid",          "buildType": "nixpacks",          "name": "My static solid site",          "type": "static",          "domain": "solid.yourapp.com",          "outputDirectory": "dist",          "singlePageApp": true        }      ]    }  ]}
```

[Report an issue with this page](https://github.com/solidjs/solid-docs-next/issues/new?assignees=ladybluenotes&labels=improve+documentation%2Cpending+review&projects=&template=CONTENT.yml&title=[Content]:&subject=/guides/deployment-options/aws-via-flightcontrol.mdx)
