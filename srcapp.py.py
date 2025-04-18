from flask import Flask
from .extensions import redis_manager

class App(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_manager = redis_manager
        self.redis_manager.init_app(self)

def create_app(config=None) -> App:
    app = App(__name__)
    
    if config:
        app.config.update(config)
    
    @app.teardown_appcontext
    def shutdown_redis(exception=None):
        app.redis_manager.close()
    
    return app