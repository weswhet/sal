from django.apps import AppConfig
from watson import search as watson

class ServerAppConfig(AppConfig):
    name = "server"
    def ready(self):
        Machine = self.get_model("Machine")
        Fact = self.get_model("Fact")
        Condition = self.get_model("Condition")
        watson.register(Machine, exclude=("report", "errors", "warnings",))
        watson.register(Fact)
        watson.register(Condition)