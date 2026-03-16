# Day 1 Structure and Tasks

## London Transport Data Engineering Project

Welcome to **Day 1** of the London Transport Data Engineering Project.

This document explains:

* the technical structure of the project
* the raw data organization
* what you must complete today
* how to manage your GitHub workflow
* what your Day 1 deliverables are

Please read this file carefully before starting the ETL and ELT task files.

---

# 1. Day 1 goal

The goal of **Day 1** is to complete the full **local project foundation**.

That means that by the end of today, you should have:

* your own public GitHub repository
* the shared project cloned locally
* your own GitHub repository connected to the local project
* the correct folder structure created
* the raw transport data files placed correctly
* the Day 1 ETL tasks completed
* the Day 1 ELT tasks completed
* your progress pushed step by step to GitHub
* your checkpoint answers written

This is a full working day, and it should feel like a real junior data engineering assignment.

---

# 2. Day 1 project scope

For **Day 1 only**, your work is limited to the **local ETL and ELT foundation**.

You are **not** working on:

* Spark
* AWS S3
* Databricks
* dashboards
* advanced orchestration
* production deployment

Today is about building the first complete local version of the project correctly.

That local foundation is very important, because the later stages of the project will build on it.

---

# 3. The raw data for Day 1

For this project, you are working with **at least 10 raw source files**.

These files simulate exports from different internal transport systems.

This is intentional.

In real business work, data engineers often receive multiple files from different departments or systems, not one perfect file.

For Day 1, your raw files should be stored here:

```text
data/raw/
```

And the raw data should include **at least these 10 files**:

```text
data/raw/
├── stations.csv
├── lines.csv
├── journeys.json
├── vehicle_types.csv
├── operators.csv
├── zones.csv
├── disruptions.json
├── fares.csv
├── boroughs.csv
└── schedules.xml
```

You may later extend the project with even more files, but for Day 1 this is already a strong and realistic raw data layer.

---

# 4. What these raw files represent

Here is the business meaning of each raw file.

## `stations.csv`

Contains station-level information such as:

* station ID
* station name
* borough
* zone
* line reference

## `lines.csv`

Contains transport line information such as:

* line ID
* line name
* transport mode
* operator ID

## `journeys.json`

Contains journey or trip activity such as:

* journey ID
* station ID
* line ID
* passenger count
* delay minutes
* journey date

## `vehicle_types.csv`

Contains vehicle type information such as:

* vehicle type ID
* mode name
* capacity range

## `operators.csv`

Contains operator information such as:

* operator ID
* operator name
* service type

## `zones.csv`

Contains fare or travel zone information such as:

* zone ID
* zone name
* fare group

## `disruptions.json`

Contains disruption or incident records such as:

* disruption ID
* line ID
* disruption type
* severity
* date

## `fares.csv`

Contains pricing information such as:

* fare ID
* zone ID
* transport mode
* base fare

## `boroughs.csv`

Contains London borough data such as:

* borough ID
* borough name
* region group

## `schedules.xml`

Contains schedule information such as:

* schedule ID
* station ID
* line ID
* planned start time
* planned end time

This file set is intentionally larger than a tiny toy dataset.

That helps the project feel more serious, richer, and more portfolio-worthy.

---

# 5. Day 1 project folder structure

Your repository should be organized like this:

```text
london-transport-data-engineering-project/
│
├── README.md
├── README_02_Day1_Structure_and_Tasks.md
├── README_03_Day1_ETL.md
├── README_04_Day1_ELT.md
│
├── data/
│   ├── raw/
│   │   ├── stations.csv
│   │   ├── lines.csv
│   │   ├── journeys.json
│   │   ├── vehicle_types.csv
│   │   ├── operators.csv
│   │   ├── zones.csv
│   │   ├── disruptions.json
│   │   ├── fares.csv
│   │   ├── boroughs.csv
│   │   └── schedules.xml
│   ├── staging/
│   └── output/
│
├── sql/
│   ├── create_tables.sql
│   ├── etl_checks.sql
│   ├── elt_transform.sql
│   └── reporting_queries.sql
│
├── src/
│   ├── extract.py
│   ├── transform_etl.py
│   ├── load_postgres.py
│   ├── run_etl.py
│   ├── run_elt.py
│   └── utils.py
│
├── config/
│   └── settings.json
│
├── logs/
│   └── pipeline.log
│
└── docs/
    ├── project_notes.md
    └── checkpoint_answers.md
```

This structure is not random.

It is designed to help you think and work like a junior data engineer in a real team.

---

# 6. Why this structure matters

A good data engineering project is not only about code.

It is also about organization.

This structure helps you separate:

* raw data
* SQL logic
* Python logic
* configuration
* logs
* documentation

That makes the project:

* easier to understand
* easier to maintain
* easier to explain
* easier to show later in interviews

That is one reason this project can be a good portfolio item if you complete it well.

---

# 7. Your GitHub workflow for Day 1

Today, you must work in **your own public GitHub repository**.

That means you should do the following:

## Step 1

Clone the shared starter repository.

Example:

