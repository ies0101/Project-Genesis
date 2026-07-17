import json
from pathlib import Path

memory_file = Path("kang/memory/creator_memory.json")


def load_creator():
    memory_data = memory_file.read_text(encoding="utf=8")
    creator_data = json.loads(memory_data)

    return creator_data


def get_creator_name():
    creator_data = load_creator()

    return creator_data["name"]


def save_creator_name(creator_name):
    creator_data = load_creator()

    creator_data["name"] = creator_name


    memory_file.write_text(
        json.dump(creator_data, ensure_ascii=False, indent=4),
        encoding="utf=8"
    )

def add_creator_memory(memory):
    creator_data = load_creator()


    if memory not in creator_data["memories"]:

       creator_data["memories"].append(memory)
       memory_file.write_text(
           json.dumps(creator_data, ensure_ascii=False, indent=4),
           encoding="utf=8"
       )


def get_creator_memories():
    creator_data = load_creator()

    return creator_data["memories"]