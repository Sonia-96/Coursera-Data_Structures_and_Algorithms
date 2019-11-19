# python3


from collections import namedtuple

AssignedJob = namedtuple('AssignedJob', ['worker', 'started_at'])


class JobQueue:
    def __init__(self, n_workers, jobs):
        self.n = n_workers
        self.jobs = jobs
        self.finish_time = []
        self.assigned_jobs = []
        for i in range(self.n):
            self.finish_time.append([i, 0])

    def SiftDown(self, i):
        min_index = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < self.n:
            if self.finish_time[min_index][1] > self.finish_time[left][1]:
                min_index = left
            elif self.finish_time[min_index][1] == self.finish_time[left][1]:
                if self.finish_time[min_index][0] > self.finish_time[left][0]:
                    min_index = left
        if right < self.n:
            if self.finish_time[min_index][1] > self.finish_time[right][1]:
                min_index = right
            elif self.finish_time[min_index][1] == self.finish_time[right][1]:
                if self.finish_time[min_index][0] > self.finish_time[right][0]:
                    min_index = right
        if min_index != i:
            self.finish_time[i], self.finish_time[min_index] = self.finish_time[min_index], self.finish_time[i]
            self.SiftDown(min_index)

    def NextWorker(self, job):
        root = self.finish_time[0]
        next_worker = root[0]
        started_at = root[1]
        self.assigned_jobs.append(AssignedJob(next_worker,started_at))
        self.finish_time[0][1] += job
        self.SiftDown(0)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    job_queue = JobQueue(n_workers, jobs)
    for job in jobs:
        job_queue.NextWorker(job)
    assigned_jobs = job_queue.assigned_jobs

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
