"""Encaminha logs ERROR para a New Relic sem ativar APM."""
import json, logging, os, platform, traceback, urllib.request

class NewRelicLogHandler(logging.Handler):
    def __init__(self, service_name):
        super().__init__(logging.ERROR)
        self.service_name = service_name
        self.key = os.environ.get("NEW_RELIC_LICENSE_KEY", "").strip()
        self.url = os.environ.get("NEW_RELIC_LOG_API_URL", "https://log-api.newrelic.com/log/v1").strip()

    def emit(self, record):
        if not self.key:
            return
        try:
            message = record.getMessage()
            if record.exc_info:
                message += "\n" + "".join(traceback.format_exception(*record.exc_info))
            body = json.dumps({
                "service.name": self.service_name, "environment": os.environ.get("APP_ENV", "production"),
                "hostname": platform.node(), "level": record.levelname, "logger": record.name,
                "message": message[:32000],
            }).encode()
            req = urllib.request.Request(self.url, body, {"Api-Key": self.key, "Content-Type": "application/json"}, method="POST")
            urllib.request.urlopen(req, timeout=2).close()
        except Exception:
            pass

def configure_new_relic_logs(service_name):
    root = logging.getLogger()
    if not any(isinstance(item, NewRelicLogHandler) for item in root.handlers):
        root.addHandler(NewRelicLogHandler(service_name))
