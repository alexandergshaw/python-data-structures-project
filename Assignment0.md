# Assignment 0: Development Environment Setup

## Phase 1: Repository Setup & Deployment

### Step 1: Fork the Repository

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

1. Open your forked repository on GitHub.
2. Click the green **Code** button near the top-right of the repository page.
3. Select the **Codespaces** tab in the dropdown.
4. Click **Create codespace on main**.

GitHub will begin building your Codespace. This opens a browser-based version of Visual Studio Code connected to a cloud server running your project.

> **Note:** The Codespace may take several minutes to initialize the first time. This is normal. Wait for the editor to fully load before proceeding.

---

### Step 3: Explore the Development Environment

- **File Explorer** (left sidebar, folder icon): Browse and open project files.
- **Source Control panel** (left sidebar, branch icon): Stage, commit, and manage Git changes without typing commands.
- **Terminal** (bottom panel or `Ctrl+\``): Run commands directly on the cloud server.
- **Ports panel** (bottom panel, "Ports" tab): Lists network ports being used by your running application.

---

### Step 4: Install Project Dependencies

In the Terminal, run:

```bash
pip install -r requirements.txt
```

> **Tip:** If you see a "command not found" error, make sure you are in the Terminal panel at the bottom of the editor, not the search bar.

---

### Step 5: Run the Application

In the Terminal, run:

```bash
python app.py
```

**Open the application in your browser:**

1. Click the **Ports** tab at the bottom of the editor.
2. Locate the forwarded port (typically port `5000`).
3. Click the **globe icon** or the URL next to the port to open the application in a new browser tab.

---

### Step 6: Verify the Application

- Confirm the application loads successfully in your browser.
- Browse the application briefly.
- Note any error messages in the terminal or browser before continuing.

> **Tip:** If the app fails to start, re-run `pip install -r requirements.txt` and try again.

---

### Step 7: Deploy to Vercel

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

## Phase 2: First Code Change

---

### Step 1: Create a Feature Branch

In the Terminal, run:

```bash
git checkout -b assignment-0-setup
```

> **Tip:** You can verify which branch you are on by running `git branch`. The active branch is marked with an asterisk (`*`).

---

### Step 2: Make a Visible Change

Open a template file in the `templates/` folder, make a small visible edit (e.g., add your name to a heading or welcome message), and save the file.

> **Note:** Keep the change small. You are not expected to build a feature — you are learning the workflow.

---

### Step 3: Verify the Change

1. If the application is not already running, start it with `python app.py`.
2. Open the application in your browser using the Ports panel.
3. Confirm your change appears on the page.

If your change does not appear, double-check that you saved the file and that you are viewing the correct page.

---

### Step 4: Run Automated Tests

```bash
python -m pytest assignments/ -q
```

Review the output. All tests should pass. If any tests fail, read the error message — it will tell you which test failed and why.

> **Tip:** Tests that were already failing before you made any changes are not your responsibility for this assignment.

---

### Step 5: Commit the Change

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "Complete Assignment 0 setup"
```

---

### Step 6: Push the Branch

```bash
git push origin assignment-0-setup
```

After pushing, your branch and commits will appear on your GitHub repository page.

---

## Phase 3: Pull Request Workflow

---

### Step 1: Open a Pull Request

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

1. On your Pull Request page, scroll down to the **Checks** section.
2. Wait for all checks to complete (this may take a minute or two).
3. Verify that all checks show a green ✅ status.

If any check fails, click on it to view the detailed log and understand what went wrong.

---

### Step 4: Merge the Pull Request

1. Scroll to the bottom of the Pull Request page.
2. Click **Merge pull request**.
3. Click **Confirm merge**.
4. Click **Delete branch** to clean up the feature branch.

---

### Step 5: Verify Automatic Redeployment

1. Open your Vercel dashboard at [https://vercel.com](https://vercel.com).
2. Select your project.
3. Confirm a new deployment was triggered after the merge (check the deployments list).
4. Once the deployment finishes, click the live URL.
5. Verify that your code change appears in the production application.

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
