# checkpoint_answers.md

# Day 1 Checkpoint Answers

## London Transport Data Engineering Project

## Why these checkpoint questions matter

These questions are an important part of Day 1.

They are not only here to check whether your code runs.
They are here to help you prove that you understand:

* the business context
* the technical structure
* the difference between ETL and ELT
* why this project matters professionally
* how to explain your own work clearly

Please answer all questions in your own words.

Short answers are acceptable, but they should still be clear and complete.

---

## Checkpoint Question 1

### What is the business purpose of the London Transport Data Engineering Project?

**Your answer:**
The business purpose of this project to make an analytic in order to give answers for questions, on which business users are interested.

---

## Checkpoint Question 2

### Why are we using multiple raw source files instead of one clean table?

**Your answer:**
Because we are recieving data from different sources and in different formats. And the raw files contain tha data, that is also different from business perspective. So it's more convenient to save such data separately and than analyze.

---

## Checkpoint Question 3

### What is the difference between ETL and ELT in this project?

**Your answer:**
In ELT version the  transformations are being done on database level vs python on memory transformation for ETL. The ELT is more suitable when we have big amount of data.

---

## Checkpoint Question 4

### Why is it important to use your own public GitHub repository for this project?

**Your answer:**
Because it's a good example of a portfolio project, that can be used in future interview.

---

## Checkpoint Question 5

### Which raw files seem to be the most important for building the final reporting output on Day 1, and why?

**Your answer:**
The **journeys.json** contains fact data on which the whole analysis has been build. Other files are also important but they have lookup data. 

---

## Final reflection

### What was the most important thing you learned from Day 1?

**Your answer:**
Actually the project is most the same as the previous one. It only contains more files as a source. I think some more complicated logic should be used for deduplication.

---

## Submission reminder

Before finishing Day 1, make sure you have:

* answered all 5 checkpoint questions
* added your name
* added your public GitHub repository link
* committed this file
* pushed it to your GitHub repository

Example:

```bash
git add .
git commit -m "Add Day 1 checkpoint answers"
git push -u origin main
```

This file is part of your Day 1 deliverables, so do not skip it.


