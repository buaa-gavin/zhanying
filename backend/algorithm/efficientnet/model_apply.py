import torch
from PIL import Image
from torchvision import transforms

from efficientnet import EfficientNet

device = torch.device('cuda')

transform = transforms.Compose([
    transforms.Resize(224),  # 压缩成224*224
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


def apply(img_path):
    net = EfficientNet.from_name("efficientnet-b6", num_classes=3)
    pretrained = torch.load('effb6.pth')
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
    print('诊断结果: ', classify[int(predicted[0])])
    return int(predicted[0])


if __name__ == '__main__':
    apply('./image/malignant (176).png')

    # total = 0
    # for i in range(168, 211):
    #     if apply('../image/malignant ({}).png'.format(i)) == 0:
    #         total += 1
    # for i in range(108, 134):
    #     if apply('../image/normal ({}).png'.format(i)) == 1:
    #         total += 1
    # for i in range(351, 438):
    #     if apply('../image/benign ({}).png'.format(i)) == 2:
    #         total += 1
    # print(total/156)
