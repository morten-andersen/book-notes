### Programming Machine Learning

**Paolo Perrotta** [*Programming Machine Learning*](https://pragprog.com/titles/pplearn/programming-machine-learning/)

Hands on introduction to machine learning with focus on *supervised learning* and the *deep learning* "explosion" after 2012

* **CNN - Convolutional Neural Network** (2012) - perfect for image *recognition*
* **GAN - Generative Adversarial Network** (2014)- for image *creation*
* **RNN - Recurrent Neural Network** - perfect for processing of language and sentences where "context" / "memory" is required

[![Programming Machine Learning - 1](machine-learning-2020_1.jpg "Programming Machine Learning - 1")](machine-learning-2020_1.jpg)
[![Programming Machine Learning - 2](machine-learning-2020_2.jpg "Programming Machine Learning - 2")](machine-learning-2020_2.jpg)

#### OpenAI / ChatGPT / Transformers

* [ChatGPT is everywhere. Here’s where it came from](https://www.technologyreview.com/2023/02/08/1068068/chatgpt-is-everywhere-heres-where-it-came-from/?truid=c391fa75ffdab20bb629e835d3d227ce&mc_cid=7c70f2d30e)
  * traditionally language models have been using RNN (recurrent neural networks)
  * in 2017 a group of Google researchers invented *transformers* - described in [Attention Is All You Need](https://papers.nips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
* [How ChatGPT actually works](https://www.assemblyai.com/blog/how-chatgpt-actually-works/)
* [How does ChatGPT work? Tracing the evolution of AIGC](https://www.dtonomy.com/how-does-chatgpt-work/)

#### Software

* [Jupyter](https://jupyter.org/) - machine learning *notebooks* with a mix of text, live code, visualizations, etc.
* [Keras](https://keras.io/) simple API on top of Tensorflow
* [Tensorflow](https://www.tensorflow.org/) - machine learning library  developed by Google
* [PyTorch](https://pytorch.org/) - machine learning library  developed by Facebook
* [Teachable Machine](https://teachablemachine.withgoogle.com/) - can be used for quick'n'dirty online training of a model that can be exported to TensorFlow
* [scikit-learn](https://scikit-learn.org) - an alternative open source ML library. The documentation about [Choosing the right estimator](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html) contains a very informative interactive "cheat-sheet"
[![scikit-learn - cheat-sheet](scikit-learn.png "scikit-learn - cheat-sheet")](scikit-learn.png)

#### Hardware

* [Coral](https://www.coral.ai/) - Google's offering of small IoT components with AI support out-of-the box.

#### Setup using Miniconda

* install [Miniconda](https://docs.conda.io/en/latest/miniconda.html), a minimal Conda distribution
* create an environment `conda create --name=machinelearning python=3`
* install packages
```bash
conda install numpy=1.15.2
conda install matplotlib=3.1.2
conda install seaborn=0.9.0
conda install scikit-learn=0.22.1
conda install keras=2.2.4
conda install jupyter==1.0.0
```

#### Activate Environment

```bash
conda update -n base -c defaults conda
conda activate machinelearning
```

#### Start jupyter Notebook

`jupyter notebook`
