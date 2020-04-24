import json

from commons import get_model

# Custom Imports 
import numpy as np
import PIL.Image as Image
import torchvision.transforms.functional as F

# Access commons
model = get_model()

def get_prediction(file):
    img = 255.0 * F.to_tensor(Image.open(file).convert('RGB'))
    img[0,:,:]=img[0,:,:]-92.8207477031
    img[1,:,:]=img[1,:,:]-95.2757037428
    img[2,:,:]=img[2,:,:]-104.877445883
    img = img.cpu()
    output = model(img.unsqueeze(0))
    prediction = int(output.detach().cpu().sum().numpy())
    print("Predicted Count : ",int(output.detach().cpu().sum().numpy())) # Output the prediction
    return prediction