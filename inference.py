import json

from commons import get_model

# Custom Imports 
import numpy as np
import PIL.Image as Image
from torchvision import transforms
import matplotlib.pyplot as plt
import random

# Access commons
model = get_model()
# Standard RGB transform
transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),])
def get_prediction(file):
    img = transform(Image.open(file).convert('RGB'))
    img = img.cpu()
    output = model(img.unsqueeze(0))
    prediction = int(output.detach().cpu().sum().numpy())
    x = random.randint(1,100000) 
    density = 'static/density_map'+str(x)+'.jpg' 
    plt.imsave(density, output.detach().cpu().numpy()[0][0]) 
    return prediction, density