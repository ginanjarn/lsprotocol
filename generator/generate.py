import json
import sys
from pathlib import Path

from metamodel_loader import load_meta_model
from py_generator import CodeGenerator

# add this parent directory to sys.path
sys.path.append(str(Path(__file__).parent))


def main():
    this_folder = Path(__file__).parent
    path = this_folder / "metaModel.json"
    metamodel = json.loads(path.read_text(encoding="utf-8"))
    model = load_meta_model(metamodel)

    gen = CodeGenerator(model)
    gen.generate()

    init_path = this_folder.parent / "__init__.py"
    init_path.touch()

    types_path = this_folder.parent / "lsprotocol.py"
    types_path.write_text(gen.types_code, encoding="utf-8")

    server_path = this_folder.parent / "server.py"
    server_path.write_text(gen.server_code, encoding="utf-8")

    client_path = this_folder.parent / "client.py"
    client_path.write_text(gen.client_code, encoding="utf-8")


if __name__ == "__main__":
    main()
