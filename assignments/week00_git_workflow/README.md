# Week 00: Git Workflow

## Overview

This is Assignment 0 — your introduction to the development workflow you will use for every assignment in this course. There is very little "programming" here. The goal is to get comfortable with the tools and the process **before** the actual coding begins.

By the end of this assignment you will have:

- Created a feature branch on your own copy of the repository.
- Opened that branch inside GitHub Codespaces (a cloud editor that runs in your browser).
- Made a small but meaningful code change — replacing a placeholder name with your own.
- Run the automated tests to verify your change is correct.
- Committed and pushed your work.
- Opened a Pull Request (PR) on GitHub.
- Confirmed the Vercel preview deployment worked.
- Merged the PR into your main branch.

This exact sequence — **branch → code → test → commit → push → PR → preview → merge** — is what professional developers do every single day. Learning it now means you will feel at home in any real software team.

---

## What You Are Changing

Inside the file `assignment.py` in this folder, there is one line that looks like this:

```python
STUDENT_NAME = "John Doe"
```

Your only task is to replace `"John Doe"` with your own full name, like this:

```python
STUDENT_NAME = "Maria Garcia"
```

That is it. One line. Everything else in this assignment is about *how* you make and deliver that change.

---

## Folder Structure

```
week00_git_workflow/
├── assignment.py        ← edit this file
├── tests/
│   └── test_week00.py   ← automated checks (do not edit)
└── README.md            ← you are here
```

---

## Step-by-Step Instructions

---

### Step 1 — Create a New Branch

A **branch** is like a personal scratchpad that lives alongside your main code. Changes you make on a branch do not affect `main` until you deliberately merge them. This protects your working application while you experiment.

**In the Terminal inside your Codespace, run:**

```bash
git checkout -b assignment-0-name
```

Breaking that command down:
- `git` — the version-control program.
- `checkout` — "switch to a branch."
- `-b` — "create it first if it does not exist yet."
- `assignment-0-name` — the name of your new branch (you can use any name, but be descriptive).

**Verify it worked:**

```bash
git branch
```

You will see a list of branches. The one with an asterisk (`*`) next to it is the branch you are currently on. It should look like:

```
* assignment-0-name
  main
```

> **Why bother with branches?**
> Imagine you are halfway through a change and you break something. With a branch, you can always throw your changes away and return to `main` safely. Without one, you could accidentally break your deployed application.

---

### Step 2 — Open the Assignment File

In the left sidebar of your Codespace, click the **Explorer** icon (it looks like two stacked pages). Navigate to:

```
assignments/week00_git_workflow/assignment.py
```

Click on `assignment.py` to open it in the editor.

You will see this line near the top of the file:

```python
STUDENT_NAME = "John Doe"
```

---

### Step 3 — Change the Name

Replace `"John Doe"` with your own full name. Keep the quotes. For example:

```python
STUDENT_NAME = "Maria Garcia"
```

> **Common mistakes to avoid:**
> - Do not remove the quotes. Python needs them to know this is a text value.
> - Do not add extra spaces inside the quotes. `" Maria Garcia "` and `"Maria Garcia"` are different strings.
> - Do not change anything else in the file. The tests expect the rest of the file to stay the same.

Save the file. On most systems you can press `Ctrl + S` (Windows/Linux) or `Cmd + S` (Mac).

---

### Step 4 — Run the Unit Tests

**Unit tests** are small automated checks that confirm your code does what it is supposed to do. Think of them like answer keys — they compare your code's output against the expected result and tell you immediately if something is wrong.

**Run only this week's tests:**

```bash
pytest assignments/week00_git_workflow/tests/ -v
```

The `-v` flag means "verbose" — it prints the name of each individual test so you can see exactly what is being checked.

**What you should see when all tests pass:**

```
assignments/week00_git_workflow/tests/test_week00.py::test_student_name_is_a_string        PASSED
assignments/week00_git_workflow/tests/test_week00.py::test_student_name_is_not_empty       PASSED
assignments/week00_git_workflow/tests/test_week00.py::test_student_name_is_not_john_doe    PASSED
assignments/week00_git_workflow/tests/test_week00.py::test_get_student_name_matches_variable PASSED
assignments/week00_git_workflow/tests/test_week00.py::test_is_complete_returns_boolean     PASSED
assignments/week00_git_workflow/tests/test_week00.py::test_is_complete_is_true_after_name_change PASSED
assignments/week00_git_workflow/tests/test_week00.py::test_get_week_summary_is_a_dict      PASSED
assignments/week00_git_workflow/tests/test_week00.py::test_get_week_summary_contains_student_name PASSED

8 passed in 0.XX s
```

**If a test fails,** read the error message carefully. It will tell you which test failed and why. The most common failure for this assignment looks like:

```
FAILED test_student_name_is_not_john_doe
AssertionError: STUDENT_NAME is still 'John Doe'. Open assignment.py and replace 'John Doe' with your own full name.
```

That means you either forgot to save the file or forgot to make the change. Fix it, save, and re-run the tests.

You can also run all assignment tests at once (useful to make sure you have not accidentally broken anything else):

```bash
python -m pytest assignments/ -q
```

---

### Step 5 — Commit Your Change

**Committing** is how you tell Git "I am happy with this change — save a snapshot of it." A commit is a permanent record in the project's history. You will add a short message describing what you did.

**First, check what Git sees:**

```bash
git status
```

You will see something like:

```
On branch assignment-0-name
Changes not staged for commit:
  modified:   assignments/week00_git_workflow/assignment.py
```

This confirms Git noticed your edit. Good.

**Stage the change (tell Git which files to include in the commit):**

```bash
git add assignments/week00_git_workflow/assignment.py
```

Or, to stage all changed files at once:

