import json
import os
from ai.client.OllamaClient import OllamaClient
from ai.client.OpenAiClient import OpenAIClient
from data.excel.ExcelManger import ExcelManager
from exercise_details.models.AnswerModel import AnswerModel


def generate_new_column(path, new_column, model, provider, column):
    excel_df = ExcelManager(path).read()
    excel_df[new_column] = ""

    if provider == "openai":
        ai_client = OpenAIClient()
    elif provider == "ollama":
        ai_client = OllamaClient()
    else:
        raise ValueError("Invalid provider. Choose 'openai' or 'ollama'.")

    with open("./exercise_details/prompts/generate_column.txt", "r") as file:
        system_prompt = file.read()

    total_rows = len(excel_df)
    for index, row in excel_df.iterrows():
        exercise_name = row[column]
        print(f"Processing row {index + 1} of {total_rows}...")
        print(exercise_name)
        response = ai_client.ask(
            model=model,
            system_prompt=system_prompt,
            user_messages=[
                {"role": "user", "content": f"Exercise name: {exercise_name}"},
                {"role": "user", "content": f"Needed detail: {new_column}"},
            ],
            formatoutput=AnswerModel.model_json_schema(),
        )

        excel_df.at[index, new_column] = json.loads(response)["answer"]

    directory, filename = os.path.split(path)
    name, ext = os.path.splitext(filename)
    new_filename = os.path.join(
        directory, f"{name}_{new_column.replace(" ", "_")}{ext}"
    )

    excel_df.to_excel(new_filename, index=False)
    print(f"Updated Excel file saved as: {new_filename}")
