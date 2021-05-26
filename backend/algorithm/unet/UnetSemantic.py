import os

import numpy as np
import torch
import torch.nn.functional as F
from PIL import Image
from torchvision import transforms

from algorithm.unet.unet.unet_model import UNet
from algorithm.unet.utils.dataset import BasicDataset


def predict_img(net,
                full_img,
                device,
                scale_factor=1,
                out_threshold=0.5):
    net.eval()

    img = torch.from_numpy(BasicDataset.preprocess(full_img, scale_factor))

    img = img.unsqueeze(0)
    img = img.to(device=device, dtype=torch.float32)

    with torch.no_grad():
        output = net(img)

        if net.n_classes > 1:
            probs = F.softmax(output, dim=1)
        else:
            probs = torch.sigmoid(output)

        probs = probs.squeeze(0)

        tf = transforms.Compose(
            [
                transforms.ToPILImage(),
                transforms.Resize(full_img.size[1]),
                transforms.ToTensor()
            ]
        )

        probs = tf(probs.cpu())
        full_mask = probs.squeeze().cpu().numpy()

    return full_mask > out_threshold


def get_output_filenames(args):
    out_path = ''
    input_split = os.path.splitext(args)
    name_split = input_split[0].split("/")
    for i in range(len(name_split) - 1):
        out_path = out_path + name_split[i] + "/"
    out_path = out_path + '{}_out{}'.format(name_split[-1], input_split[1])
    return out_path


def mask_to_image(mask):
    return Image.fromarray((mask * 255).astype(np.uint8))


def unet_semantic(img_path):
    in_files = img_path
    out_path = get_output_filenames(img_path)
    # model_path = "MODEL.pth"
    model_path = os.path.dirname(__file__) + "/MODEL.pth"
    pretrained = torch.load(model_path)
    net = UNet(n_channels=3, n_classes=1)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net.to(device=device)
    net.load_state_dict(torch.load(model_path, map_location=device))

    img = Image.open(in_files)

    mask = predict_img(net=net,
                       full_img=img,
                       scale_factor=0.5,
                       out_threshold=0.5,
                       device=device)

    result = mask_to_image(mask)
    result.save(out_path)
    return out_path
