from waitress import serve
import api
import logging
logger = logging.getLogger('waitress')
logger.setLevel(logging.INFO)
serve(api.app, host='0.0.0.0', port=8081)