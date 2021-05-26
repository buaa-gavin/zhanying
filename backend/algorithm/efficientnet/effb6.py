import os

import torch
from PIL import Image
from torchvision import transforms

from .efficientnet import EfficientNet

device = torch.device('cuda')

transform = transforms.Compose([
    transforms.Resize(224),  # 压缩成224*224
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


def effb6_apply(img_path):
    net = EfficientNet.from_name("efficientnet-b6", num_classes=3)
    modelpath = os.path.dirname(__file__) + "/effb6.pth"
    pretrained = torch.load(modelpath)
    net.load_state_dict(pretrained)  # 加载模型
    net.eval()  # 注意！！一定要加这个,不启用Batch Normalization和Dropout
    # print(net.state_dict)
    net = net.to(device)
    torch.no_grad()
    img = Image.open(img_path)  # 打开
    img = transform(img).unsqueeze(0)  # 变形
    # print(img.size())
    image = img.to(device)
    # print(image.shape)
    outputs = net(image)
    # print(outputs)
    _, predicted = torch.max(outputs, 1)
    classify = ['恶性肿瘤', '正常', '良性肿瘤']
    return classify[int(predicted[0])]

# if __name__ == "__main__":
#     effb6_apply("C:\\Users\\Stone Hana Yang\\Desktop\\Detection\\demo1\\media\\images\\20210324\\malignant_16.png")
