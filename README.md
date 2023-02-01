# Assistant

Little project that makes use of available language models to process requests by users and act as a voice assistant that can operate (almost entirely) locally. 
Users can make requests in natural language to get a variety of services.

The script is triggered by a wake word that then uses OpenAI's Whisper to convert a spoken request to text. 
This text is then inserted into a prompt that is fed to the GPT3 API.
The response is python-like data that can be parsed, classified and processed.

Supported features currently cover Spotify services only. 
Other web services can be easily added provided that an API is accessible. 
Like other modern voice assistants, this could enable voice-controlled home IoT automation.

The entirety of the program could be executed locally and offline given the replacement of the model that covers language comprehension, which is currently text-davinci-003, by a similar open-source model like GPT-NeoX.
This would require personal dedicated hardware but is another step towards the democratization of powerful machine learning applications.
