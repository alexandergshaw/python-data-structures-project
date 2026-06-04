# Assignment 0: Development Environment Setup

## Assignment Overview

Assignment 0 establishes the professional software development workflow you will use throughout this course. Every assignment going forward will follow the same process: fork a repository, write code in a cloud environment, test your changes, and submit your work using a Pull Request.

By completing this assignment, you will learn how to:

- Fork a GitHub repository
- Create and use a GitHub Codespace
- Run an application in a cloud development environment
- Deploy an application to Vercel
- Create and use Git branches
- Make and test code changes
- Commit and push code to GitHub
- Open and manage Pull Requests
- Review automated CI/CD checks
- Merge changes into the main branch
- Verify production deployments

> **Estimated completion time:** 1–2 hours

---

## Learning Objectives

By the end of this assignment, you will be able to:

- Explain the purpose of repositories, forks, branches, and pull requests
- Run an application using GitHub Codespaces
- Deploy an application using Vercel
- Use Git commands to manage source code
- Verify automated tests and deployment pipelines
- Follow a professional software development workflow

---

## Phase 1: Repository Setup & Deployment

### Objective

In this phase, you will create your own copy of the project, launch a cloud development environment, run the application locally, and deploy it to production.

---

### Step 1: Fork the Repository

**What is a repository?**
A **repository** (often called a "repo") is a folder that stores your project's code, history, and files. It lives on GitHub and tracks every change ever made to the project.

**What is a fork?**
A **fork** is your personal copy of someone else's repository. Forking lets you make changes without affecting the original project. You need your own fork so you can freely experiment, commit code, and submit your work independently.

**Instructions:**

1. Open your web browser and navigate to the course repository on GitHub.
2. In the top-right corner of the repository page, click the **Fork** button.
3. On the "Create a new fork" page, make sure your GitHub account is selected as the owner.
4. Leave the repository name as-is (or customize it if you prefer).
5. Click **Create fork**.

GitHub will redirect you to your personal copy of the repository. The URL will include your GitHub username, for example:
`https://github.com/YOUR-USERNAME/python-data-structures-project`

> **Note:** Always work from your forked repository, not the original course repository.

---

### Step 2: Create a GitHub Codespace

**What is GitHub Codespaces?**
**GitHub Codespaces** is a cloud-based development environment that runs directly in your browser. It gives you a full code editor, terminal, and all the tools you need — with no local installation required.

**Why Codespaces instead of installing software locally?**
Setting up a development environment locally can be complex and error-prone, especially across different operating systems. Codespaces provides a consistent, pre-configured environment that works the same way for every student.

**Instructions:**

1. Open your forked repository on GitHub.
2. Click the green **Code** button near the top-right of the repository page.
3. Select the **Codespaces** tab in the dropdown.
4. Click **Create codespace on main**.

GitHub will begin building your Codespace. This opens a browser-based version of Visual Studio Code connected to a cloud server running your project.

> **Note:** The Codespace may take several minutes to initialize the first time. This is normal. Wait for the editor to fully load before proceeding.

---

### Step 3: Explore the Development Environment

Once your Codespace is ready, take a moment to get familiar with the interface:

- **File Explorer** (left sidebar, folder icon): Browse and open project files.
- **Source Control panel** (left sidebar, branch icon): Stage, commit, and manage Git changes without typing commands.
- **Terminal** (bottom panel or `Ctrl+\``): Run commands directly on the cloud server. This is where you will install dependencies, run the app, and execute tests.
- **Ports panel** (bottom panel, "Ports" tab): Lists network ports being used by your running application. Use this to open the app in your browser.

---

### Step 4: Install Project Dependencies

**Dependencies** are external packages your project needs to run. This project uses Python and Flask.

In the Terminal, run:

```bash
pip install -r requirements.txt
```

This reads the `requirements.txt` file and installs all required packages automatically.

> **Tip:** If you see a "command not found" error, make sure you are in the Terminal panel at the bottom of the editor, not the search bar.

---

### Step 5: Run the Application

Start the application by running the following command in the Terminal:

```bash
python app.py
```

You should see output indicating the Flask development server has started.

**Opening the application in your browser:**

