import os
from first_server import mcp

port = int(os.environ.get("PORT", 8000))

app = mcp.streamable_http_app()
