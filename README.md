# Docker Learning Lab

A hands-on learning repository for building Docker fundamentals through small daily exercises. The goal is to document practical command usage, container workflows, Dockerfiles, images, volumes, networking, and debugging notes as I learn.

## Overview

This repository is organized as a weekly lab journal. Each day contains commands, notes, and small runnable examples rather than a single production application.

Current focus: **Week 1 - Docker fundamentals**

## Motivation

I am using this repository to turn Docker concepts into repeatable practice. Recruiters and reviewers should be able to see the progression from basic container commands to more realistic development workflows.

## Current Contents

```text
docker-learning-lab/
└── week1/
    ├── day1/   # Docker fundamentals, commands, and notes
    ├── day2/   # First Dockerfile and Python container example
    ├── day3/
    ├── day4/
    ├── day5/
    ├── day6/
    └── day7/
```

## Skills Practiced

- Docker CLI fundamentals
- Container lifecycle commands
- Image building with Dockerfiles
- Running small Python applications in containers
- Recording commands and notes for repeatable learning
- Building a habit of daily technical documentation

## Getting Started

Clone the repository:

```bash
git clone https://github.com/haseebahmad60/docker-learning-lab.git
cd docker-learning-lab
```

Open a specific day and follow the notes or commands:

```bash
cd week1/day1
```

For days that include a Dockerfile, build and run the example from that day folder:

```bash
docker build -t docker-learning-day2 .
docker run --rm docker-learning-day2
```

## Documentation Style

Each day should include one or more of the following:

- Commands used during practice
- Notes explaining what each command does
- Small runnable examples
- Mistakes or debugging lessons
- A short reflection on what was learned

## Roadmap

- Add short summaries for each completed day
- Add a `docker-compose` practice section
- Add networking and volume examples
- Add a small multi-container app
- Add diagrams for image/container lifecycle and compose networking

## Learning Outcomes

This repository shows steady learning, command fluency, and a habit of documenting work. It is intentionally a lab, not a finished product.

## License

No license has been selected yet.
