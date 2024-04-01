# Gemini Python API Example

A large language model [LLM](https://cloud.google.com/ai/llms?hl=en)  is a statistical language model, trained on a massive amount of data, that can be used to generate and translate text and other content and perform other natural language processing (NLP) tasks. LLMs are typically based on deep learning architectures, such as the [Transformer](https://arxiv.org/abs/1706.03762) developed by Google in 2017, and can be trained on billions of text and other content.

Google offers an LLM called Gemini

[Gemini](https://blog.google/technology/ai/google-gemini-ai/#sundar-note) is the result of large-scale collaborative efforts by teams across Google, including our colleagues at Google Research. It was built from the ground up to be multimodal, which means it can generalize and seamlessly understand, operate across, and combine different types of information including text, code, audio, image, and video.

How to use the Python SDK for Gemini API, see this information [Gemini API for Python](https://ai.google.dev/tutorials/python_quickstart) 

This is open-source code that uses the Python SDK for Gemini API to create questions and answers from a document. This code is ready to deploy to GCP or another cloud platform.

Once is deployed the request is like this:

```json
{
    "filename": "cd832c46-9db6-4290-9f1f-7f9b80e48f60/test2.pdf",
    "amount": 5,
    "complexity": "EASY",
    "language": "en"
}
```

The structure of the response is like this:

```json
[
    {
        "question": "What is the main purpose of tuning in Google AI Studio?",
        "options": [
            "To improve the performance of Gemini models for specific tasks",
            "To train the model with new data",
            "To identify domain models",
            "To build a domain layer and business logic",
            "To containerize the service"
        ],
        "answer": "To improve the performance of Gemini models for specific tasks"
    },
    {
        "question": "Which of the following is NOT a step in the workshop?",
        "options": [
            "Identification of domain models",
            "Identification of microservices and their boundary",
            "Definition of an architecture and patterns to build microservices",
            "Construction of unit tests",
            "Deployment"
        ],
        "answer": "Construction of unit tests"
    },
    {
        "question": "What type of Machine Learning is the most common?",
        "options": [
            "Supervised Learning",
            "Unsupervised Learning",
            "Reinforcement Learning",
            "Semi-supervised Learning",
            "Transfer Learning"
        ],
        "answer": "Supervised Learning"
    },
    {
        "question": "Can LLMs generate music?",
        "options": [
            "Yes",
            "No",
            "Maybe",
            "It depends on the LLM",
            "It is not known yet"
        ],
        "answer": "Yes"
    },
    {
        "question": "What is the name of the podcast episode mentioned in the text?",
        "options": [
            "#ML",
            "#machinelearning",
            "#podcast",
            "#MLpodcast",
            "#machinelearningpodcast"
        ],
        "answer": "#ML"
    }
]
```

You can try it with the following link

```
POST
https://questionanswers-gzedfdcm3q-uc.a.run.app/apis/v1/questions
```

Made with ❤ by  [jggomez](https://devhack.co).

[![Twitter Badge](https://img.shields.io/badge/-@jggomezt-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/jggomezt)](https://twitter.com/jggomezt)
[![Linkedin Badge](https://img.shields.io/badge/-jggomezt-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/jggomezt/)](https://www.linkedin.com/in/jggomezt/)
[![Medium Badge](https://img.shields.io/badge/-@jggomezt-03a57a?style=flat-square&labelColor=000000&logo=Medium&link=https://medium.com/@jggomezt)](https://medium.com/@jggomezt)

## License

    Copyright 2024 Juan Guillermo Gómez

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
