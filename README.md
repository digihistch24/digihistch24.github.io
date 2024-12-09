# Digital History Switzerland 2024 Book of Abstracts

This repository contains the Book of Abstracts for the Digital History Switzerland 2024. Historical Research, Digital Literacy and Algorithmic Criticism. The data in this repository is openly available to everyone and is intended to support reproducible research.

[![GitHub issues](https://img.shields.io/github/issues/digihistch24/book-of-abstracts.svg)](https://github.com/digihistch24/digihistch24.github.io/issues)
[![GitHub forks](https://img.shields.io/github/forks/digihistch24/book-of-abstracts.svg)](https://github.com/digihistch24/digihistch24.github.io/network)
[![GitHub stars](https://img.shields.io/github/stars/digihistch24/book-of-abstracts.svg)](https://github.com/digihistch24/digihistch24.github.io/stargazers)
[![Code license](https://img.shields.io/github/license/digihistch24/book-of-abstracts.svg)](https://github.com/digihistch24/digihistch24.github.io/blob/main/LICENSE-AGPL.md)
[![Data license](https://img.shields.io/github/license/digihistch24/book-of-abstracts.svg)](https://github.com/digihistch24/digihistch24.github.io/blob/main/LICENSE-CCBYSA.md)

<!-- [![DOI](https://zenodo.org/badge/ZENODO_RECORD.svg)](https://zenodo.org/badge/latestdoi/ZENODO_RECORD) -->

## Installation

Install [Quarto](https://quarto.org/) and [Node.js](https://nodejs.org/) and run the following commands in the root directory of the repository:

```bash
npm install
npm run prepare
```

## Usage

### 1. Code Quality Checks

**Check Formatting**  
This command identifies files that do not follow the project’s style conventions.

```bash
npm run check
```

Expected output: A list of files with formatting issues, if any.

**Auto-Format**  
This command automatically corrects formatting issues in project files.

```bash
npm run format
```

### 2. Local Development

**Preview the Site**  
This command starts a local development server with hot-reloading to allow you to preview the website.

```bash
quarto preview blog
```

Expected output: A local preview accessible at `http://localhost:4000`.

### 3. Building for Production

**Build Static Site**  
This command compiles the website for deployment, generating static files in the `_site` directory.

```bash
quarto render blog
```

Expected output: A fully built static website in the `_site` directory, ready for deployment.

### 4. Version Control

**Commit Messages Wizard**  
This command launches an interactive prompt to help create standardized, meaningful commit messages.

```bash
npm run commit
```

Expected output: A structured prompt for crafting a detailed commit message.

**Generate Changelog**  
This command automatically creates or updates a `CHANGELOG.md` file based on recent commits.

```bash
npm run changelog
```

Expected output: An updated `CHANGELOG.md` file summarizing recent changes and updates.

## Support

This project is maintained by [@digihistch24](https://github.com/digihistch24). Please understand that we can't provide individual support via email. We also believe that help is much more valuable when it's shared publicly, so more people can benefit from it.

| Type                                   | Platforms                                                                                |
| -------------------------------------- | ---------------------------------------------------------------------------------------- |
| 🚨 **Bug Reports**                     | [GitHub Issue Tracker](https://github.com/digihistch24/digihistch24.github.io/issues)    |
| 📊 **Report bad data**                 | [GitHub Issue Tracker](https://github.com/digihistch24/digihistch24.github.io/issues)    |
| 📚 **Docs Issue**                      | [GitHub Issue Tracker](https://github.com/digihistch24/digihistch24.github.io/issues)    |
| 🎁 **Feature Requests**                | [GitHub Issue Tracker](https://github.com/digihistch24/digihistch24.github.io/issues)    |
| 🛡 **Report a security vulnerability** | See [SECURITY.md](SECURITY.md)                                                           |
| 💬 **General Questions**               | [GitHub Discussions](https://github.com/digihistch24/digihistch24.github.io/discussions) |

## Roadmap

- [x] Add all submissions to the Book of Abstracts
- [ ] Add a Table of Contents to the Book of Abstracts
- [ ] Add an introduction to the Book of Abstracts
- [x] Add styling to the Book of Abstracts

## Contributing

All contributions to this repository are welcome! If you find errors or problems with the data, or if you want to add new data or features, please open an issue or pull request. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. The available versions are listed in the [tags on this repository](https://github.com/digihistch24/digihistch24.github.io/tags).

## Authors and acknowledgment

- **Moritz Mähr** - _Initial work_ - [maehr](https://github.com/maehr)
- **Moritz Twente** - _Submissions_ - [mtwente](https://github.com/mtwente)
- **Kapitolina Kostina** - _Submissions_ - [consincopa](https://github.com/consincopa)

See also the list of [contributors](https://github.com/digihistch24/digihistch24.github.io/graphs/contributors) who contributed to this project.

## License

The data in this repository is released under the Creative Commons Attribution 4.0 International (CC BY 4.0) License - see the [LICENSE-CCBYSA](LICENSE-CCBYSA.md) file for details. By using this data, you agree to give appropriate credit to the original author(s) and to indicate if any modifications have been made.

The code in this repository is released under the GNU Affero General Public License v3.0 - see the [LICENSE-AGPL](LICENSE-AGPL.md) file for details. By using this code, you agree to make any modifications available under the same license.
