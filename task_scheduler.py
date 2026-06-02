"""
Imagine that we are building task scheduling system from scratch.
This system must execute tasks in the specified order.

We want to start with two types of tasks: send http request and execute command.
Tasks are executed sequentially one by one until successful completion.
Failed tasks are rescheduled to the end of the queue.

And also let's not take into account any persistence here.
Each new launch is considered independent of the previous ones.

The goal is to get simple but extensible system in various parts:
- support new types of tasks
- change storage for tasks (for example, replace the tasks file with some kind of database)
"""

import json
import subprocess
import urllib.request
from abc import ABC, abstractmethod
from collections import deque
from enum import StrEnum

# Tasks


class TaskType(StrEnum):
    HTTP = "http"
    EXEC = "exec"


class Task(ABC):
    def __init__(self, task_id: int):
        self.task_id = task_id

    @abstractmethod
    def execute(self) -> str:
        pass


class HttpTask(Task):
    def __init__(self, task_id: int, url: str):
        super().__init__(task_id)
        self.url = url

    def execute(self) -> str:
        response = urllib.request.urlopen(self.url)

        content = response.read()

        return f"status code {response.status}, content length {len(content)}"


class ExecTask(Task):
    def __init__(self, task_id: int, command: str):
        super().__init__(task_id)
        self.command = command

    def execute(self) -> str:
        result = subprocess.run(
            self.command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
        )

        return f"status code {result.returncode}, output: {result.stdout.strip()}"


# Task factory


class TaskFactory:
    @staticmethod
    def create(task_data: dict) -> Task:
        task_type = task_data["type"]

        if task_type == TaskType.HTTP:
            return HttpTask(
                task_id=task_data["task_id"],
                url=task_data["url"],
            )

        if task_type == TaskType.EXEC:
            return ExecTask(
                task_id=task_data["task_id"],
                command=task_data["command"],
            )

        raise ValueError(f"Unknown task type: {task_type}")


# Collectors


class Collector(ABC):
    @abstractmethod
    def collect(self) -> list[Task]:
        pass


class FileCollector(Collector):
    def __init__(self, filename: str):
        self.filename = filename

    def collect(self) -> list[Task]:
        tasks = []

        with open(self.filename) as f:
            for line in f:
                try:
                    task_data = json.loads(line)
                    task = TaskFactory.create(task_data)
                    tasks.append(task)

                except Exception as exc:
                    print(f"Invalid task '{line.strip()}': {exc}")

        return tasks


class DBCollector(Collector):
    def __init__(self, db_url: str):
        self.db_url = db_url

    def collect(self) -> list[Task]:
        raise NotImplementedError


# Scheduler


class TaskScheduler:
    def run(self, tasks: list[Task]) -> None:
        queue = deque(tasks)

        while queue:
            task = queue.popleft()

            try:
                result = task.execute()

                print(f"Task {task.task_id} " f"executed with result: {result}")

            except Exception as exc:
                print(f"Task {task.task_id} " f"failed with error: {exc}")

                queue.append(task)


# Main


def main():
    collector = FileCollector("tasks.json")

    tasks = collector.collect()

    scheduler = TaskScheduler()

    scheduler.run(tasks)


if __name__ == "__main__":
    main()
