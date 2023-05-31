import os.path

FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


JSON_SCHEMA_POST = get_path(filename="schema_03_post.json")
JSON_SCHEMA_POSTS = get_path(filename="schema_03_posts.json")
JSON_SCHEMA_RANDOM = get_path(filename="schema_01_random.json")
JSON_SCHEMA_IMAGES = get_path(filename="schema_01_images.json")
CSV_DATA_01 = get_path(filename="data_01_dog.csv")
CSV_DATA_02 = get_path(filename="data_02_pivo.csv")
CSV_DATA_03 = get_path(filename="data_03_json_placeholder.csv_.csv")
