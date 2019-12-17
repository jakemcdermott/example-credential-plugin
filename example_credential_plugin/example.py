from collections import namedtuple


def backend(**inputs):
    # inputs is a dictionary of key-value pairs for the fields and metadata.
    # e.g. inputs["url"], inputs["token"], inputs["secret_key"].
    return "secret"


example_plugin = namedtuple("CredentialPlugin", ["name", "inputs", "backend"])(
    "Example",
    inputs={
        "fields": [
            {
                "id": "url",
                "label": "Server URL",
                "type": "string",
            },
            {
                "id": "token",
                "label": "Authentication Token",
                "type": "string",
                "secret": True,
            },
        ],
        "metadata": [
            {
                "id": "secret_key",
                "label": "Secret Key",
                "type": "string",
                "help_text": "The value of the key in My Credential System to fetch.",
            }
        ],
        "required": ["url", "token", "secret_key"],
    },
    backend=backend,
)
