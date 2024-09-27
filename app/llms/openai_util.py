from openai import OpenAI
import json

# Set your OpenAI API key
client = OpenAI(
    # This is the default and can be omitted
    api_key='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')

def query_chatgpt(prompt, model="chatgpt-4o-latest", max_tokens=500, temperature=0.7):
    """
    Query ChatGPT using the OpenAI API.

    Args:
        prompt (str): The input prompt to send to ChatGPT.
        model (str): The model to use. Defaults to 'gpt-4'.
        max_tokens (int): The maximum number of tokens in the output. Defaults to 150.
        temperature (float): Controls randomness in the output. Defaults to 0.7.
    
    Returns:
        str: The response from ChatGPT.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful summarizer."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        # print(json.dumps(response))
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"