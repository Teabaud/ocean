# OCEAN: Online Chatbot for Effective Altruism Navigation

## Project Overview

OCEAN (Online Chatbot for Effective Altruism Navigation) is a prototype RAG (Retrieval-Augmented Generation) chatbot designed to interact with Effective Altruism (EA) resources. This project aims to provide an intelligent interface for exploring and understanding EA concepts and information.

## Technical Stack

- **Framework**: Haystack
- **Vector Database**: Chroma
- **Embedding Model**: Sentence Transformers
- **Language Model**: Claude
- **User Interface**: Gradio
- **Project Management**: Poetry

## Features

- Retrieval-Augmented Generation for accurate and context-aware responses
- Integration with EA resources for comprehensive information
- User-friendly chat interface powered by Gradio
- Efficient vector storage and retrieval using Chroma
- High-quality embeddings generated by Sentence Transformers
- Advanced language understanding and generation with Claude

## Installation

1. Ensure you have Python 3.8+ installed.
2. Install Poetry if you haven't already:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Clone the repository:
   ```
   git clone https://github.com/teabaud/ocean.git
   cd ocean
   ```
4. Install dependencies:
   ```
   poetry install
   ```

## Usage

1. Activate the virtual environment:
   ```
   poetry shell
   ```
2. Run the application:
   ```
   python main.py
   ```
3. Open your web browser and navigate to the URL provided by Gradio (typically `http://localhost:7860`).

## Configuration

- Update `config.yaml` to modify settings such as model parameters, database configuration, and API keys.
- Ensure you have the necessary API keys for Claude and other services.

## Contributing

We welcome contributions to OCEAN! Please see our `CONTRIBUTING.md` file for guidelines on how to submit issues, feature requests, and pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Haystack framework
- Hugging Face's Sentence Transformers
- Anthropic's Claude
- Gradio team
- The Effective Altruism community for their valuable resources

## Contact

For any queries or suggestions, please open an issue on this repository or contact [Your Name/Team] at [contact email].

---

This README is part of a prototype project and may be updated as the project evolves.