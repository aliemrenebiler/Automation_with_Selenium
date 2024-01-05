"File Utils"


def save_file(content: str, file_path: str):
    "Saves the content as a file to the specified path"

    with open(file_path, "w", encoding="utf8") as file:
        file.write(content)
