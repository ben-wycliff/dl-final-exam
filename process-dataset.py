# import packages
import os
import logging
import shutil
import glob 

def main():
    logging.basicConfig(filename="pipeline.log",
                         level=logging.INFO,
                           format='%(asctime)s %(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())
    # explore data folders
    data_path = "./archive"
    folders = os.listdir(data_path)
    classes = set([i.split(" ")[0] for i in  folders])
    
    # Merge all images into their respective classes
    for category in classes:
        os.makedirs(f"dataset/{category}", exist_ok=True)
    for i, src in enumerate(glob.glob("./archive/*/*")):
        name = src.split("/")[2]
        category = name.split(" ")[0]
        file = f"img{i}"+src.split("/")[-1]
        # print(category)
        dst = os.path.join("dataset", category, file)
        print(f"Copying {file} from {src} to {dst}")
        shutil.copy(src, dst)

    # Create partitions
    for categor in classes:
        os.makedirs(f"./data/train/{categor}", exist_ok=True)
        os.makedirs(f"./data/val/{categor}", exist_ok=True)
        os.makedirs(f"./data/test/{categor}", exist_ok=True)

if __name__ == "__main__":
    main()