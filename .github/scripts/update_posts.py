import os
import json
from datetime import datetime

def extract_metadata_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    metadata = {}
    in_metadata = False

    for line in lines:
        line = line.strip()

        if line == "---":
            if in_metadata:
                break
            else:
                in_metadata = True
            continue

        if in_metadata and line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip()

    return metadata

categories_dir = "categories"
posts_dir = "posts"
posts_file = "posts.json"

for subdir in os.listdir(categories_dir):

    subdir_path = os.path.join(categories_dir, subdir) # EX) categories/daily, categories/miscellaneous

    if not os.path.isdir(subdir_path): # if it's not a dir (so it is a file) skip.
        continue

    posts_dir_path = os.path.join(subdir_path, posts_dir) # EX) categories/daily/posts, categories/miscellaneous/posts
    
    posts_json = os.path.join(subdir_path, posts_file) # EX) categories/daily/posts.json, categories/miscellaneous/posts.json

    data = []
    
    posts_list = os.listdir(posts_dir_path)

    for post_file in posts_list:
        post_file_path = os.path.join(posts_dir_path, post_file)

        metadata = extract_metadata_from_md(os.path.join(post_file_path))

        file_name_without_ext = os.path.splitext(post_file)[0]
        
        metadata["path"] = f"{subdir}/{file_name_without_ext}"
        metadata["hidden"] = metadata.get("hidden", "false").lower() == "true"

        data.append(metadata)

    data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y.%m.%d %H:%M'), reverse=True)

    print(data)


    with open(posts_json, 'w') as f:
        json.dump({"posts": data}, f, indent=4)
