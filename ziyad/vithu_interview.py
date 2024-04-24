"""
- large scale system
- task scheduler with priorities and dependencies
- job scheduler with priority and dependency support
- support scheduling a job, list of dependencies, priority
"""

import heapq


class Job:
    def __init__(self, job_id: int, priority: float, dependencies: List[Job]):
        self.job_id = job_id
        self.priority = priority
        self.dependencies = dependencies

    def execute(self):
        pass


class JobScheduler:
    def __init__(self):
        self.jobs = Graph[jobs]

    def enqueue_job(self, job: Job):
        logger.warning("Enqueued job: {}".format(job.id))
        self.jobs.enqueue_with_dependencies(job)

    def fetch_next_job(self) -> Job:
        # pass

    def is_completed(self, job: Job) -> Job:
        # pass


job1 = Job(priority=1, dependencies=[])
job2 = Job(priority=1, dependencies=[job1])

scheduler = JobScheduler()
scheduler.enqueue_job(job=job1)
scheduler.enqueue_job(job=job2)
