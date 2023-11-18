import torch
from PIL import Image
import torchvision.transforms as transforms
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Run inference on a single image.')
parser.add_argument('img_path', type=str, help='Path to the image file.')
args = parser.parse_args()

path = r'ModelSaves\M1_epoch_138_loss_1.5287_vloss1.5153_acc_0.9471_vacc0.9527.pt'

model = torch.load(path)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

transform = transforms.Compose([
    transforms.Resize((16, 128)),
    transforms.Grayscale(),
    transforms.ToTensor(),
    transforms.Lambda(lambda x: x.clamp(0, 1))
])

# Load the data
input_img = Image.open(args.img_path)
input_img = transform(input_img)

with torch.no_grad():
    input_img = input_img.to(device)
    output = model(input_img.unsqueeze(0))
    _, predicted = torch.max(output, 1)
    predicted_label = predicted.item()

print(f'Prediction: {predicted_label} (Confidence: {torch.max(output)})')
