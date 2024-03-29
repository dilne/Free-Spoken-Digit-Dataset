<h1 align="center">🔢Audio MNIST Classification on the Free Spoken Digit Dataset🔊</h1>
This project is the MNIST equivalent for audio. The dataset contains recordings of speakers saying numbers 0 to 9. The data is converted to mel spectograms and classified using a modified ResNet18 model.

## Dataset
Free Spoken Digit Dataset (FSDD) is a simple audio/speech dataset consisting of recordings of spoken digits in wav files. The dataset contains approximately 20 MB of 1,500 recordings of spoken digits from 0 to 9. Each digit was spoken by 50 different speakers, and each speaker spoke each digit five times. The recordings are trimmed so that they have near minimal silence at the beginnings and ends. 

FSDD is an open dataset, which means it will grow over time as data is contributed. It is a useful dataset for speech recognition tasks and can be thought of as an audio version of the popular MNIST dataset which consists of hand-written digits.

![alt text](https://github.com/dilne/Free-Spoken-Digit-Dataset/blob/main/Mel%20Spectogram%20Example.png?raw=true "Mel Spectogram Example")

## Training
[Notebook](https://github.com/dilne/Free-Spoken-Digit-Dataset/blob/main/TrainAndTest%20-%20CNN.ipynb)

<a href="https://colab.research.google.com/github/dilne/Free-Spoken-Digit-Dataset/blob/main/TrainAndTest%20-%20CNN.ipynb" target="_blank">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

- Imput data: Mel spectograms (2400 train, 600 test)
- Model: Modified ResNet18 model
- Total epochs: 300
- LR: 0.001, step size 20, gamma 0.9
- Loss: 1.4690
- Val Loss: 1.5069
- Accuracy: 0.9571
- Val Acc: 0.9696

Best epoch (highest validation accuracy):
- Epoch: 271
- Precision: 0.9691420399131312
- Recall: 0.9694164524957861
- F1 score: 0.9690412348965143

![alt text](https://github.com/dilne/Free-Spoken-Digit-Dataset/blob/main/Metrics.png?raw=true "Model Metrics")

## Inference
You can use the trained model to run inference on a single mel spectogram image using:</br>
```python inference.py Data\Mel\0\0_george_0.png```

Output:</br>
```Prediction: 0 (Confidence: 0.9999996423721313)```

## Future steps
- Any empty signal at the beginning or end of each clip is removed, however, this does not mean noise before and after the section of the desired signal is removed. To fix, the data could be passed through a noise gate to remove noise before and after the desired signal while not affecting it.
- The model should be modified to allow input of different lengths withou having to resize them
