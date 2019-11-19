# python3


from collections import namedtuple
import collections


Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = collections.deque(maxlen=size)

    def process(self, request):
        while len(self.finish_time) > 0:
            if self.finish_time[0] <= request.arrived_at:
                self.finish_time.popleft()
            else:
                break
        packets = len(self.finish_time)
        if packets == self.size:
            return Response(True, -1)
        if packets == 0:
            started_at = request.arrived_at
        else:
            started_at = self.finish_time[packets - 1]
        finished_at = started_at + request.time_to_process
        self.finish_time.append(finished_at)
        return Response(False, started_at)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
