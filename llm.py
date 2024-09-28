from ctransformers import AutoModelForCausalLM


# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
# context_length needs to be 1024 at minimum, depending on length of persona documents. If maximum token length is
# exceeding, you can put it up to 2048.
config_llm = AutoModelForCausalLM.from_pretrained(
    model_path_or_repo_id="./models/em_german_leo_mistral.Q6_K.gguf",
    gpu_layers=0,
    context_length=1024
)


def run_llm(instruction: str, generate="generate"):
    if generate == "generate":
        output_text = config_llm(
            f"Du bist ein hilfreicher Assistent. USER: Du bekommst entweder eine Persona, eine Problembeschreibung, oder beides. Mit dem text als Vorlage generierst du mir mehrere User Stories für meinen Product Backlog. Eine User Story besteht aus einem Satz der mit '*' am Anfang gekennzeichnit ist, ohne sonst etwas hinzuzufügen:/n{instruction}!/nASSISTANT:",
            temperature=0.6,
        )
        return output_text
    else:
        output_text = config_llm(
            f"Du bist ein hilfreicher Assistent. USER: Du wirst eine User Story bekommen. Generiere mir in eine andere User Story mit gleichem Kontext, ohne sonst etwas hinzuzufügen. Die User Story soll ein einziger Satz sein. Die User Story ist:/n{instruction}!/nASSISTANT:",
            temperature=0.6,
        )
        return output_text