```bash
git clone <SHARED_REPOSITORY_URL>
```

## Step 2

Move into the project folder.

```bash
cd london-transport-data-engineering-project
```

## Step 3

Create your own public GitHub repository in your own GitHub account.

A good name could be:

```text
london-transport-data-engineering-project
```

## Step 4

Connect your local project to your own GitHub repository.

Example workflow:

```bash
git remote rename origin upstream
git remote add origin <YOUR_GITHUB_REPOSITORY_URL>
git remote -v
```

## Step 5

Push your work step by step during the day.

That means after every important milestone, you should run:

```bash
git add .
git commit -m "Clear message here"
git push -u origin main
```

Do not wait until the very end and push only once.

A real engineer saves progress regularly.

---

# 8. Suggested Day 1 commit milestones

To help you stay organized, here are good commit points for Day 1.

## Commit 1

After repository setup and folder creation

Example:

```bash
git commit -m "Set up project structure for Day 1"
```

## Commit 2

After adding the raw data files

```bash
git commit -m "Add London transport raw data files"
```

## Commit 3

After starting the ETL work

```bash
git commit -m "Add Day 1 ETL pipeline tasks"
```

## Commit 4

After starting the ELT work

```bash
git commit -m "Add Day 1 ELT pipeline tasks"
```

## Commit 5

After writing checkpoint answers and final updates

```bash
git commit -m "Complete Day 1 project deliverables"
```

These are only examples, but they show the kind of structured progress you should maintain.

---

# 9. Day 1 task list

Here is what you must complete today.

## Task 1 — Read the business scenario

Read the main `README.md` carefully and make sure you understand:

* who you are in this project
* what the business problem is
* why the project matters

## Task 2 — Set up your public GitHub repository

Create your own public repository and connect it properly.

## Task 3 — Create the project folder structure

Make sure your repository matches the required project structure.

## Task 4 — Add the 10 raw source files

Place all raw files inside:

```text
data/raw/
```

## Task 5 — Explore the raw data

Look at the files and understand:

* what each file represents
* what fields exist
* what potential data quality issues exist

## Task 6 — Create your notes file

Inside `docs/project_notes.md`, begin writing short notes about:

* the source files
* the business meaning
* the data quality issues you notice

## Task 7 — Complete the ETL tasks

Follow all guided ETL steps in:

* [README 03 - Day 1 ETL Tasks](./README_03_Day1_ETL.md)

## Task 8 — Complete the ELT tasks

Follow all guided ELT steps in:

* [README 04 - Day 1 ELT Tasks](./README_04_Day1_ELT.md)

## Task 9 — Answer the checkpoint questions

Write your answers in:

```text
docs/checkpoint_answers.md
```

## Task 10 — Push your work regularly

Make sure your GitHub repository reflects your real progress.

---

# 10. What you should observe while exploring the raw data

When you inspect the raw data, do not just look at it quickly.

Think like a data engineer.

Ask questions such as:

* Which files seem to describe reference data?
* Which file seems to contain operational events or transactions?
* Which fields may be used for joins?
* Which fields may contain messy values?
* Which tables might become dimension-style tables?
* Which table might become the main reporting table?

This is an important professional habit.

---

# 11. What Day 1 is trying to teach you

Day 1 is not only trying to teach you how to run a script.

Day 1 is training you to think in a more professional way about:

* repository structure
* source data management
* pipeline planning
* ETL vs ELT logic
* documentation
* GitHub workflow
* project ownership

These habits matter in real work.

---

# 12. Day 1 deliverables

By the end of today, your repository should contain:

* your own public GitHub project
* all 4 Day 1 README files
* the full project folder structure
* the 10 raw data files in the correct folder
* ETL implementation progress
* ELT implementation progress
* project notes
* checkpoint answers
* multiple commits showing step-by-step progress

If these are missing, your Day 1 submission is incomplete.

---

# 13. Required checkpoint questions

You must answer **all 5 checkpoint questions**.

Write your answers in:

```text
docs/checkpoint_answers.md
```

### Checkpoint Question 1

What is the business purpose of the London Transport Data Engineering Project?

### Checkpoint Question 2

Why are we using multiple raw source files instead of one clean table?

### Checkpoint Question 3

What is the difference between ETL and ELT in this project?

### Checkpoint Question 4

Why is it important to use your own public GitHub repository for this project?

### Checkpoint Question 5

Which raw files seem to be the most important for building the final reporting output, and why?

These questions are mandatory because they help confirm that you understand the project, not only the code.

---

# 14. Important reminder

This project is **guided**, which means you are not expected to invent everything from scratch.

You are expected to:

* follow the instructions carefully
* complete the steps in order
* understand what each step is doing
* document your work
* manage your repository professionally

That is the best way to learn from this project.

---

# 15. What to do next

Now that you understand the structure and Day 1 tasks, move to the technical task files:

* [README 03 - Day 1 ETL Tasks](./README_03_Day1_ETL.md)
* [README 04 - Day 1 ELT Tasks](./README_04_Day1_ELT.md)

Complete them carefully and do not forget to commit and push your progress regularly.



