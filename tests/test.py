# flask_app_docker_template/tests/test.py
from app.lib.internal.get_data_stream import get_data_stream

# Utilisez la fonction importée
result = get_data_stream()
print(result)
