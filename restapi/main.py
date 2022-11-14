from flask import Flask
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)


class GitHubRelese(Resource):
    def get(self, user, repo):
        res = requests.get(f"https://api.github.com/repos/{user}/{repo}/releases/latest")
        return res.json()["name"]


api.add_resource(GitHubRelese, "/<string:user>/<string:repo>")

if __name__ == "__main__":
    app.run()
