# Sustainability Resources Platform (sustainable-info)

This is the code repository for the WPI Sustainability Resources Platform website (final deliverable of WPI D20 IQP), developed by Rui Huang, Akash Shaji and Emily Baker.

You can check out a snapshot of the website [here](https://ryc1x.github.io/sustainable-studies/). For the most up-to-date version we recommend contacting WPI's office of sustainability.

The repository consists of a Vue.js project, which contains the necessary code for generating the website. If you plan to maintain the development, you may find the following instructions to be helpful.

## About the Project

This project is developed with `Vue` 2.6 and managed with `NPM`.

- Setup
- Updating the Curricula Listing
- Deployment

### Setup

#### Install Dependencies

To run the project, you first need to install necessary dependencies via `npm`:

```
npm install
```

#### Compiles and hot-reloads for development

Then you can serve the project locally:

```
npm run serve
```

(The default URL used is: http://localhost:8080/)

#### Compiles and minifies for production

You can then generate production code, containing necessary files for deploying the website.

```
npm run build
```

(This command will generate a `dist` folder under the root directory)


### Updating the Curricula Listing

In order to update the curricula listing, all one has to do is update `CourseData.xlsx` under root directory and run the following command. This requires having `Python 3` with package `xlrd` installed.

```
python3 updateCourses.py
```

This command will run the `updateCourses.py` script and generate `courses.json` under `src/assets` directory based on the entry in `CourseData.xlsx`.

(Note that the updates on `CourseData.xlsx` needs to follow the format strictly to avoid any unexpected errors in the script)


### Deployment

To host the website for public access, you need to host the production files under `dist` directory. We are using GitHub Pages to host this lightweight front-end webpage ([Link](https://ryc1x.github.io/sustainable-studies/)). You may choose to use any website hosting service though.

#### Deployment using GitHub Pages

Please refer to this [tutorial](https://cli.vuejs.org/guide/deployment.html#gitlab-pages) for a full deployment guide.

To deploy the project, navigate to `deploy.sh`, change the file (line 20/23 specifically) accordingly and run the following command:

```
bash deploy.sh
```

Then navigate to your GitHub Pages site, the website should be deployed successfully.

(If you doesn't change the remote repo address in the `deploy.sh`, you will not have the permission to push)





## Additional Information

### Helpful Links

https://vuejs.org/

https://cli.vuejs.org/

https://vuematerial.io/
