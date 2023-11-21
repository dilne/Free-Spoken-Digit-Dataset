import torch
from PIL import Image
import torchvision.transforms as transforms
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Run inference on a single image.')
parser.add_argument('img_path', type=str, help='Path to the image file.')
args = parser.parse_args()

path = r'ModelSaves\M2\M2_epoch_271_loss_1.4690_vloss1.5069_acc_0.9571_vacc0.9696.pt'

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
