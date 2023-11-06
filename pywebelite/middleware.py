class MiddlewareManager:
    def __init__(self):
        self.middlewares = []

    def add_middleware(self, middleware):
        self.middlewares.append(middleware)

    def process_request(self, request):
        for middleware in self.middlewares:
            request = middleware.process_request(request)
        return request

class Middleware:
    def process_request(self, request):
        # Perform tasks like authentication, logging, or request modification
        return request
