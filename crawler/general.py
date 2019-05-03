import os
from shutil import rmtree

CRAWLER_OUTPUT = "crawler_output/"


def create_project_dir(directory):
    if os.path.exists(directory):
        rmtree(directory)

    print("Creating project {} ...".format(directory))
    os.makedirs(directory)


def create_data_files(project_name, base_url):  # base_url - starting point
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_new_file(queue, base_url)

    if not os.path.isfile(crawled):
        write_new_file(crawled, '')


# Create queue and crawled files ( if not created)
def write_new_file(path_file, data):
    f = open(path_file, 'w', encoding="utf-8")
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a', encoding="utf-8") as file:
        file.write(data + "\n")


# Delete the content of a file
def delete_file_content(path):
    if os.path.exists(path):
        with open(path, 'w'):
            pass


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, "rt", encoding="utf-8") as f:  # Read text file
        for line in f:
            results.add(line.replace("\n", ''))
    return results


# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)
