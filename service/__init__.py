"""
Application Setup
"""
import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service import config
from service.common import log_handlers

# Create Flask application
app = Flask(__name__)
app.config.from_object(config)

# Apply Security Headers
talisman = Talisman(app)

# Enable CORS
CORS(app)

# Import routes and models
from service import routes, models
from service.common import error_handlers, cli_commands

# Logging Configuration
log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  ACCOUNT SERVICE RUNNING ".center(70, "*"))
app.logger.info(70 * "*")

try:
    models.init_db(app)
except Exception as error:
    app.logger.critical(f"Database Initialization Error: {error}")
    sys.exit(4)

app.logger.info("Service initialized!")