1. Click the **Ports** tab at the bottom of the editor.
2. Locate the forwarded port (typically port `5000`).
3. Click the **globe icon** or the URL next to the port to open the application in a new browser tab.

---

### Step 6: Verify the Application

Before moving on, confirm that the application is working:

- The application should load successfully in your browser.
- Browse the application briefly to understand what it does.
- If you see any error messages in the terminal or browser, note them before continuing.

> **Tip:** Most startup errors are caused by missing dependencies. If the app fails to start, re-run `pip install -r requirements.txt` and try again.

---

### Step 7: Deploy to Vercel

**What is Vercel?**
**Vercel** is a cloud platform that hosts web applications and makes them publicly accessible on the internet. When you push code changes to GitHub, Vercel can automatically rebuild and redeploy your application — this is called **continuous deployment**.

**Why use Vercel?**
Professional development teams use automated deployment platforms so that every approved code change immediately goes live without manual intervention. Learning this workflow now prepares you for real-world software development.

**Instructions:**

1. Go to [https://vercel.com](https://vercel.com) and sign in with your GitHub account (or create a free account).
2. From the Vercel dashboard, click **Add New… → Project**.
3. Click **Continue with GitHub** and authorize Vercel to access your repositories if prompted.
4. Find and select your forked repository (`python-data-structures-project`).
5. Vercel will automatically detect the project configuration from `vercel.json`.
6. Click **Deploy**.

Vercel will build and deploy your application. This typically takes 1–2 minutes.

> **Note:** No additional configuration should be needed. The `vercel.json` file in this repository already contains the deployment settings.

---

### Step 8: Verify Production Deployment

1. After deployment finishes, Vercel will display a live URL (e.g., `https://python-data-structures-project-xyz.vercel.app`).
2. Click the URL to open your deployed application in a new tab.
3. Confirm the application loads correctly.
4. **Save this URL** — you will need it for your submission.

---

### Phase 1 Deliverables

- ✅ Forked GitHub repository
- ✅ Working GitHub Codespace
- ✅ Successful Vercel deployment with a live URL

---

## Phase 2: First Code Change

### Objective

In this phase, you will create your first branch, make a visible change to the application, run the automated tests, and prepare your changes for submission.

---

### Step 1: Create a Feature Branch

**What is a branch?**
A **branch** is an independent line of development within a repository. It lets you work on changes without affecting the main codebase until your work is reviewed and approved.

**Why do professional teams use branches?**
Branches keep work isolated. Multiple developers can work simultaneously without overwriting each other's changes. When work is complete, it is reviewed and merged into the main branch.

In the Terminal, run:

```bash
git checkout -b assignment-0-setup
```

This creates a new branch named `assignment-0-setup` and switches to it immediately.

> **Tip:** You can verify which branch you are on by running `git branch`. The active branch is marked with an asterisk (`*`).

---

### Step 2: Make a Visible Change

Make a simple, visible modification to the application. The goal is to confirm you can edit code and see the result.

**Suggestions:**

- Add your name to the homepage or a status message
- Update a welcome heading or introductory text
- Add a short personal introduction to a page

Open a template file (look in the `templates/` folder), find text you want to change, and edit it. Save the file when done.

> **Note:** Keep the change small. You are not expected to build a feature — you are learning the workflow.

---

### Step 3: Verify the Change

1. If the application is not already running, start it with `python app.py`.
2. Open the application in your browser using the Ports panel.
3. Confirm your change appears on the page.

If your change does not appear, double-check that you saved the file and that you are viewing the correct page.

---

### Step 4: Run Automated Tests

**What are automated tests?**
**Automated tests** are scripts that verify your code behaves correctly. Instead of manually clicking through the application every time you make a change, tests check expected behavior instantly and consistently.

**Why is testing important?**
Tests catch bugs early, prevent regressions (accidentally breaking existing features), and give your team confidence that changes are safe to deploy.

Run the project's test suite with:

```bash
python -m pytest assignments/ -q
```

Review the output. All tests should pass (shown as dots or `passed`). If any tests fail, read the error message carefully — it will tell you which test failed and why.

> **Tip:** Tests that were already failing before you made any changes are not your responsibility for this assignment. Focus on ensuring your changes do not introduce new failures.

---

### Step 5: Commit the Change

**Committing** saves a snapshot of your changes to the repository's history. Each commit should represent a single logical change with a descriptive message.

Run the following commands in order:

```bash
git status
```
Shows which files have been modified. Review this before adding anything.

```bash
git add .
```
Stages all modified files, marking them to be included in the next commit.

```bash
git commit -m "Complete Assignment 0 setup"
```
Creates a commit with the message `Complete Assignment 0 setup`. The message describes what changed and why.

---

### Step 6: Push the Branch

**Pushing** uploads your local commits to GitHub so they are visible online and can be reviewed.

```bash
git push origin assignment-0-setup
```

- `origin` refers to your forked repository on GitHub.
- `assignment-0-setup` is the name of the branch being pushed.

After pushing, your branch and commits will appear on your GitHub repository page.

---

### Phase 2 Deliverables

- ✅ Feature branch (`assignment-0-setup`)
- ✅ Visible code change in the application
- ✅ Passing automated tests
- ✅ Branch pushed to GitHub

---

## Phase 3: Pull Request Workflow

### Objective

In this phase, you will submit your work using the same workflow used by professional software development teams.

---

### Step 1: Open a Pull Request

**What is a Pull Request?**
A **Pull Request** (PR) is a formal request to merge changes from one branch into another. It provides a space for code review, discussion, and automated checks before changes are accepted.

**Why are Pull Requests used?**
Pull Requests are the standard mechanism for submitting, reviewing, and approving code in professional teams. They create a permanent record of what changed, who reviewed it, and why it was approved.

**Instructions:**

1. Go to your forked repository on GitHub.
2. GitHub will display a banner saying your branch was recently pushed. Click **Compare & pull request**.
   - If the banner does not appear, click the **Pull requests** tab → **New pull request**.
3. Set the **base** branch to `main` and the **compare** branch to `assignment-0-setup`.
4. Use the following suggested title and description:

**Title:**
```
Complete Assignment 0 Setup
```

**Description:**
```
Completed repository setup, deployment verification, first code change, testing, and workflow validation.
```

5. Click **Create pull request**.

---

### Step 2: Review Files Changed

1. On your Pull Request page, click the **Files changed** tab.
2. Review the diff — the highlighted lines showing what was added (green) or removed (red).
3. Confirm that only the changes you intended appear. If you see unexpected changes, investigate before merging.

---

### Step 3: Review Automated Checks

**What is GitHub Actions?**
**GitHub Actions** is a built-in automation platform that runs tasks automatically when you push code or open a Pull Request. These tasks are defined in workflow files inside the repository.

**What does CI/CD mean?**
- **CI (Continuous Integration):** Automatically builds and tests every change to catch problems early.
- **CD (Continuous Deployment):** Automatically deploys changes that pass all checks.

**Why do automated checks exist?**
Checks ensure that code meets quality standards before it is merged. They prevent broken code from reaching the main branch and, ultimately, production.

**Instructions:**

1. On your Pull Request page, scroll down to the **Checks** section.
2. Wait for all checks to complete (this may take a minute or two).
3. Verify that all checks show a green ✅ status.

If any check fails, click on it to view the detailed log and understand what went wrong.

---

### Step 4: Merge the Pull Request

Once all checks pass:

1. Scroll to the bottom of the Pull Request page.
2. Click **Merge pull request**.
3. Click **Confirm merge**.
4. After a successful merge, click **Delete branch** to clean up the feature branch.

> **Tip:** Deleting merged branches is a professional best practice. It keeps the repository tidy and makes it clear which branches contain active work.

---

### Step 5: Verify Automatic Redeployment

When changes are merged into `main`, Vercel automatically detects the update and triggers a new deployment. This is continuous deployment in action.

**Instructions:**

1. Open your Vercel dashboard at [https://vercel.com](https://vercel.com).
2. Select your project.
3. Confirm a new deployment was triggered after the merge (check the deployments list).
4. Once the deployment finishes, click the live URL.
5. Verify that your code change (e.g., your name or message) appears in the production application.

---

### Phase 3 Deliverables

- ✅ Pull Request URL
- ✅ Passing GitHub Actions checks
- ✅ Merged Pull Request
- ✅ Updated production deployment on Vercel

---

## Submission Requirements

Submit the following in the course learning management system:

| Item | Description |
|---|---|
| GitHub Repository URL | Link to your forked repository |
| Vercel Deployment URL | Link to your live production deployment |
| Pull Request URL | Link to the merged Pull Request |
| Screenshot — Tests | Screenshot showing passing `pytest` output in the terminal |
| Screenshot — Deployment | Screenshot showing successful deployment in the Vercel dashboard |

---

## Grading Rubric

| Category | Points |
|---|---|
| Repository Setup & Deployment | 35 |
| First Code Change | 35 |
| Pull Request Workflow | 30 |

**Total: 100 Points**

---

## Troubleshooting

### Codespace fails to start

**Common causes:**
- GitHub service outage
- Browser extension blocking the page

**Solutions:**
- Refresh the page and try again.
- Try a different browser or disable browser extensions.
- Check [https://githubstatus.com](https://githubstatus.com) to see if GitHub is experiencing issues.
- Delete the Codespace and create a new one from the **Code → Codespaces** tab.

---

### Application will not run

**Common causes:**
- Missing dependencies
- Syntax error in a recently edited file

**Solutions:**
- Run `pip install -r requirements.txt` and try `python app.py` again.
- Read the error message in the terminal carefully — it usually points to the exact file and line number with the problem.
- Undo any recent changes with `git diff` to see what you modified, or `git checkout -- <filename>` to revert a specific file.

---

### Forwarded port not visible

**Common causes:**
- Application not running
- Ports panel not open

**Solutions:**
- Confirm the application started successfully (look for the Flask "Running on" message in the terminal).
- Click the **Ports** tab at the bottom of the editor. If it is not visible, go to **View → Terminal** and then switch to the **Ports** tab.
- If the port appeared but the browser tab shows an error, wait a few seconds and refresh.

---

### Tests fail

**Common causes:**
- A code change broke existing functionality
- Dependencies not installed

**Solutions:**
- Read the test failure output carefully. It will tell you which test failed and what the expected versus actual result was.
- Undo any changes unrelated to the test that is failing.
- Run `pip install -r requirements.txt` to ensure all packages are installed.

---

### Push rejected

**Common causes:**
- Trying to push to the original course repository instead of your fork
- Not authenticated in the Codespace

**Solutions:**
- Confirm that your Codespace is connected to your fork, not the original repository. Check the URL of your repository in the browser.
- Run `git remote -v` to see where your repository is pointing. The URL should contain your GitHub username.
- In the Codespace, GitHub authentication is handled automatically. If you are prompted to log in, follow the on-screen instructions.

---

### Pull Request not appearing

**Common causes:**
- Branch was not pushed
- Comparing against the wrong repository

**Solutions:**
- Run `git push origin assignment-0-setup` again and check for errors.
- On GitHub, go to your fork (not the original repository), click **Pull requests → New pull request**, and manually select your branch.
- Make sure the **base repository** is your fork, not the upstream course repository.

---

### GitHub Actions checks failing

**Common causes:**
- Tests are failing in CI
- Linting or formatting errors

**Solutions:**
- Click the failing check to open the detailed log.
- Run the same command locally in the terminal: `python -m pytest assignments/ -q`
- Fix the errors reported in the log, commit, and push again. The checks will re-run automatically.

---

### Vercel deployment failing

**Common causes:**
- Build error in the application
- Missing environment variable or configuration

**Solutions:**
- Open the Vercel dashboard and click on the failed deployment to view its build log.
- Look for the first error message in the log — that is usually the root cause.
- Confirm that the `vercel.json` file in the repository has not been modified.
- If you are unsure what changed, compare your `vercel.json` against the original course repository.

---

### Vercel redeployment not occurring

**Common causes:**
- Vercel is not connected to your GitHub repository
- The merge went to a branch Vercel is not watching

**Solutions:**
- Open your Vercel project settings and confirm that it is connected to your forked repository and set to deploy on pushes to `main`.
- Confirm the Pull Request was merged into `main` (not a different branch).
- Trigger a manual redeployment from the Vercel dashboard by clicking **Redeploy** on your most recent deployment.
