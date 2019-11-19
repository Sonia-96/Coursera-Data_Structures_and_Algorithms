# python3


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = query[1]
        if self.type == "add":
            self.name = query[2]


def WriteResponses(result):
    print('\n'.join(result))


def ProcessQuery(query, contacts):
    if query.type == "add":
        contacts[query.number] = query.name
    elif query.type == "del":
        if contacts.__contains__(query.number):
            del contacts[query.number]
    else:
        response = 'not found'
        if contacts.__contains__(query.number):
            response = contacts[query.number]
        return response


n_queries = int(input())
contacts = {}
for _ in range(n_queries):
    query = Query(input().split())
    result = ProcessQuery(query, contacts)
    if result:
        print(result)
