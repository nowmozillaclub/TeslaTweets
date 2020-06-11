<p align="center"><img height="400" width="400" src="./branding/icon.jpg" alt="TeslaTweets"/></p>

# TeslaTweets

[![Stars](https://img.shields.io/github/stars/nowmozillaclub/TeslaTweets.svg)](https://github.com/nowmozillaclub/TeslaTweets/stargazers)
[![Forks](https://img.shields.io/github/forks/nowmozillaclub/TeslaTweets.svg)](https://github.com/nowmozillaclub/TeslaTweets/network/members)
[![Issues](https://img.shields.io/github/issues/nowmozillaclub/TeslaTweets.svg)](https://github.com/nowmozillaclub/TeslaTweets/issues)
[![License](https://img.shields.io/github/license/nowmozillaclub/TeslaTweets.svg)](https://opensource.org/licenses/GPL-3.0)

TeslaTweets is a project where we try to predict whether Tesla's stock price will rise or fall based on Elon Musk's twitter data by using Machine Learning techniques and Natural Language Processing.

## Datasets

1. The [tweets dataset](datasets/data_elonmusk.csv) contains all of Elon Musk's tweets from November 16, 2012 to September 29, 2017. This dataset was taken from [Kaggle](https://www.kaggle.com/kulgen/elon-musks-tweets).
2. The [stock price](datasets/tsla_stock_price.csv) was extracted using [pandas_datareader](https://pandas-datareader.readthedocs.io/en/latest/). Refer to the [code](datasets/extract_tsla_stock_price.py) for more information. This contains Date, Open, Close, Low, High prices and the Volume for Tesla's stock from November 16, 2012 to September 29, 2017.

## Building

To build and run the project on your device, do the following:

- Install Anaconda by following the instructions on their [website](https://www.anaconda.com/) and make sure you have Jupyter Notebooks. Alternatively you can also use [Google Colab](https://colab.research.google.com/).
- Clone this repo to your local machine using `https://github.com/nowmozillaclub/TeslaTweets.git`.
- Start Jupyter Notebook in the project directory and you are free to explore the codebase. For Google Colab, you will have to upload the file on your Google Drive and then you can start exploring.

## Contributing

Please read the [CONTRIBUTING.md](CONTRIBUTING.md) file for more details on how to contribute.

## Credits

This project is developed by a bunch of engineering students at NMIMS MPSTME, Mumbai. Take a look at the entire list of [contributors](https://github.com/nowmozillaclub/TeslaTweets/graphs/contributors) to see who all have helped with the project. The image on top is a photo by [Roberto Nickson](https://unsplash.com/@rpnickson?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on Unsplash.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
