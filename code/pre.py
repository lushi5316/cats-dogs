import glob
import os
import random


# train_img = glob.glob("../data/train/*jpg")
# print(len(train_img))
# for i in train_img:
#     if "cat" in i:
#         os.rename(i, i.replace("train","train/cat"))
#     else:
#         os.rename(i, i.replace("train","train/dog"))

# ramdon.seed(10)

train_cat = glob.glob("../data/train/cat/*jpg")
for i in range(12500):
    if i <= (12500*0.2):
        os.rename(train_cat[i],train_cat[i].replace("train","valid"))

train_cat = glob.glob("../data/train/dog/*jpg")
for i in range(12500):
    if i <= (12500*0.2):
        os.rename(train_cat[i],train_cat[i].replace("train","valid"))