```bash
git add .
```

**Create the commit with a descriptive message:**

```bash
git commit -m "Assignment 0: update STUDENT_NAME to my name"
```

A good commit message is short but descriptive. It tells anyone looking at the history *what* changed and *why*.

> **Check your commit was recorded:**
> ```bash
> git log --oneline -3
> ```
> You should see your new commit listed at the top.

---

### Step 6 — Push the Branch to GitHub

Committing only saves the snapshot locally — it is still only on the cloud server running your Codespace. **Pushing** sends it to GitHub so others (and GitHub Actions) can see it.

```bash
git push origin assignment-0-name
```

Breaking that down:
- `git push` — send commits to the remote server.
- `origin` — the name of the remote (your GitHub repository).
- `assignment-0-name` — the branch to push.

You should see output like:

```
To https://github.com/YOUR-USERNAME/python-data-structures-project.git
 * [new branch]      assignment-0-name -> assignment-0-name
```

If you see an error like `remote: Permission denied`, make sure your Codespace is connected to your **fork** of the repository (not the original course repository). Run `git remote -v` to check — the URL should contain your GitHub username.

---

### Step 7 — Open a Pull Request

A **Pull Request (PR)** is a formal way of saying "I have some changes on a branch and I want to merge them into main." It gives you (and instructors) a place to review the diff, run automated checks, and discuss the change before it becomes permanent.

1. Go to **your forked repository** on GitHub (the URL should include your username).
2. GitHub will likely show a yellow banner at the top: **"Your recently pushed branch: `assignment-0-name`. Compare & pull request."** Click that button.
   - If the banner is not visible, click the **Pull requests** tab → **New pull request**. Set the **base** branch to `main` and the **compare** branch to `assignment-0-name`.
3. Fill in the PR details:

   **Title:**
   ```
   Assignment 0: Update STUDENT_NAME
   ```

   **Description:**
   ```
   Changed the STUDENT_NAME placeholder from "John Doe" to my own name.
   All Week 00 unit tests pass.
   ```

4. Click **Create pull request**.

---

### Step 8 — Check the Vercel Preview Deployment

When you open a Pull Request, Vercel automatically builds and deploys a **preview version** of your application. This lets you (and reviewers) see exactly what the live site will look like if this PR is merged — without actually touching your production site yet.

**How to find the preview link:**

1. On your Pull Request page, scroll down to the **Checks** section (or look for a comment from the Vercel bot).
2. You will see a check called something like **"Vercel — Preview deployment"** or a Vercel bot comment with a link labeled **"Visit Preview"**.
3. Click that link. Your application should open in a new browser tab.
4. Look at the application and confirm it loads without errors.

> **If the Vercel check shows a red ✗:**
> Click on the check to open the build log. Look for the first error message — that is usually the root cause. Common causes are a syntax error in a Python file or a missing dependency. See the Troubleshooting section at the bottom of this file.

> **If you do not see a Vercel check at all:**
> Vercel may not be connected to your repository. Go back to Assignment 0's Phase 1 instructions and make sure you completed the Vercel deployment setup.

---

### Step 9 — Merge the Pull Request

Once the Vercel preview looks good and all automated checks are green, you are ready to merge.

1. On the Pull Request page, scroll to the bottom.
2. Click **Merge pull request**.
3. Click **Confirm merge**.
4. Click **Delete branch** to clean up the branch now that it has been merged.

Your change is now part of `main`, and Vercel will automatically redeploy your production site with the updated code.

**Verify the production redeploy:**

1. Open your Vercel dashboard at [https://vercel.com](https://vercel.com).
2. Select your project.
3. You should see a new deployment in progress (or recently completed).
4. Once it finishes, click the live URL and confirm the application loads correctly.

---

## Understanding What Each Test Checks

| Test name | What it verifies |
|-----------|-----------------|
| `test_student_name_is_a_string` | `STUDENT_NAME` is a text value (not a number or missing) |
| `test_student_name_is_not_empty` | `STUDENT_NAME` is not blank |
| `test_student_name_is_not_john_doe` | You actually changed the placeholder |
| `test_get_student_name_matches_variable` | The `get_student_name()` function returns what the variable says |
| `test_is_complete_returns_boolean` | `is_complete()` gives back `True` or `False` |
| `test_is_complete_is_true_after_name_change` | The assignment registers as done after your name change |
| `test_get_week_summary_is_a_dict` | `get_week_summary()` returns a dictionary |
| `test_get_week_summary_contains_student_name` | The summary includes your name |

---

## Troubleshooting

### "I saved the file but the tests still fail"

Run `git status` and check that `assignment.py` shows as **modified**. If it does not, the file might have been saved in the wrong location. Double-check you are editing `assignments/week00_git_workflow/assignment.py` and not some other file.

### "git push is rejected"

Run `git remote -v`. The URL next to `origin` should contain **your GitHub username**. If it points to the original course repository, you are in the wrong place. Make sure your Codespace was opened from your fork, not the upstream repository.

### "I do not see the Vercel check on my PR"

Vercel needs to be connected to your repository. Go back to the full Assignment 0 setup instructions and complete the Vercel deployment steps (connecting your fork to Vercel). Once connected, future PRs will trigger previews automatically.

### "The Vercel build failed"

Click the failed check to open the build log. Scroll to the first line that says `Error:` — that is usually the root cause. A common cause is a Python syntax error in a file you edited. Read the error carefully, fix the problem in your editor, commit the fix, and push again. The checks will re-run automatically.

### "I merged the PR but production did not redeploy"

Open your Vercel project settings and confirm the project is connected to your forked repository and is set to deploy on pushes to `main`. If everything looks right, click **Redeploy** on the most recent deployment in the Vercel dashboard to trigger it manually.
