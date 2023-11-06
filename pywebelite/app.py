from server import Server
from router import Router

app = Server()

def index(request):
    return "Hello, World!"

router = Router()
router.add_route('/', index)

app.run(router)
