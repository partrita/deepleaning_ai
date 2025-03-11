from typing import List, Dict, Any
from llama_cpp import Llama


# GLOBAL VARIABLES
MODEL_PATH: str = "./model/zephyr-7b-beta.Q4_0.gguf"
CONTEXT_SIZE: int = 512


# LOAD THE MODEL
llm_model: Llama = Llama(model_path=MODEL_PATH,
                        n_ctx=CONTEXT_SIZE)


def generate_text_from_prompt(
    user_prompt: str,
    max_tokens: int = 100,
    temperature: float = 0.3,
    top_p: float = 0.1,
    echo: bool = True,
    stop: List[str] = ["Q", "\n"]
) -> Dict[str, Any]:
    """
    Generate text response from the LLM model based on input prompt.
    
    Args:
        user_prompt: Input text prompt
        max_tokens: Maximum number of tokens to generate
        temperature: Controls randomness in generation
        top_p: Controls diversity via nucleus sampling
        echo: Whether to echo the prompt in the output
        stop: List of strings that will stop generation when encountered
        
    Returns:
        Dictionary containing model's response and metadata
    """
    model_output = llm_model(
        user_prompt,
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        echo=echo,
        stop=stop,
    )

    return model_output


if __name__ == "__main__":
    my_prompt: str = "What do you think about the inclusion policies in Tech companies?"
    zephyr_model_response: Dict[str, Any] = generate_text_from_prompt(my_prompt)
    final_result = zephyr_model_response["choices"][0]["text"].strip()
    print(final_result)
