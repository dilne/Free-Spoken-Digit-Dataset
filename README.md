<h1 align="center">Audio MNIST Classification on the Free Spoken Digit Dataset</h1>
This project is the MNIST equivalent for audio.

## Dataset
Free Spoken Digit Dataset (FSDD) is a simple audio/speech dataset consisting of recordings of spoken digits in wav files. The dataset contains approximately 20 MB of 1,500 recordings of spoken digits from 0 to 9. Each digit was spoken by 50 different speakers, and each speaker spoke each digit five times. The recordings are trimmed so that they have near minimal silence at the beginnings and ends. 

FSDD is an open dataset, which means it will grow over time as data is contributed. It is a useful dataset for speech recognition tasks and can be thought of as an audio version of the popular MNIST dataset which consists of hand-written digits.

## Training
[Notebook](https://github.com/dilne/Free-Spoken-Digit-Dataset/blob/main/TrainAndTest%20-%20CNN.ipynb)
- Data: Mel spectograms
- Model: Modified ResNet18 model
- Epochs: 160
- LR: 0.001, step size 20, gamme 0.9
- Loss: 1.5287
- Val Loss: 1.5153
- Accuracy: 0.9471
- Val Acc: 0.9527

## Inference
You can use the trained model to run inference on a single mel spectogram image using:</br>
```python inference.py Data\Mel\0\0_george_0.png```
