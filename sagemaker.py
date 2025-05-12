from cortexutils.analyzer import Analyzer
import requests
import json

class SageMakerAnalyzer(Analyzer):

    def __init__(self):
        Analyzer.__init__(self)
        self.api_key = self.get_param('config.apiKey', None, "Missing API key")

    def run(self):
        try:
            hostname = self.getData().strip()
            result = self.scan_hostname(hostname)
            self.report(result)
        except Exception as e:
            self.error(str(e))
    
    def scan_hostname(self, hostname):
        # Code
        print(hostname)
        if not self.api_key:
            raise ValueError("API key is missing.")
        return {"message": f"Processed hostname: {hostname}"}
        # Code

if __name__ == "__main__":
    SageMakerAnalyzer().run()