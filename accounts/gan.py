import torch
import matplotlib.pyplot as plt
from torchvision.utils import make_grid
from torchvision.utils import save_image

import os

def denorm(img_batch):
    stats = (0.5, 0.5, 0.5), (0.5, 0.5, 0.5)
    return img_batch * stats[1][0] + stats[0][0]

def load_checkpoint(filepath):
    checkpoint = torch.load(filepath,map_location=torch.device('cpu'))
    model = checkpoint['gen']
    model.load_state_dict(checkpoint['gen_state_dict'])
    for parameter in model.parameters():
        parameter.requires_grad = False
    
    model.eval()
    
    return model

def generateAnimeFace():
    generator = load_checkpoint('checkpoint_gen.pth')
    noise = torch.randn(8,128, 1, 1)
    fake_image_batch = generator(noise)
    fake_image_batch = denorm(fake_image_batch)
    for i in range(8):        
        save_image(fake_image_batch[i],'static/generated-images/{}.png'.format(i))  