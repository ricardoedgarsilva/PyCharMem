<a name="readme-top"></a>

[![Issues][issues-shield]][issues-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Contributors][contributors-shield]][contributors-url]
[![GPL License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
  <p align="center">
    <br />
    <a href="https://github.com/ricardoedgarsilva/PyCharMem"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ricardoedgarsilva/PyCharMem">View Demo</a>
    ·
    <a href="https://github.com/ricardoedgarsilva/PyCharMem/issues">Report Bug</a>
    ·
    <a href="https://github.com/ricardoedgarsilva/PyCharMem/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

PyCharMem is a Python program that allows you to measure the charge memory of a device. The program measures the charge memory of a device under different conditions, which are specified in a configuration file.

The program has been developed by Ricardo E. Silva and is licensed under the GNU General Public License v3.0. The source code is available on GitHub.

PyCharMem provides a command-line interface (CLI) that allows you to select a measurement type, enter measurement parameters, and run a measurement. The program also has a GUI that provides real-time visualization of the measurement results.

PyCharMem was developed as part of a research project at INESC-MN Lisbon, Portugal.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python-url]
* [![Rich][Rich]][Rich-url]
* [![InquirerPy][InquirerPy]][InquirerPy-url]
* [![PyQt6][PyQt6]][PyQt6-url]
* [![PyQtGraph][PyQtGraph]][PyQtGraph-url]
* [![PyVISA][PyVISA]][PyVISA-url]
* [![YAML][YAML]][YAML-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In order to get started clone the repository and install the required dependencies.

### Prerequisites

PyCharMem can run in every operating system that supports Python 3.6 or higher. The following instructions will guide you through the process of installing Python 3.6 or higher. Then you will need to get an National Instruments GPIB card and install the NI-VISA drivers. If your instrument is not in `/measurements` folder you will need to create an API for it.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

After cloning the repository, you will need to install the required dependencies. The following instructions will guide you through the process.

  ```sh
    pip install -r requirements.txt
  ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

In order to run the program open a terminal window and run the following command:

  ```sh
    python PyCharMem.py
  ```

_For more, please refer to the manual.pdf

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Add changelog
- [ ] Add manual
- [ ] Add more measurements


See the [open issues](https://github.com/ricardoedgarsilva/PyCharMem/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/ricardoedgarsilva/PyCharMem](https://github.com/ricardoedgarsilva/PyCharMem)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!


* [GNU Licence V3](https://choosealicense.com/licenses/gpl-3.0/)
* [Rich](https://pypi.org/project/rich/)
* [InquirerPy](https://pypi.org/project/inquirerpy/)
* [PyQt6](https://pypi.org/project/PyQt6/)
* [PyQtGraph](https://pypi.org/project/pyqtgraph/)
* [PyVISA](https://pypi.org/project/PyVISA/)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ricardoedgarsilva/PyCharMem/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/ricardoedgarsilva/PyCharMem/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/ricardoedgarsilva/PyCharMem/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/ricardoedgarsilva/PyCharMem/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://www.gnu.org/licenses/gpl-3.0.en.html
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[Python-url]: https://www.python.org/
[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[GNU-url]: https://www.gnu.org/licenses/gpl-3.0.en.html
[GNU]: https://img.shields.io/badge/License-GPLv3-blue.svg
[Rich-url]: https://pypi.org/project/rich/
[Rich]: https://img.shields.io/badge/Rich-000000?style=for-the-badge&logo=rich&logoColor=white
[InquirerPy-url]: https://pypi.org/project/inquirerpy/
[InquirerPy]: https://img.shields.io/badge/InquirerPy-000000?style=for-the-badge&logo=inquirerpy&logoColor=white
[PyQt6-url]: https://pypi.org/project/PyQt6/
[PyQt6]: https://img.shields.io/badge/PyQt6-000000?style=for-the-badge&logo=pyqt6&logoColor=white
[PyQtGraph-url]: https://pypi.org/project/pyqtgraph/
[PyQtGraph]: https://img.shields.io/badge/PyQtGraph-000000?style=for-the-badge&logo=pyqtgraph&logoColor=white
[PyVISA-url]: https://pypi.org/project/PyVISA/
[PyVISA]: https://img.shields.io/badge/PyVISA-000000?style=for-the-badge&logo=pyvisa&logoColor=white
[YAML-url]: https://yaml.org/
[YAML]: https://img.shields.io/badge/YAML-000000?style=for-the-badge&logo=yaml&logoColor=white