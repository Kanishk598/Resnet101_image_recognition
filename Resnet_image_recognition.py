# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
from torchvision import models, transforms
import sys
path = 'Small Dataset/' + str(sys.argv[1])

# %%
resnet = models.resnet101(pretrained=True)
#resnet 
preprocess = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(), transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

# %%
from PIL import Image
img = Image.open(path)
img.show()


# %%
import torch
img_t = preprocess(img)
batch_t = torch.unsqueeze(img_t, 0)


# %%
resnet.eval()
out = resnet(batch_t)
#out
with open('imagenet_classes.txt') as f:
    labels = [line.strip() for line in f.readlines()]
_, index = torch.max(out, 1)
percentage = 100*torch.nn.functional.softmax(out, dim=1)[0]
print(labels[index[0]])
print(percentage[index[0]].item())


# %%



