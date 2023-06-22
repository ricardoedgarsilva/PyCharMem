<a name="readme-top"></a>



<!-- Header -->
<br />
  <p align="center">
    <br />
    <a href="https://github.com/ricardoedgarsilva/PyCharMem"><strong>Explore the docs »</strong></a>
    <br />
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

PyCharMem is a robust Python-based software, engineered to perform electrical characterization on memristive devices. It conducts these measurements under a range of conditions dictated by a user-configured file, thereby offering a great deal of flexibility and control.

Developed by Ricardo E. Silva, PyCharMem is openly licensed under the GNU General Public License v3.0, with the source code readily accessible on GitHub, promoting transparency and community-based enhancements.

PyCharMem furnishes both a command-line interface (CLI) and a graphical user interface (GUI). The CLI permits users to select a specific measurement type, key in the necessary parameters, and initiate the measurement. Simultaneously, the GUI presents an intuitive platform for real-time results visualization, enhancing user understanding and interaction.

The inception of PyCharMem traces back to a comprehensive research project at INESC-MN Lisbon, Portugal, a testament to its scientific rigor and reliability.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Python][Python]][Python-url]
* [![YAML][YAML]][YAML-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites


PyCharMem is compatible with all operating systems that support Python 3.9 or above. This guide will walk you through the steps necessary to install Python 3.9 or a newer version. Afterward, you'll need to acquire a National Instruments GPIB card and install the specific NI-VISA drivers for your case. If your device is not listed in the /instruments directory, you will need to generate a file using the "template.py" file provided in the same folder. This will serve as a communication bridge between your device and the system, effectively functioning as an API.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Installation

Once you have cloned the repository or downloaded a particular release, it's essential to install the necessary dependencies. Here's how you can proceed with the process:

Firstly, you will need to install the Python requirements. Execute the following command to do so:

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

For more, please refer to the documentation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap


- [X] Create documentation
- [ ] Add step measurements


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

Distributed under the [[license-url]](GNU General Public License v3.0).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Personal Website: [Link](https://ricardosilva.super.site)

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
[license-url]: https://www.gnu.org/licenses/gpl-3.0.en.html
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