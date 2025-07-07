from flask import Response
import time

start_time = time.time()


def metrics():
    uptime = int(time.time() - start_time)
    return Response(
        f"""# HELP devops_uptime_seconds Time the service has been running
# TYPE devops_uptime_seconds counter
devops_uptime_seconds {uptime}
""",
        mimetype="text/plain"
    )

